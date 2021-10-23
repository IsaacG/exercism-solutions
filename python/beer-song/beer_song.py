"""Beer song."""

def bottles(num: int) -> str:
    """Return {num} bottles."""
    if num > 1:
        return f"{num} bottles"
    if num == 1:
        return "1 bottle"
    return "No more bottles"


def verse(num: int) -> list[str]:
    """Return one verse."""
    out = [f"{bottles(num)} of beer on the wall, {bottles(num).lower()} of beer."]
    if num > 1:
        out.append(f"Take one down and pass it around, {bottles(num - 1)} of beer on the wall.")
    elif num == 1:
        out.append("Take it down and pass it around, no more bottles of beer on the wall.")
    elif num == 0:
        out.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return out + [""]


def recite(start: int, take: int = 1) -> list[str]:
    """Return song verses."""
    return [v for i in range(start, start - take, -1) for v in verse(i)][:-1]
