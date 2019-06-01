def response(hey):
  if not hey or hey.isspace():
    return 'Fine. Be that way!'
  if hey.strip().endswith('?'):
    return "Calm down, I know what I'm doing!" if hey.isupper() else 'Sure.'
  else:
    return 'Whoa, chill out!' if hey.isupper() else 'Whatever.'

# vim:ts=2:sw=2:expandtab
