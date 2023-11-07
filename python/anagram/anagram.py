from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    word_count = Counter(word.lower())
    return [
        c for c in candidates
        if c.lower() != word.lower() and word_count == Counter(c.lower())
    ]
