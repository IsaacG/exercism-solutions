"""Make change with fewest coins."""
import functools
import itertools
import queue
from typing import Optional


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target < 0:
        raise ValueError("target can't be negative")

    # res = find_fewest_coins_queue(coins, target)
    # res = find_fewest_coins_tree(coins, target)
    res = find_fewest_coins_manual(coins, target)
    # res = find_fewest_coins_itertools(coins, target)
    if res is None:
        raise ValueError("can't make target with given coins")
    return sorted(res)


def find_fewest_coins_queue(coins: list[int], target: int) -> list[int]:
    """Solve using a PriorityQueue and a while-loop; no recursion."""

    coins = sorted(coin for coin in coins if coin <= target)
    options = queue.PriorityQueue()
    options.put((0, coins, target, tuple()))

    while not options.empty():
        size, coins, target, used = options.get()
        if target == 0:
            return list(used)
        if not coins:
            continue
        biggest = coins[-1]
        # Try solving with the largest coin removed from the options.
        scenario = (size, coins[:-1], target, used)
        options.put(scenario)

        # Try solving with the largest coin being used.
        next_target = target - biggest
        next_coins = [coin for coin in coins if coin <= next_target]
        scenario = (size + 1, next_coins, next_target, used + (biggest,))
        options.put(scenario)

    return None


def find_fewest_coins_tree(coins: list[int], target: int) -> list[int]:
    """Solve using recursion, dynamic programming, trying with and without the largest coin."""

    @functools.cache
    def solve(coins: frozenset[int], target: int, max_size: int) -> Optional[list[list[int]]]:
        if target in coins:
            return [[target]]
        coins = frozenset(coin for coin in coins if coin <= target)
        if not coins or not depth:
            return None
        biggest = max(coins)
        options = []
        if (sub_solution := solve(coins, target - biggest, max_size)) is not None:
            options.extend(s + [biggest] for s in sub_solution)
        if (sub_solution := solve(frozenset(coins - {biggest}), target, max_size)) is not None:
            options.extend(s for s in sub_solution if s)
        return [option for option in options if len(option) <= max_size] or None

    if target == 0:
        return []
    max_size = target // min(coins)
    for depth in range(1, max_size + 1):
        if options := solve(frozenset(coins), target, depth):
            return options[0]
    return None


def find_fewest_coins_itertools(coins: list[int], target: int) -> list[int]:
    """Return how to make change with fewest coins."""
    if target == 0:
        return []
    worst = target // min(coins)
    for count in range(1, worst + 1):
        print(count, worst + 1)
        for change in itertools.combinations_with_replacement(coins, count):
            if sum(change) == target:
                return list(change)
    return None


def find_fewest_coins_manual(coins: list[int], target: int) -> list[int]:
    """Return how to make change with fewest coins."""

    @functools.cache
    def solve(sub: int) -> Optional[list[int]]:
        """Solve for a sub-problem."""
        if sub == 0:
            return []

        options = []
        # All the coins are too large to make change.
        if all(coin > sub for coin in coins):
            return None
        # Optimization: ignore small coins when there are much larger coins.
        # Avoids trying to use coin=1 when we can apply coin=100.
        threshold = max(coin for coin in coins if coin <= sub) / 25
        for coin in coins:
            if coin > sub:
                continue
            if coin < threshold:
                continue
            # Using a given coin, solve for the remainder.
            found = solve(sub - coin)
            if found is not None:
                options.append(found + [coin])
        if not options:
            return None
        return sorted(options, key=len)[0]

    return solve(target)
