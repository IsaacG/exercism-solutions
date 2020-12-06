import string

mapping = {string.ascii_lowercase[i]: string.ascii_lowercase[25 - i] for i in range(26)}
mapping.update({i: i for i in string.digits})
alnum = string.ascii_letters + string.digits

def encode(text):
  text = text.lower()
  text = (t for t in text if t in alnum)
  text = list(mapping[t] for t in text)
  r = (''.join(text[i:i+5]) for i in range(0, len(text), 5))

  return ' '.join(r)


def decode(text):
  text = text.replace(' ', '')
  return ''.join(mapping[t] for t in text)


# vim:ts=2:sw=2:expandtab
