ALLERGENS = (
  'eggs', 'peanuts', 'shellfish', 'strawberries',
  'tomatoes', 'chocolate', 'pollen', 'cats')


class Allergies(object):

    def __init__(self, score):
        self._lst = [
          a for i, a in enumerate(ALLERGENS)
          if (score & (1 << i))]

    def allergic_to(self, item):
        return item in self._lst

    @property
    def lst(self):
        return self._lst


# vim:ts=2:sw=2:expandtab
