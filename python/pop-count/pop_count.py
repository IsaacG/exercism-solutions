def egg_count(display_value: int) -> int:
    # Built in function: return display_value.bit_count()
    count = 0
    while display_value:
        if display_value & 1:
            count += 1
        display_value >>= 1
    return count
