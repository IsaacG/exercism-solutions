import calendar
import datetime


class MeetupDayException(Exception):
  pass


OFFSET = {'first': 1, 'second': 8, 'third': 15, 'fourth': 22, 'fifth': 29, 'teenth': 13}


def meetup(year, month, week, day_of_week):
  
  t_month = month
  if week in OFFSET:
    try:
      d = datetime.date(year, month, OFFSET[week])
    except ValueError:
      raise MeetupDayException('That day does not exist.')
  elif week == 'last':
    t_month += 1
    if t_month > 12:
      year += t_month // 12
      t_month %= 12
    d = datetime.date(year, t_month, 1) - datetime.timedelta(7)
  else:
    raise ValueError(f"unknown week {week}")

  day_of_week = list(calendar.day_name).index(day_of_week)
  dow_shift = datetime.timedelta((day_of_week - d.weekday()) % 7)
  result = d + dow_shift
  if result.month != month:
    raise MeetupDayException('That day does not exist.')
  return result


# vim:ts=2:sw=2:expandtab
