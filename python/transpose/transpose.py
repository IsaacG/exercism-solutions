def transpose(lines: str) -> str:
    if not lines:
        return ""
    rows = lines.splitlines()
    width = max(len(r) for r in rows)
    rows = [r.ljust(width) for r in rows]
    return "\n".join("".join(rows[y][x] for y in range(len(rows))) for x in range(len(rows[0])))
