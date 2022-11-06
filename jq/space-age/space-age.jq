def two_decimal: (. * 100) | round / 100;
def ratios:
  {
    "Mercury": 0.2408467,
    "Venus": 0.61519726,
    "Earth": 1.0,
    "Mars": 1.8808158,
    "Jupiter": 11.862615,
    "Saturn": 29.447498,
    "Uranus": 84.016846,
    "Neptune": 164.79132
  }
  ;

.
| if (.planet | in(ratios)) then . else ("not a planet\n" | halt_error) end
| (60 * 60 * 24 * 365.25) as $earth_year
| .seconds / $earth_year / ratios[.planet]
| two_decimal
