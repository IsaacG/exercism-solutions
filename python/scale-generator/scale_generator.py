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

        start = [s.upper() for s in scale].index(self.tonic.upper())
        return [scale[(start + i) % len(scale)] for i in range(len(scale))]

    def interval(self, intervals: str) -> list[str]:
        """Return an interval."""
        chromatic = self.chromatic()
        cur = 0
        out = []
        for i in intervals:
            out.append(chromatic[cur])
            cur += STEPS[i]
        return out
