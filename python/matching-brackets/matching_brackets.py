def is_paired(input_string):
    unmatched = []
    matching = {")": "(", "]": "[", "}": "{"}
    for character in input_string:
        if character in matching.values():
            unmatched.append(character)
        if character in matching:
            if not unmatched:
                return False
            if unmatched[-1] == matching[character]:
                unmatched.pop()
            else:
                return False
    return not unmatched
