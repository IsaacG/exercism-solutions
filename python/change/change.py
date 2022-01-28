"""Make change with fewest coins."""
import functools
import itertools
from typing import Optional


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """Return how to make change with fewest coins."""
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    worst = target // min(coins)
    for count in range(1, worst + 1):
        print(count, worst + 1)
        for change in itertools.combinations_with_replacement(coins, count):
            if sum(change) == target:
                return list(change)
    raise ValueError("can't make target with given coins")


def find_fewest_coins_manual(coins: list[int], target: int) -> list[int]:
    """Return how to make change with fewest coins."""
    if target < 0:
        raise ValueError("target can't be negative")

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

    res = solve(target)
    if res is None:
        raise ValueError("can't make target with given coins")
    return sorted(res)
