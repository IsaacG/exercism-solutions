import functools


EARTH_SECONDS = 60 * 60 * 24 * 365.25
PLANET_RATIOS = {
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'earth': 1.0,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132
}


class SpaceAge(object):

    def __init__(self, seconds):
        self.seconds = seconds

    @property
    def years(self):
        return self.seconds / 31557600

    def __getattr__(self, n):
        assert n.startswith("on_"), n
        planet = n.removeprefix("on_")
        result = round(self.seconds / (EARTH_SECONDS * PLANET_RATIOS[planet]), 2) 
        return lambda: result

