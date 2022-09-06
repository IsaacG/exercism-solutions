package paasio

import (
	"io"
	"sync"
)

type readCounter struct {
	r         io.Reader
	mu        sync.RWMutex
	readOps   int
	readBytes int64
}

type writeCounter struct {
	w          io.Writer
	mu         sync.RWMutex
	writeOps   int
	writeBytes int64
}

type readWriteCounter struct {
	readCounter
	writeCounter
}

func NewWriteCounter(writer io.Writer) WriteCounter {
	return &writeCounter{w: writer}
}

func NewReadCounter(reader io.Reader) ReadCounter {
	return &readCounter{r: reader}
}

func NewReadWriteCounter(readwriter io.ReadWriter) ReadWriteCounter {
	return &readWriteCounter{
		readCounter{r: readwriter},
		writeCounter{w: readwriter},
	}
}

func (rc *readCounter) Read(p []byte) (int, error) {
	rc.mu.Lock()
	defer rc.mu.Unlock()
	count, err := rc.r.Read(p)
	if err != nil {
		return 0, err
	}
	rc.readOps++
	rc.readBytes += int64(count)
	return count, nil
}

func (rc *readCounter) ReadCount() (int64, int) {
	rc.mu.RLock()
	defer rc.mu.RUnlock()
	return rc.readBytes, rc.readOps
}

func (wc *writeCounter) Write(p []byte) (int, error) {
	wc.mu.Lock()
	defer wc.mu.Unlock()
	count, err := wc.w.Write(p)
	if err != nil {
		return 0, err
	}
	wc.writeOps++
	wc.writeBytes += int64(count)
	return count, nil
}

func (wc *writeCounter) WriteCount() (int64, int) {
	wc.mu.RLock()
	defer wc.mu.RUnlock()
	return wc.writeBytes, wc.writeOps
}
