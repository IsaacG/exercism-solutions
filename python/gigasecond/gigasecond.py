import datetime


def add(moment):
    return datetime.datetime.fromtimestamp(int(moment.timestamp() + 1e9))
