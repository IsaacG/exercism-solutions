# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
  def __init__(self, word):
    self.remaining_guesses = 9
    self.status = STATUS_ONGOING
    self.word = word
    self.guesses = set()

  def guess(self, char):
    if self.status != STATUS_ONGOING:
      raise ValueError('The game has already ended.')

    # Reduce guess count on a wrong or repeated guess.
    if char not in self.word or char in self.guesses:
      self.remaining_guesses -= 1
    # Track the guess.
    self.guesses.add(char)

    # Win if all the letters in the word were guessed.
    if set(self.word).issubset(self.guesses):
      self.status = STATUS_WIN

    if self.remaining_guesses < 0:
      self.status = STATUS_LOSE

  def get_masked_word(self):
    return ''.join(
        c if c in self.guesses else '_'
        for c in self.word)

  def get_status(self):
    return self.status


# vim:ts=2:sw=2:expandtab
