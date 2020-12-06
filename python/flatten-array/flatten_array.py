def flatten(val):
  if val is None:
    return []
  if not isinstance(val, list):
    return [val]
  return [j for i in val for j in flatten(i)]


def longform(iterable):
  out = []
  for i in iterable:
    if isinstance(i, list):
      out.extend(flatten(i))
    elif i is not None:
      out.append(i)
  return out


# vim:ts=2:sw=2:expandtab
