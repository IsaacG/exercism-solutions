import collections
import dataclasses

@dataclasses.dataclass
class TeamScore:
  wins: int = 0
  losses: int = 0
  draws: int = 0

  @property
  def played(self):
    return self.wins + self.losses + self.draws

  @property
  def points(self):
    return 3 * self.wins + self.draws


class Tournament:
  def __init__(self, teams):
    self._teams = teams

  @classmethod
  def from_rows(cls, rows):
    teams = collections.defaultdict(TeamScore)
    for row in rows:
      fields = row.split(';')
      if len(fields) != 3:
        raise ValueError('Poorly formed input')
      team_a, team_b, result = fields
      if result == 'draw':
        teams[team_a].draws += 1
        teams[team_b].draws += 1
        continue
      elif result == 'win':
        teams[team_a].wins += 1
        teams[team_b].losses += 1
      elif result == 'loss':
        teams[team_a].losses += 1
        teams[team_b].wins += 1
      else:
        raise ValueError('Poorly formed input')

    return cls(teams)

  def format(self):
    teams = self._teams
    template = '%-30s | %2d | %2d | %2d | %2d | %2d'
    table = ['Team                           | MP |  W |  D |  L |  P']
    # https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts
    # Sort first by name then by points. Sort stability will give us points-then-names.
    team_names = sorted(teams)
    team_names = sorted(team_names, key=lambda t: teams[t].points, reverse=True)
    for team_name in team_names:
      team = teams[team_name]
      table.append(
        template % (
          team_name, team.played, team.wins,
          team.draws, team.losses, team.points))
    return table


def tally(rows):
  return Tournament.from_rows(rows).format()



# vim:ts=2:sw=2:expandtab
