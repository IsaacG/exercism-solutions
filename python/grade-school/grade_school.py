import collections

class School:
  def __init__(self):
    self._grades = collections.defaultdict(set)

  def add_student(self, name, grade):
    self._grades[grade].add(name)

  def roster(self):
    roster = []
    for grade in sorted(self._grades):
      roster.extend(self.grade(grade))
    return roster

  def grade(self, grade_number):
    return sorted(self._grades[grade_number])
