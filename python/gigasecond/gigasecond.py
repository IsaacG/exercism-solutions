import datetime

GIGASECOND = datetime.timedelta(seconds=int(1e9))


def add(moment):
    return moment + GIGASECOND
