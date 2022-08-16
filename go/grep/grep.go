// Package grep implements grep.
package grep

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

// Match represents a matching line.
type Match struct {
	Filename   string
	LineNumber int
	Text       string
}

// Formatter formats grep results.
type Formatter struct {
	IncludeFilename bool
	OnlyFilename    bool
	IncludeLineNum  bool
	Invert          bool
	FullLine        bool
	CaseSensitive   bool
}

func (f *Formatter) withFilename() {
	f.IncludeFilename = true
}

func (f *Formatter) filenameOnly() {
	f.OnlyFilename = true
}

func (f *Formatter) withLineNumber() {
	f.IncludeLineNum = true
}

func (f *Formatter) invertMatch() {
	f.Invert = true
}

func (f *Formatter) matchFullLine() {
	f.FullLine = true
}

func (f *Formatter) caseInsensitive() {
	f.CaseSensitive = false
}

// NewFormatter builds a formatter from flags.
func NewFormatter(flags []string, multiFile bool) *Formatter {
	// Defaults
	formatter := &Formatter{
		IncludeFilename: false,
		OnlyFilename:    false,
		IncludeLineNum:  false,
		Invert:          false,
		FullLine:        false,
		CaseSensitive:   true,
	}
	// Map flags to options and apply.
	for _, flag := range flags {
		switch flag {
		case "-x":
			formatter.matchFullLine()
		case "-i":
			formatter.caseInsensitive()
		case "-l":
			formatter.filenameOnly()
		case "-n":
			formatter.withLineNumber()
		case "-v":
			formatter.invertMatch()
		}
	}
	if multiFile {
		formatter.withFilename()
	}
	return formatter
}

// formatter formats results from a chan.
func (f *Formatter) format(matches <-chan Match, out chan<- []string) {
	results := []string{}

	for m := range matches {
		if f.OnlyFilename {
			results = append(results, m.Filename)
		} else {
			parts := make([]string, 0, 3)
			if f.IncludeFilename {
				parts = append(parts, m.Filename)
			}
			if f.IncludeLineNum {
				parts = append(parts, strconv.Itoa(m.LineNumber))
			}
			parts = append(parts, m.Text)
			results = append(results, strings.Join(parts, ":"))
		}
	}
	out <- results
}

// Search for a pattern.
func Search(pattern string, flags, files []string) []string {
	matchChan := make(chan Match, 1)
	out := make(chan []string)
	defer close(out)

	// Format the results async.
	f := NewFormatter(flags, len(files) > 1)
	go f.format(matchChan, out)

	if !f.CaseSensitive {
		pattern = strings.ToLower(pattern)
	}

	// Check each file.
	for _, filename := range files {
		fh, err := os.Open(filename)
		if err != nil {
			panic("unable to open file: " + filename)
		}
		defer fh.Close()

		fileScanner := bufio.NewScanner(fh)
		fileScanner.Split(bufio.ScanLines)
		// Check each line in the file.
		for i := 1; fileScanner.Scan(); i++ {
			line := fileScanner.Text()
			// Match the line using various options.
			checkLine := line
			if !f.CaseSensitive {
				checkLine = strings.ToLower(checkLine)
			}
			var lineMatches bool
			if f.FullLine {
				lineMatches = checkLine == pattern
			} else {
				lineMatches = strings.Contains(checkLine, pattern)
			}

			// Handle a match.
			if lineMatches != f.Invert {
				matchChan <- Match{filename, i, line}
				if f.OnlyFilename {
					break
				}
			}
		}
	}
	close(matchChan)
	return <-out
}
