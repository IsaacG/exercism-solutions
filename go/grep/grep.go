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

// Opts stores grep options.
type Opts struct {
	IncludeFilename bool
	IncludeLineNum  bool
	OnlyFilename    bool
	Invert          bool
	FullLine        bool
	CaseSensitive   bool
}

func getOpts(flags []string) Opts {
	o := Opts{
		CaseSensitive: true,
	}
	for _, flag := range flags {
		switch flag {
		case "-x":
			o.FullLine = true
		case "-i":
			o.CaseSensitive = false
		case "-l":
			o.OnlyFilename = true
		case "-n":
			o.IncludeLineNum = true
		case "-v":
			o.Invert = true
		}
	}
	return o
}

// formatter formats results from a chan.
func formatter(o Opts, matches <-chan Match, out chan<- []string) {
	results := []string{}

	for m := range matches {
		if o.OnlyFilename {
			results = append(results, m.Filename)
		} else {
			parts := make([]string, 0, 3)
			if o.IncludeFilename {
				parts = append(parts, m.Filename)
			}
			if o.IncludeLineNum {
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
	o := getOpts(flags)
	o.IncludeFilename = len(files) > 1

	matchChan := make(chan Match)
	out := make(chan []string)
	defer close(out)

	// Format the results async.
	go formatter(o, matchChan, out)

	if !o.CaseSensitive {
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
			if !o.CaseSensitive {
				checkLine = strings.ToLower(checkLine)
			}
			var lineMatches bool
			if o.FullLine {
				lineMatches = checkLine == pattern
			} else {
				lineMatches = strings.Contains(checkLine, pattern)
			}

			// Handle a match.
			if lineMatches != o.Invert {
				matchChan <- Match{filename, i, line}
				if o.OnlyFilename {
					break
				}
			}
		}
	}
	close(matchChan)
	return <-out
}
