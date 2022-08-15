def slices(series, length):
  if length == 0:
    raise ValueError('slice length cannot be zero')
  if length < 0:
    raise ValueError('slice length cannot be negative')
  if not series:
    raise ValueError('series cannot be empty')
  if length > len(series):
    raise ValueError('slice length cannot be greater than series length')

  res = []
  for i in range(len(series) - length + 1):
    res.append(series[i:i+length])
  return res

# vim:ts=2:sw=2:expandtab
