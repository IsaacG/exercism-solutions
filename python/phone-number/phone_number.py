"""Phone number handler."""


class Phone:
    """Phone number validator."""

    def __init__(self, num: str):
        """Load and clean a number, validating it."""
        # Ignore all non-digits.
        digits = ''.join(i for i in num if i.isdigit())

        # For an 11-digit with country code, drop the country code.
        if len(digits) == 11 and digits.startswith('1'):
            digits = digits[1:]
        self.number = digits
        self.validate()

    def validate(self) -> None:
        """Validate the number."""
        if len(self.number) != 10:
            raise ValueError('Invalid number')

        for invalid in ('0', '1'):
            for check in (self.area_code, self.exchange):
                if check.startswith(invalid):
                    raise ValueError('Invalid number')

    @property
    def area_code(self) -> str:
        """Return the area code (leading 3 digits)."""
        return self.number[0:3]

    @property
    def exchange(self) -> str:
        """Return the exchange (3 digits after the area code)."""
        return self.number[3:6]

    @property
    def subscriber(self) -> str:
        """Return the subscriber (final 4 digits)."""
        return self.number[6:10]

    def pretty(self) -> str:
        """Return a pretty string of the number."""
        return f'({self.area_code}) {self.exchange}-{self.subscriber}'
