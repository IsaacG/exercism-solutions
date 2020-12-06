"""Lowest price finder, by trying out different groupings.

So long as we are careful about how we add books to each grouping,
we don't need to actually track which book is in the grouping.
We just need the size of the grouping.
It doesn't matter if the grouping contains titles [A, B, C]
or [A, D, F]. It's three unique titles either way.

If we insert books into groups, one title at a time, and only
one copy of the title per group, we don't need to track what
titles are in the group.

We could skip straight to step 3 and brute force.
Steps 1 and 2 provide optimizations.

Step 1.
Whichever book shows up the most times (N times) determines
how many groupings are needed. We can't double them up so
there cannot be fewer groupings. If we have more groupings,
we can merge them.

If three books show up five times, we will have five groups
which all contain those three books as the starting scenario.

Step 2.
Looking at the remaining books, pick whichever occurs the most
(M times).
Since all the groups are the same, place that next book in the
first M groups. Different combos will result in the same
exact groupings, though in differing orders.

Step 3.
Brute force.
At this point, we need to consider more possibilities.
For each remaining title, attempt to place it in each
combination of buckets and see which results in the
lowest price.
"""

import collections
import itertools
from typing import Mapping, List

# The price paid for various group sizes.
DISCOUNT = {1: 1.00, 2: 0.95, 3: 0.90, 4: 0.80, 5: 0.75}
# The total price per grouping, by group size.
PRICE = {n: int(800 * n * d) for n, d in DISCOUNT.items()}


class Grouping:
  """Represents a set of books, organized into groups.

  All we actually need to store here is the count of unique
  titles per group so long as we manage groupings in a way
  that prevents adding a title twice to one group.
  """

  def __init__(self, bookset: List[int]):
    self._bookset = bookset

  def Price(self) -> int:
    """Returns the discounted price of the books."""
    return sum(PRICE[b] for b in self._bookset)

  def WithBookIn(self, group_idxs: List[int]) -> 'Grouping':
    """Return a new grouping with a new title added to specific groups."""
    bookset = list(self._bookset)
    for idx in group_idxs:
      bookset[idx] += 1
    return Grouping(bookset)


class Possibilities:
  """A collection of possible groupings of the books."""

  def __init__(self, basket: Mapping[int, int]):
    self._num_groups = max(basket.values() or [0])
    self._possibilities = [Grouping([0] * self._num_groups)]

  def MinPrice(self) -> int:
    """Return the price of the cheapest possible grouping."""
    return min(p.Price() for p in self._possibilities)

  def UpdateFirstPossibility(self, book_count: int, group_count: int):
    """Inplace update of the titles in the first possibility.
  
    This is used to build out the base case before diverging
    into multiple branches.
    """
    for group in range(group_count):
      self._possibilities[0]._bookset[group] += book_count

  def AddInAllCombos(self, book_count: int):
    """Add a book title to the groups in all possible combos.

    This operation expands the number of possibilities by trying
    all combos.
    """
    new_possibilities = []
    for grouping in self._possibilities:
      # Given N groups and M counts of a book, get combos C(N, M)
      combos = itertools.combinations(range(self._num_groups), book_count)
      for selected_groups in combos:
        new_groupings = grouping.WithBookIn(selected_groups)
        new_possibilities.append(new_groupings)
    self._possibilities = new_possibilities


def BuildPossibilities(books: List[int]) -> Possibilities:
  """Generate a Possibilities with all good groupings.

  Some optimizations are done to ignore more expensive groupings.
  """
  basket = collections.Counter(books)
  possibilities = Possibilities(basket)
  books_used = set()

  if set(basket) == books_used:
    return possibilities

  # The number of groups is controlled by the most common book found.
  num_groups = max(basket.values() or [0])
  common_titles = [
      book for book, count in basket.items() if count == num_groups]
  # Start by placing the most-common-titles into each basket,
  # using just one possible distribution for now.
  possibilities.UpdateFirstPossibility(len(common_titles), num_groups)
  books_used.update(common_titles)

  if set(basket) == books_used:
    return possibilities

  # Place the second most common title into the first M groups.
  # Picking exactly one title from the basket (which shows up
  # more than any other group, ie M times), place that title
  # into the first M groups.
  # Since the groups at this point are all the same, the order
  # does not matter for this step.
  second_highest_count = max(
      i for i in basket.values() if i != num_groups)
  book = [
      book for book, count in basket.items()
      if count == second_highest_count][0]
  possibilities.UpdateFirstPossibility(1, second_highest_count)
  books_used.add(book)

  if set(basket) == books_used:
    return possibilities

  # Brute force stage. Try all combos.
  # For each title in the basket, try placing it in every
  # combination of groups. Each try creates a new possibility.
  remaining = set(basket) - books_used
  for book in remaining:
    possibilities.AddInAllCombos(basket[book])
    books_used.add(book)
  
  if set(basket) == books_used:
    return possibilities
  
  raise RuntimeError('How are there books left?')


def total(basket):
  return BuildPossibilities(basket).MinPrice()


# vim:ts=2:sw=2:expandtab
