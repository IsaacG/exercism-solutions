import string

def is_pangram(sentence):
    sentence = sentence.lower()
    return all(i in sentence for i in string.ascii_lowercase)
    return set(sentence).issuperset(set(string.ascii_lowercase))
    return {i for i in sentence if i.isalpha()} == set(string.ascii_lowercase)
    return len({i for i in sentence if i.isalpha()}) == 26

    unfound = set(string.ascii_lowercase)
    for letter in sentence:
        if letter in unfound:
            unfound.remove(letter)
        if not unfound:
            return True
    return False
