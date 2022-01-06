import string


class PhoneNumber:
    """Phone number validator."""

    def __init__(self, number: str):
        """Load and clean a number, validating it."""
        # Raise exceptions for invalid characters.
        for char in string.ascii_letters:
            if char in number:
                raise ValueError('letters not permitted')

        invalid_chars = set(string.punctuation) - set('+-().')
        for char in invalid_chars:
            if char in number:
                raise ValueError('punctuations not permitted')

        # Drop all non-digits.
        digits = ''.join(i for i in number if i.isdigit())

        if len(digits) > 11:
            raise ValueError('more than 11 digits')

        if len(digits) == 11:
            if not digits.startswith('1'):
                raise ValueError('11 digits must start with 1')
            # For an 11-digit with country code, drop the country code.
            digits = digits[1:]

        if len(digits) != 10:
            raise ValueError('incorrect number of digits')

        self.number = digits
        self.area_code = digits[0:3]
        self.exchange = digits[3:6]
        self.subscriber = digits[6:10]

        for invalid_char, char_name in (('0', 'zero'),  ('1', 'one')):
            for part, part_name in (
                (self.area_code, 'area code'), (self.exchange, 'exchange code')
            ):
                if part.startswith(invalid_char):
                    raise ValueError(f'{part_name} cannot start with {char_name}')

    def pretty(self) -> str:
        """Return a pretty string of the number."""
        return f'({self.area_code})-{self.exchange}-{self.subscriber}'
