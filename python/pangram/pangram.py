import string

def is_pangram(sentence):
  sentence = sentence.lower()
  return all(i in sentence for i in string.ascii_lowercase)
