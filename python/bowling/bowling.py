"""Score a bowling card."""
from __future__ import annotations


class Frame:
    """One frame of a game."""

    next_frame: Frame

    def __init__(self, frame: int):
        """Initialize."""
        self.rolls: list[int] = []
        self.frame = frame

    @property
    def is_open_frame(self) -> bool:
        """Return if this frame is open."""
        return sum(self.rolls) < 10

    @property
    def is_spare(self) -> bool:
        """Return if this frame contains a spare."""
        return self.rolls[0] != 10 and sum(self.rolls[:2]) == 10

    @property
    def is_strike(self) -> bool:
        """Return if this frame contains a strike."""
        return 10 in self.rolls

    def roll(self, pins: int) -> None:
        """Validate and track a roll."""
        if self.frame > 10:
            raise ValueError("game is over")
        if not 0 <= pins <= 10:
            raise ValueError(f"invalid pin value, {pins}")

        if pins == 10 and self.rolls:
            # Strike is only possible on the first roll of a frame
            # ... or on frame 10 (following a strike/spare).
            assert self.frame == 10 and sum(self.rolls) >= 10, "invalid pin value"

        # Combined pins on the second* roll cannot exceed 10.
        # On frame 10, unless following a spare/strike, combined pins cannot exceed 10.
        if self.rolls:
            if self.frame != 10:
                assert sum(self.rolls) + pins <= 10, "invalid pin value"
            elif self.rolls[-1] != 10 and not self.is_spare:
                assert self.rolls[-1] + pins <= 10, "invalid pin value"

        self.rolls.append(pins)

    def full(self) -> bool:
        """Return if this frame is "full" or complete."""
        # Normally, a frame is over on the second ball or a strike.
        if self.frame < 10:
            return self.is_strike or len(self.rolls) == 2

        # On the last frame, you get a third roll when you have a spare/strike.
        if self.is_spare or self.is_strike:
            return len(self.rolls) == 3
        return len(self.rolls) == 2

    def get_next(self) -> Frame:
        """Return a new next frame."""
        self.next_frame = Frame(self.frame + 1)
        return self.next_frame

    def next_two_rolls(self) -> list[int]:
        """Return the next two rolls after this frame."""
        rolls = self.next_frame.rolls[:2]
        if len(rolls) == 1:
            rolls.append(self.next_frame.next_frame.rolls[0])
        return rolls

    def score(self) -> int:
        """Return the score of a frame."""
        if self.is_open_frame:
            return sum(self.rolls)
        if self.is_spare:
            return sum(self.rolls + self.next_two_rolls()[:1])
        if self.is_strike:
            return sum(self.rolls + self.next_two_rolls()[:2])
        raise RuntimeError("Invalid frame")

    def __str__(self) -> str:
        """Return a string reresentation of a frame."""
        return f"{self.frame}{self.rolls}"


class BowlingGame:
    """Bowling score."""

    def __init__(self):
        """Initialize."""
        self.rolls: list[int] = []
        self.current_frame = Frame(1)
        self.frames: list[Frame] = [self.current_frame]

    def roll(self, pins: int) -> None:
        """Validate and track a roll."""
        self.current_frame.roll(pins)
        if self.current_frame.full():
            self.current_frame = self.current_frame.get_next()
            self.frames.append(self.current_frame)

    def score(self) -> int:
        """Score a game."""
        assert self.current_frame.frame == 11, "game not over"
        return sum(f.score() for f in self.frames)
