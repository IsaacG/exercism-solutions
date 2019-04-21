def slices(series, length):
  if not series or length < 1:
    raise ValueError('foo')
  if length > len(series):
    raise ValueError('foo')

  res = []
  for i in range(len(series) - length + 1):
    res.append(series[i:i+length])
  return res

# vim:ts=2:sw=2:expandtab
