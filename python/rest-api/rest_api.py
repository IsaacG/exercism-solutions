"""REST API for an IOU service."""

import collections
import dataclasses
import json
from typing import Callable, Optional, Union


@dataclasses.dataclass(order=True)
class User:
    """One person and how much they owe or are owed."""

    name: str
    # A collection of debts owed to or from this user.
    debts: collections.defaultdict[str, float] = dataclasses.field(
        default_factory=lambda: collections.defaultdict(float)
    )

    def asdict(self):
        """Return a formatted dict for this user."""
        return {
            "name": self.name,
            "owes": {name: amount for name, amount in self.debts.items() if amount > 0},
            "owed_by": {name: -amount for name, amount in self.debts.items() if amount < 0},
            "balance": -sum(self.debts.values()),
        }


class Database(dict):
    """User database which auto-adds on lookup."""

    def __missing__(self, name) -> User:
        """Add a User if they are not in the database."""
        self[name] = User(name)
        return self[name]


def json_encoded(func: Callable[["RestAPI", str, Optional[str]], Union[User, list[User]]]):
    """Call an API endpoint and return the JSON formatted data."""

    def wrapper(self, url: str, payload: Optional[str] = None) -> str:
        encoder = json.JSONEncoder(default=lambda u: u.asdict())
        data = func(self, url, payload)
        if isinstance(data, list):
            return encoder.encode({"users": sorted(data)})
        return encoder.encode(data)

    return wrapper


class RestAPI:
    """IOU API."""

    def __init__(self, database=None):
        """Initialize the data."""
        users = database["users"] if database else []
        self._data = Database()
        for user in users:
            _ = self._data[user["name"]]  # Ensure the name is in the database
            for lender, amount in user["owes"].items():
                self.record_debt(user["name"], lender, amount)

    @json_encoded
    def get(self, url: str, payload: Optional[str] = None) -> list[User]:
        """Return a list of user info, optionally filtered."""
        assert url == "/users"
        names = json.loads(payload)["users"] if payload else self._data.values()
        return [self._data[name] for name in names]

    @json_encoded
    def post(self, url: str, payload: Optional[str] = None) -> Union[User, list[User]]:
        """Handle POST requests: add and iou."""
        assert payload is not None
        parsed = json.loads(payload)
        if url == "/add":
            return self._data[parsed["user"]]
        if url == "/iou":
            borrower, lender, amount = parsed["borrower"], parsed["lender"], parsed["amount"]
            self.record_debt(borrower, lender, amount)
            return [self._data[name] for name in (borrower, lender)]
        return NotImplemented

    def record_debt(self, borrower: str, lender: str, amount: float) -> None:
        """Update the database with a new debt."""
        self._data[borrower].debts[lender] += amount
        self._data[lender].debts[borrower] -= amount
