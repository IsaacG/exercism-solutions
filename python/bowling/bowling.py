"""Score a bowling card."""
import itertools


class BowlingGame:
    """Bowling score."""
    def __init__(self):
        """Initialize."""
        self._rolls: list[int] = []
        self._frame = 1
        self._ball = 0

    def end_frame(self) -> None:
        """End a frame."""
        self._ball = 0
        self._frame += 1

    def roll(self, pins: int) -> None:
        """Validate and track a roll."""
        # Simple checks: pin is possible, game is not over.
        assert 0 <= pins <= 10, "invalid pin value"
        assert self._frame <= 10, "game is over"

        if pins == 10 and self._ball != 0:
            # Strike is only possible on the first roll of a frame
            # ... or on frame 10 (following a strike/spare).
            assert self._frame == 10
            assert sum(self._rolls[-self._ball:]) >= 10, "invalid pin value"

        # Combined pins on the second* roll cannot exceed 10.
        # On frame 10, unless following a spare/strike, combined pins cannot exceed 10.
        if self._ball > 0:
            if self._frame != 10:
                assert self._rolls[-1] + pins <= 10, "invalid pin value"
            else:
                if self._rolls[-1] != 10 and sum(self._rolls[-self._ball:]) != 10:
                    assert self._rolls[-1] + pins <= 10, "invalid pin value"

        self._rolls.append(pins)
        self._ball += 1

        if self._frame == 10:
            if self._ball == 1:
                pass
            elif self._ball == 2:
                if 10 not in self._rolls[-2:] and sum(self._rolls[-2:]) != 10:
                    self.end_frame()
            elif self._ball == 3:
                self.end_frame()
        elif self._ball == 2 or pins == 10:
            self.end_frame()

    def score(self) -> int:
        """Score a game."""
        assert self._frame == 11, "game not over"
        score = 0
        rolls = itertools.zip_longest(*[self._rolls[i:] for i in range(3)])
        for _ in range(1, 11):
            pins = next(rolls)
            if pins[0] == 10:
                # Strike
                score += sum(pins)
            else:
                # Spare
                if sum(pins[:2]) == 10:
                    score += sum(pins)
                else:
                    score += sum(pins[:2])
                next(rolls)
        return score
