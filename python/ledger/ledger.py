# -*- coding: utf-8 -*-
"""Ledger formatting."""

# Changelog:
# * Import module, not classes.
# * Use dataclass for LedgerEntry.
# * Replace sorting block with sorted() and dataclass ordering.
# * Use string formating for header row.
# * Use date formatting for formatting the date.
# * Build rows as a list over a single string.
# * Move row formatting into LedgerEntry format().
# * Pull date formatting, description truncation out of conditional.
# * Fix description formatting to use a slice/ljust().
# * Use format string to format the row from parts.
# * Add a fmt_decimal that accepts ki and dec separators.
# * Move currency formatting into a function and use a template string.

import dataclasses
import datetime

# Currency symbols.
SYMBOL = {'USD': '$', 'EUR': '€'}


@dataclasses.dataclass(order=True)
class LedgerEntry:
    """Ledger entry."""
    date: datetime.datetime
    description: str
    change: int


@dataclasses.dataclass
class Formatter:
    """Formatter is used to format values."""

    # Date format string.
    date: str
    # Number separators: thousands and decimal.
    k_sep: str
    d_sep: str
    # Currency format string. (positive and negative amounts).
    currency: dict[bool, str]
    headers: list[str]

    def format_decimal(self, num: int) -> str:
        """Format a decimal number."""
        assert num >= 0, "Absolute values only"
        val = num // 100
        # Join thousands with the k_sep.
        whole = f"{val:_}".replace("_", self.k_sep)
        # Add the decimal part.
        return f'{whole}{self.d_sep}{num % 100:02}'

    def format_cur(self, amount: int, currency: str) -> str:
        """Format the currency change."""
        return self.currency[amount >= 0].format(
            symbol=SYMBOL[currency],
            num=self.format_decimal(abs(amount))
        )

    def format_date(self, date) -> str:
        """Format a date."""
        return date.strftime(self.date)

    @staticmethod
    def format_description(description) -> str:
        """Format a description."""
        if len(description) > 25:
            description = description[:22] + '...'
        return description

    def format_entry(self, entry: LedgerEntry, currency: str) -> str:
        """Format one entry."""
        date = self.format_date(entry.date)
        description = self.format_description(entry.description)
        change = self.format_cur(entry.change, currency)

        # Combine columns.
        return f'{date:<10} | {description:<25} | {change:>13}'

    def format(self, entries: list[LedgerEntry], currency: str) -> str:
        """Return entries formatted to a table."""
        parts = self.headers
        header = f'{parts[0]:<10} | {parts[1]:<25} | {parts[2]:<13}'
        rows = [header] + [self.format_entry(entry, currency) for entry in sorted(entries)]
        return '\n'.join(rows)


FMT = {
    'en_US': Formatter(
        date='%m/%d/%Y',
        k_sep = ',',
        d_sep = '.',
        currency = {True: '{symbol}{num} ', False: '({symbol}{num})'},
        headers = ['Date', 'Description', 'Change'],
    ),
    'nl_NL': Formatter(
        date='%d-%m-%Y',
        k_sep = '.',
        d_sep = ',',
        currency = {True: '{symbol} {num} ', False: '{symbol} -{num} '},
        headers = ['Datum', 'Omschrijving', 'Verandering'],
    ),
}


def create_entry(date: str, description: str, change: int) -> LedgerEntry:
    """Return a LedgerEntry."""
    pdate = datetime.datetime.strptime(date, '%Y-%m-%d')
    return LedgerEntry(pdate, description, change)


def format_entries(currency: str, locale: str, entries: list[LedgerEntry]) -> str:
    """Format LedgerEntry values."""
    return FMT[locale].format(entries, currency)
