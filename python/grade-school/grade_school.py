"""Grade School Roster."""
import collections

class School:
    """Roster."""
    def __init__(self):
        """Initialize."""
        self._grades = collections.defaultdict(set)
        self._added = []

    def add_student(self, name: str, grade: int) -> None:
        """Add a student to the roster if not yet present."""
        not_exists = not any(name in names for names in self._grades.values())
        self._added.append(not_exists)
        if not_exists:
            self._grades[grade].add(name)

    def added(self) -> list[bool]:
        """Return a list of whether or not a student was added."""
        return self._added

    def roster(self) -> list[str]:
        """Return the student roster."""
        roster = []
        for grade in sorted(self._grades):
            roster.extend(self.grade(grade))
        return roster

    def grade(self, grade_number: int) -> list[str]:
        """Return the roster for a grade."""
        return sorted(self._grades[grade_number])
