"""Variable length encoding."""

# Bit indicating there are more chunks to this number.
MORE = 0b10000000
# Mask used to access the number part of this chunk.
MASK = 0b01111111


def encode(numbers: list[int]) -> list[int]:
    """Encode numbers."""
    results = []
    for number in numbers:
        encoded: list[int] = []
        while number:
            # Set the MORE bit on all chunks.
            encoded.append(MORE | (number & MASK))
            number >>= 7
        if not encoded:
            encoded.append(0)
        # Unset MORE on the last chunk.
        encoded[0] &= MASK
        results.extend(reversed(encoded))
    return results


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
