def rotate(matrix):
  """Rotate a matrix so we can access a column as a list."""
  return [[c[i] for c in matrix]
          for i in range(len(matrix[0]))]


def saddle_points(matrix):
  points = []

  # Empty
  if not matrix:
    return points
  # Not uniform shape
  if not all(len(r) == len(matrix[0]) for r in matrix):
    raise ValueError("irregular matrix")

  rot = rotate(matrix)

  for y in range(len(matrix)):
    for x in range(len(matrix[0])):
      v = matrix[y][x]
      if v == max(matrix[y]) and v == min(rot[x]):
        points.append({"row": y + 1, "column": x + 1})
  return points


# vim:ts=2:sw=2:expandtab
