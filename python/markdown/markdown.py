import re
import enum


class Tag(enum.Enum):
    """Represents various tags that can wrap text."""
    LIST = 'ul'
    BULLET = 'li'
    PARAGRAPH = 'p'
    EMPHASIS = 'em'
    STRONG = 'strong'
    HEADER1 = 'h1'
    HEADER2 = 'h2'
    HEADER3 = 'h3'
    HEADER4 = 'h4'
    HEADER5 = 'h5'
    HEADER6 = 'h6'
    HEADER7 = 'h7'


# Indexed headers, index matching header number.
HEADERS = (None, Tag.HEADER1, Tag.HEADER2, Tag.HEADER3, Tag.HEADER4, Tag.HEADER5, Tag.HEADER6, Tag.HEADER7)
# Midline wraps, sorted by processing order.
MIDLINE_WRAP = (('__', Tag.STRONG), ('_', Tag.EMPHASIS))


def _Wrap(line, tag):
    """Wrap text in a tag."""
    return f'<{tag.value}>{line}</{tag.value}>'


def _ParseMidLineWraps(line: str) -> str:
    """Parse all mid-line text wrappers.

    Transforms e.g. '__a__' into '<strong>a</strong>'.
    Operates on a whole line, looping until no more wraps found.
    """
    for md, token in MIDLINE_WRAP:
        pattern = f'(.*){md}(.*){md}(.*)'
        replace = f'\\1<{token.value}>\\2</{token.value}>\\3'
        line = re.sub(pattern, replace, line)
    return line


def _LineWrapper(line):
    # Default line wrapper, if none others found.
    line_wrap = Tag.PARAGRAPH
    # Determine how to wrap this line.
    if line.startswith('#'):
        header, line = line.split(' ', 1)
        line_wrap = HEADERS[len(header)]
    elif line.startswith('*'):
        line_wrap = Tag.BULLET
        line = line.split(' ', 1)[1]
    return line, line_wrap


def _HandleList(line, in_list):
    tags = []
    if in_list and not line.startswith('*'):
        in_list = False
        tags.append('</ul>')
    elif line.startswith('*'):
        if not in_list:
            tags.append('<ul>')
        in_list = True
    return tags, in_list


def parse(markdown):
    lines = markdown.split('\n')
    res = []
    in_list = False
    for line in lines:
        # Close out a list if needed.
        tags, in_list = _HandleList(line, in_list)
        res.extend(tags)
        # Parse line-wrapping leading symbols.
        line, line_wrap = _LineWrapper(line)
        # Parse the line's contents.
        line = _ParseMidLineWraps(line)
        # Wrap the line.
        res.append(_Wrap(line, line_wrap))

    # Close out any list we may be in.
    if in_list:
        res.append('</ul>')
    return ''.join(res)


# vim:ts=4:sw=4:expandtab
