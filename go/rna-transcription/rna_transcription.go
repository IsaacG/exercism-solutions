package strand

import "strings"

func mapping (r rune) rune {
	switch r {
		case 'A': return 'U'
		case 'C': return 'G'
		case 'G': return 'C'
		case 'T': return 'A'
	}
	return '-'
}

func ToRNA(dna string) string {
	return strings.Map(mapping, dna)
}
