TRANSLATION = {"G": "C", "C": "G", "A": "U", "T": "A"}


def to_rna(dna_strand: str) -> str:
    return "".join(TRANSLATION[i] for i in dna_strand)
