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


FMT = {
    # Date format string.
    'date': {'en_US': '%m/%d/%Y', 'nl_NL': '%d-%m-%Y'},
    # Number separators: thousands and decimal.
    'sep': {'en_US': (',', '.'), 'nl_NL': ('.', ',')},
    # Currency format string. (locale, positive).
    'currency': {
        ('en_US', True): '{symbol}{num} ',
        ('en_US', False): '({symbol}{num})',
        ('nl_NL', True): '{symbol} {num} ',
        ('nl_NL', False): '{symbol} -{num} ',
    },
    # Header values.
    'headers': {
        'en_US': ('Date', 'Description', 'Change'),
        'nl_NL': ('Datum', 'Omschrijving', 'Verandering'),
    },
}
# Currency symbols.
SYMBOL = {'USD': '$', 'EUR': '€'}


@dataclasses.dataclass(order=True)
class LedgerEntry:
    """Ledger entry."""
    date: datetime.datetime
    description: str
    change: int

    @staticmethod
    def fmt_decimal(locale: str, num: int) -> str:
        """Format a decimal number."""
        assert num >= 0, "Absolute values only"
        k_sep, d_sep = FMT['sep'][locale]
        val = num // 100
        parts = []
        if val == 0:
            parts.append('0')
        # Split the number into thousands.
        while val:
            parts.append(str(val % 1000))
            val //= 1000
        # Join thousands with the k_sep.
        whole = k_sep.join(reversed(parts))
        # Add the decimal part.
        return f'{whole}{d_sep}{num % 100:02}'

    def fmt_cur(self, locale: str, currency: str) -> str:
        """Format the currency change."""
        symbol = SYMBOL[currency]
        fmt = FMT['currency'][(locale, self.change >= 0)]
        return fmt.format(symbol=symbol, num=self.fmt_decimal(locale, abs(self.change)))

    def format(self, locale: str, currency: str) -> str:
        """Format an entry."""
        # Format the date.
        date_fmt = FMT['date'][locale]
        date_str = self.date.strftime(date_fmt)

        # Truncate the description.
        if len(self.description) > 25:
            description = self.description[:22] + '...'
        else:
            description = self.description

        # Format the change.
        change_str = self.fmt_cur(locale, currency)

        # Combine columns.
        return f'{date_str:<10} | {description:<25} | {change_str:>13}'


def create_entry(date: str, description: str, change: int) -> LedgerEntry:
    """Return a LedgerEntry."""
    pdate = datetime.datetime.strptime(date, '%Y-%m-%d')
    return LedgerEntry(pdate, description, change)


def format_entries(currency: str, locale: str, entries: list[LedgerEntry]) -> str:
    """Format LedgerEntry values."""
    parts = FMT['headers'][locale]
    header = f'{parts[0]:<10} | {parts[1]:<25} | {parts[2]:<13}'
    rows = [header] + [entry.format(locale, currency) for entry in sorted(entries)]
    return '\n'.join(rows)
