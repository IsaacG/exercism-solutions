"""Tuples exercise."""

def get_coordinate(record: tuple[str, tuple[str, str]]) -> str:
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return "".join(i for i in record[1])


def convert_coordinate(coordinate):
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """
    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """
    return convert_coordinate(azara_record[1]) == rui_record[1]


def create_record(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: tuple of tuples - everything "cleaned". Excess coordinates and information removed.
    """
    data = [(d[0],) + (d[2:]) for d in combined_record_group]
    out = "\n".join("(" + ", ".join(repr(i) for i in d) + ")" for d in data)
    return out + "\n"


def clean_up(combined_record_group):
    report = []
    for records in combined_record_group:
        record = list(records)
        del record[1]
        report.append(record)
    return """ """.join(str(report))

