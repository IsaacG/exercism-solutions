"""Implements Rail Fence Cipher."""

import math


def encode(message: str, rails: int) -> str:
    """Encode a message using the rail fence cipher.

    Note for N rails, the message is broken up into blocks of 2*(N-1).
    Message "123456789" on 3 rails:
    1...5...9
    .2.4.6.8.
    ..3...7..

    Observe N-1 (2) down, N-1 up and then the pattern repeats itself.
    This allows us to chunk the message into blocks of 2*(N-1) (in this example, 4).

    Observe the top and bottom rails are different from the middle rails. The top and
    bottom rails are used once per block. The middle rails are used twice per block.

    For the top rail, we use chars at positions (i * block size), e.g. [0, 4, 8].
    Similarly, the bottom rail uses chars at positions
    (i * block size) + (rails - 1), e.g. [2, 6].

    The middle rails are similar in that they use `(i * block size) + rails` for the
    first character. The second character is at `(i + 1) * block size - rails`.

    Using these observations, we can build the output one rail at a time directly
    from the input.
    """
    block_size = rails * 2 - 2
    lines: list[str] = []
    for rail in range(rails):
        line = []
        for block in range(len(message) // block_size + 1):
            # The first character per block.
            offset = block * block_size + rail
            if offset < len(message):
                line.append(message[offset])
            # The second character for middle rails.
            offset = (block + 1) * block_size - rail
            if 0 < rail < rails - 1 and offset < len(message):
                line.append(message[offset])
        lines.extend("".join(line))
    return "".join(lines)


def decode(message: str, rails: int) -> str:
    """Decode a fence rail encoded message.

    Based on the above observations, it would follow that decoding should have
    a similar pattern to encoding, where messages can be broken into chunks
    of length (rails - 1) * 2. If we take an input and encode it then map the
    offset of the input characters (broken into lines of length `(rails - 1) * 2`,
    a pattern emerges.

    Offsets for a 4-rail 18 char message.
    rail    1  2  3    4  3  2
            ------------------
    offsets 0  3  9   15 10  4
            1  5 11   16 12  6
            2  7 13   17 14  8
            ------------------
    step    1  2  2    1  2  2

    Note how characters are laid out in a cyclic pattern. We can compute the offset
    pattern and use the offsets to decode the message.
    """
    offsets = {}
    block_size = 2 * (rails - 1)
    mlen = len(message)
    current = 0
    for rail in range(rails):
        if 0 < rail < rails - 1:
            step = 2
        else:
            step = 1
        row_len = math.ceil((mlen - rail) / block_size)
        offsets[rail] = list(range(current, current + step * row_len, step))
        max_val = offsets[rail][-1]
        if 0 < rail < rails - 1:
            alt_rail = block_size - rail
            row_len = math.ceil((mlen - alt_rail) / block_size)
            offsets[alt_rail] = list(range(current + 1, current + 1 + step * row_len, step))
            max_val = max(max_val, offsets[alt_rail][-1])
        current = max_val + 1
    # Sort by rail number, transpose and chain into a combined/flattened list.
    combined_offsets = [
        offsets[rail][x]
        for x in range(len(offsets[0]))
        for rail in range(block_size)
        if x < len(offsets[rail])
    ]
    # Use offsets to decode the message.
    return "".join(message[i] for i in combined_offsets)
