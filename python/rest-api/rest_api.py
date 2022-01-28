"""REST API for an IOU service."""

import collections
import dataclasses
import json
from typing import cast, Optional, Union


@dataclasses.dataclass(order=True)
class User:
    """One person and how much they owe or are owed.

    Debts this person owes are arbitrarily positive while money owed to this person
    are negative.
    """

    name: str
    # A collection of debts owed to or from this user.
    debts: collections.defaultdict[str, float] = dataclasses.field(
        default_factory=lambda: collections.defaultdict(float)
    )

    def balance(self) -> float:
        """Return the balance of debts owed to/from this person."""
        return -sum(self.debts.values())

    def asdict(self):
        """Return a formatted dict for this user."""
        return {
            "name": self.name,
            "owes": {name: amount for name, amount in self.debts.items() if amount > 0},
            "owed_by": {name: -amount for name, amount in self.debts.items() if amount < 0},
            "balance": self.balance(),
        }


class RestAPI:
    """IOU API."""

    def __init__(self, database=None):
        """Initialize the data."""
        users = database["users"] if database else []
        self._data = {}
        for user in users:
            record = User(user["name"])
            record.debts.update(user["owes"])
            # Money owed to this user is tracked as a negative debt.
            record.debts.update({name: -amount for name, amount in user["owed_by"].items()})
            self._data[user["name"]] = record

    def get(self, url: str, payload: Optional[str] = None) -> str:
        """Return a list of user info, optionally filtered."""
        assert url == "/users"
        want = json.loads(payload)["users"] if payload else None
        return self._get(want)

    def _get(self, want: Optional[list[str]]) -> str:
        """Return a list of filtered user info."""
        users = sorted(self._data.values())
        if want:
            users = [user for user in users if user.name in want]
        return json.dumps({"users": [user.asdict() for user in users]})

    def post(self, url: str, payload: Optional[str] = None) -> str:
        """Handle POST requests: add and iou."""
        assert payload is not None
        parsed = json.loads(payload)
        if url == "/add":
            return self.add(parsed)
        if url == "/iou":
            return self.iou(parsed)
        return NotImplemented

    def add(self, payload: dict[str, str]) -> str:
        """Add a user to the database."""
        name = payload["user"]
        user = User(name)
        self._data[name] = user
        return json.dumps(user.asdict())

    def iou(self, payload: dict[str, Union[str, float]]) -> str:
        """Record a debt."""
        lender = cast(str, payload["lender"])
        borrower = cast(str, payload["borrower"])
        amount = cast(float, payload["amount"])
        self._data[borrower].debts[lender] += amount
        self._data[lender].debts[borrower] -= amount
        return self._get([lender, borrower])
