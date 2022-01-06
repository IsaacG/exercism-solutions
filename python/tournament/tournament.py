"""Generate scoreboard for a tournament."""

import collections
import dataclasses


@dataclasses.dataclass
class TeamScore:
    """Stats for one team."""
    wins: int = 0
    losses: int = 0
    draws: int = 0

    @property
    def played(self) -> int:
        """Return the total games played for this team."""
        return self.wins + self.losses + self.draws

    @property
    def points(self) -> int:
        """Return the total points for this team."""
        return 3 * self.wins + self.draws

    def format(self, name: str) -> str:
        """Format the team stats for the scoreboard."""
        return (
            f"{name:<30} | {self.played:2} | {self.wins:2} | {self.draws:2} |"
            + f" {self.losses:2} | {self.points:2}"
        )


def tally(rows: list[str]) -> list[str]:
    """Tally scores for teams."""
    teams: dict[str, TeamScore] = collections.defaultdict(TeamScore)
    for row in rows:
        fields = row.split(";")
        if len(fields) != 3:
            raise ValueError("Poorly formed input")
        team_a, team_b, result = fields
        if result == "draw":
            teams[team_a].draws += 1
            teams[team_b].draws += 1
        elif result == "win":
            teams[team_a].wins += 1
            teams[team_b].losses += 1
        elif result == "loss":
            teams[team_a].losses += 1
            teams[team_b].wins += 1
        else:
            raise ValueError("Poorly formed input")

    table = [f"{'Team':<30} | MP |  W |  D |  L |  P"]
    # https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts
    # Sort first by name then by points. Sort stability will give us points-then-names.
    team_names = sorted(teams)
    team_names = sorted(team_names, key=lambda t: teams[t].points, reverse=True)
    for team_name in team_names:
        table.append(teams[team_name].format(team_name))
    return table
