"""Bottle Song."""
NUMBERS = "No One Two Three Four Five Six Seven Eight Nine Ten".split()


def bottles(num: int) -> str:
    """Return the bottle term."""
    out = f"{NUMBERS[num]} green bottle"
    if num != 1:
        out += "s"
    return out


def recite(start: int, take: int = 1) -> list[str]:
    """Return verses."""
    out = []
    for i in range(start, start - take, -1):
        out.append(f"{bottles(i)} hanging on the wall,")
        out.append(f"{bottles(i)} hanging on the wall,")
        out.append("And if one green bottle should accidentally fall,")
        out.append(f"There'll be {bottles(i - 1).lower()} hanging on the wall.")
        out.append("")
    return out[:-1]
