#!/usr/bin/python3
"""Implement pseudo-grep in Python."""

import collections


def _find_matches(
    pattern: str,
    opts: dict[str, bool],
    files: list[str]
) -> dict[str, list[tuple[int, str]]]:
    """Return details about matching lines in files."""
    matches = collections.defaultdict(list)
    if opts["i"]:
        pattern = pattern.casefold()
    for file in files:
        with open(file, "rt", encoding="utf-8") as handle:
            for num, line in enumerate(handle):
                # Remove just a single trailing newline and no more.
                line = line.removesuffix("\n")
                # Optionally ignore case on the line.
                if opts["i"]:
                    cased_line = line.casefold()
                else:
                    cased_line = line
                # Check if the line matches - either partial or full.
                if opts["x"]:
                    match = pattern == cased_line
                else:
                    match = pattern in cased_line
                # Check if we want match vs non-match.
                if match != opts["v"]:
                    matches[file].append((num, line))
                    # If we only want othe filename, stop after one match.
                    # This is an optimization to avoid processing the rest of
                    # the file when it won't be used.
                    if opts["l"]:
                        break
    return dict(matches)


def _format_output(
    matches: dict[str, list[tuple[int, str]]],
    opts: dict[str, bool],
    multi_files: bool,
) -> list[str]:
    """Format output of matches based on options."""
    results = []
    for file in matches:
        # With -l, just print the filename(s).
        if opts["l"]:
            results.append(file)
        else:
            for num, line in matches[file]:
                # Add line numbers for -n.
                if opts["n"]:
                    line = f"{num + 1}:{line}"
                # Add filenames on multi-files.
                if multi_files:
                    line = f"{file}:{line}"
                results.append(line)
    return results


def grep(pattern: str, flags: str, files: list[str]) -> str:
    """Search files for patterns."""
    # Build a dict of options (bools).
    opts = {
        f.removeprefix("-"): f in flags.split()
        for f in ("-n", "-l", "-i", "-v", "-x")
    }
    matches = _find_matches(pattern, opts, files)
    results = _format_output(matches, opts, len(files) > 1)
    return "".join(l + "\n" for l in results)
