def is_paired(input_string):
    unmatched_context = []
    matching = {")": "(", "]": "[", "}": "{"}
    for character in input_string:
        if character in matching.values():
            unmatched_context.append(character)
        if character in matching:
            if not unmatched_context:
                return False
            if unmatched_context[-1] == matching[character]:
                unmatched_context.pop()
            else:
                return False
    return not unmatched_context
