"""Crypto Square."""

import math
import string
import textwrap

ALNUM = string.ascii_lowercase + string.digits

def cipher_text(plain_text: str) -> str:
    """Encode using a Crypto Square."""
    # Remove non-alphanum chars.
    text = "".join(c for c in plain_text.lower() if c in ALNUM)

    # Calculate block size.
    cols = math.ceil(math.sqrt(len(text))) or 1
    rows = cols - 1
    if cols * rows < len(text):
        rows = cols

    # Space pad as needed.
    text = text.ljust(cols * rows)
    # Transpose the block.
    out = "".join(text[col + row * cols] for col in range(cols) for row in range(rows))
    # Chunk the result.
    return " ".join(textwrap.wrap(out, rows or 1, drop_whitespace=False))
