"""Translate text to pig Latin."""
import re


def translate(text: str) -> str:
    """Translate a sentence to pig Latin."""
    return " ".join(word_trans(word) for word in text.split())


def word_trans(word: str) -> str:
    """Translate a word to pig Latin.

    Some word patterns just get a trailing "ay". Special case those by start.

    For other words, split into the "start" and "rest", moving "start" to the end.
    The exact split pattern depends on how the word starts.
    """
    if any(word.startswith(pat) for pat in ("xr", "yt")):
        return word + "ay"

    # If the starts contains "qu", do not split on "u".
    if re.match(r"[^aeiou]*qu", word):
        pattern = r"([^aeioy]*)([aeioy].*)"
    # If the word starts with a "y", keep "y" in the start.
    elif word[0] == "y":
        pattern = r"([^aeiou]*)([aeiou].*)"
    # Default is to split at the first vowel.
    else:
        pattern = r"([^aeiouy]*)([aeiouy].*)"
    re_match = re.match(pattern, word)
    assert re_match
    return re_match.group(2) + re_match.group(1) + "ay"
