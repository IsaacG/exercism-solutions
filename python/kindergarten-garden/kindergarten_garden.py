_STUDENTS = [
  'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
  'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

_PLANTS = {
  n[0]: n for n in ('Grass', 'Clover', 'Radishes', 'Violets')}

class Garden:
  def __init__(self, diagram, students=None):
    self.students = students or _STUDENTS
    self.students.sort()
    self.rows = diagram.split()

  def plants(self, student):
    idx = self.students.index(student)
    return [
      self.lookup(i, 2 * idx + j)
      for i in (0, 1) for j in (0, 1)]

  def lookup(self, r, c):
    return _PLANTS[self.rows[r][c]]

# vim:ts=2:sw=2:expandtab
