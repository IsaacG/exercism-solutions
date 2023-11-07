"""Functions to automate Conda airlines ticketing system."""
import collections.abc
import itertools


def generate_seat_letters(number: int) -> collections.abc.Generator[str, None, None]:
    """Generate a series of letters for airline seats."""
    cycle = itertools.cycle("ABCD")
    for _ in range(number):
        yield next(cycle)


def generate_seats(number: int) -> collections.abc.Generator[str, None, None]:
    """Generate a series of identifiers for airline seats."""
    rows = (i for i in itertools.count(start=1) if i != 13 for _ in range(4))
    letters = generate_seat_letters(number)
    for row, letter in zip(rows, letters):
        yield str(row) + letter


def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Assign seats to passengers."""
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers: list[str], flight_id: str) -> collections.abc.Generator[str, None, None]:
    """Generate codes for a ticket."""
    for seat in seat_numbers:
        yield (seat + flight_id).ljust(12, "0")
