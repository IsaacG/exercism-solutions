ONES = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six',
    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'ninteen',
]
TENS = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
    'seventy', 'eighty', 'ninety']
BASES = (
    (1e9, 'billion'),
    (1e6, 'million'),
    (1e3, 'thousand'),
    (1e2, 'hundred'),
)


def say(num):
    parts = []
    if not 0 <= num < 1e12:
        raise ValueError('input out of range')

    if num == 0:
        return ONES[num]

    for base, name in BASES:
        if num >= base:
            parts.append(say(int(num // base)))
            parts.append(name)
            num = int(num % base)

    out = ''
    if num >= 20:
        out += TENS[num // 10]
        num = int(num % 10)
        if num:
            out += '-'
    if num and num < 20:
        out += ONES[num]
    if out:
        parts.append(out)

    return ' '.join(parts)

# vim:ts=4:sw=4:expandtab
