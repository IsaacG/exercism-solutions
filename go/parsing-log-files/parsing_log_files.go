// Package parsinglogfiles provides helpers for parsing log files.
package parsinglogfiles

import (
	"fmt"
	"regexp"
)

// IsValidLine returns if a log line is valid.
func IsValidLine(text string) bool {
	re := regexp.MustCompile(`^\[(TRC|DBG|INF|WRN|ERR|FTL)\]`)
	return re.MatchString(text)
}

// SplitLogLine returns a log line, split into parts.
func SplitLogLine(text string) []string {
	re := regexp.MustCompile(`<[~*=-]*>`)
	return re.Split(text, -1)
}

// CountQuotedPasswords returns the number of quoted passwords.
func CountQuotedPasswords(lines []string) int {
	re := regexp.MustCompile(`(?i)".*password.*"`)
	count := 0
	for _, line := range lines {
		if re.MatchString(line) {
			count++
		}
	}
	return count
}

// RemoveEndOfLineText removes line endings from a log entry.
func RemoveEndOfLineText(text string) string {
	re := regexp.MustCompile(`end-of-line\d+`)
	return re.ReplaceAllString(text, "")
}

// TagWithUserName returns log entries with optional USR tags added.
func TagWithUserName(lines []string) []string {
	result := []string{}
	re := regexp.MustCompile(`User\s+(\w+)`)
	for _, line := range lines {
		if re.MatchString(line) {
			matches := re.FindStringSubmatch(line)
			result = append(result, fmt.Sprintf("[USR] %s %s", matches[1], line))
		} else {
			result = append(result, line)
		}
	}
	return result
}
