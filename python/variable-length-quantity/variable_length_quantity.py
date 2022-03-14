"""Variable length encoding."""

import itertools

# Bit indicating there are more chunks to this number.
MORE = 0b10000000
# Mask used to access the number part of this chunk.
MASK = 0b01111111


def encode_one(number: int) -> list[int]:
    """Encode one number."""
    encoded: list[int] = []
    while number or not encoded:
        # Set the MORE bit on all chunks.
        encoded.append(MORE | (number & MASK))
        number >>= 7
    # Unset MORE on the last chunk.
    encoded[0] &= MASK
    return list(reversed(encoded))


def encode(numbers: list[int]) -> list[int]:
    """Encode numbers."""
    return list(itertools.chain.from_iterable(encode_one(number) for number in numbers))


def decode(encoded: list[int]) -> list[int]:
    """Decode numbers."""
    if encoded[-1] & MORE:
        raise ValueError("incomplete sequence")

    decoded: list[int] = []
    num = 0
    for chunk in encoded:
        num = (num << 7) | (chunk & MASK)
        if not chunk & MORE:
            decoded.append(num)
            num = 0
    return decoded
