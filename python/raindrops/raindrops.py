def convert(number):
  sounds = [(3, 'Pling'), (5, 'Plang'),  (7, 'Plong')]
  return ''.join(s for f, s in sounds if number % f == 0) or str(number)

def convert(number):
    factors = {3 * 5 * 7: "PlingPlangPlong", 5 * 7: "PlangPlong", 3 * 7: "PlingPlong", 3 * 5: "PlingPlang", 7: "Plong", 5: "Plang", 3: "Pling"}
    return next((sound for factor, sound in factors.items() if not number % factor), str(number))


# vim:ts=2:sw=2:expandtab
