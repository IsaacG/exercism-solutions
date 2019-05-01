// Package protein translates between codons and proteins.
package protein

import "errors"

var (
	// ErrStop is returned when a STOP protein is found
	ErrStop = errors.New("STOP")
	// ErrInvalidBase is returned on an invalid codon
	ErrInvalidBase = errors.New("Invalid")
	proteins       = map[string]string{
		"AUG": "Methionine",
		"UUU": "Phenylalanine",
		"UUC": "Phenylalanine",
		"UUA": "Leucine",
		"UUG": "Leucine",
		"UCU": "Serine",
		"UCC": "Serine",
		"UCA": "Serine",
		"UCG": "Serine",
		"UAU": "Tyrosine",
		"UAC": "Tyrosine",
		"UGU": "Cysteine",
		"UGC": "Cysteine",
		"UGG": "Tryptophan",
		"UAA": "STOP",
		"UAG": "STOP",
		"UGA": "STOP",
	}
)

// FromCodon maps a codon to a protein
func FromCodon(s string) (string, error) {
	p, ok := proteins[s]
	if !ok {
		return "", ErrInvalidBase
	}

	if p == "STOP" {
		return "", ErrStop
	}
	return p, nil
}

// FromRNA maps an RNA string to a slice of proteins
func FromRNA(s string) ([]string, error) {
	var proteins []string
	for i := 0; i+3 <= len(s); i += 3 {
		p, err := FromCodon(s[i : i+3])
		if err == ErrInvalidBase {
			return proteins, err
		} else if err == ErrStop {
			return proteins, nil
		} else {
			proteins = append(proteins, p)
		}
	}
	return proteins, nil
}
