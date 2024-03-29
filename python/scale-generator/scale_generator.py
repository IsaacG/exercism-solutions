"""Music scale generator."""
NO_SHARPS_NOR_FLATS = {"C major", "a minor"}
USE_SHARPS = {"G", "D", "A", "E", "B", "F# major e", "b", "f#", "c#", "g#", "d# minor"}
USE_FLATS = {"F", "Bb", "Eb", "Ab", "Db", "Gb major", "d", "g", "c", "f", "bb", "eb minor"}
SCALE = [
    ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"],  # Sharps
    ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"],  # Flats
]
STEPS = {"m": 1, "M": 2, "A": 3}


class Scale:
    """Scale stuff."""
    def __init__(self, tonic: str):
        self.tonic = tonic

    def chromatic(self) -> list[str]:
        """Return a chromatic."""
        if self.tonic in USE_SHARPS or self.tonic in "aC":
            scale = SCALE[0]
        else:
            scale = SCALE[1]

        start = scale.index(self.tonic.capitalize())
        return scale[start:] + scale[:start]

    def interval(self, intervals: str) -> list[str]:
        """Return an interval."""
        # Compute the steps. See also itertools.accumulate.
        steps = [0]
        for i in intervals:
            steps.append(steps[-1] + STEPS[i])

        # Use the steps to pull the notes out of the chromatic.
        chromatic = self.chromatic()
        out = [chromatic[step] for step in steps[:-1]]
        # Repeat the first note to close the loop.
        out.append(out[0])
        return out
