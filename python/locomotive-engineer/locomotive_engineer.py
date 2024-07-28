"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons: int) -> list[int]:
    """Return a list of wagons."""
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons."""
    head, tail = each_wagons_id[:2], each_wagons_id[3:]
    return [1] + missing_wagons + tail + head


def add_missing_stops(
    route: dict[str, str | list[str]],
    **stops: str,
) -> dict[str, str | list[str]]:
    """Add missing stops to route dict."""
    route["stops"] = list(stops.values())
    return route


def extend_route_information(
    route: dict[str, str],
    more_route_information: dict[str, str],
) -> dict[str, str]:
    """Extend route information with more_route_information."""
    return route | more_route_information


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[tuple] - the list of rows of wagons.
    :return: list[tuple] - list of rows of wagons.
    """
    return [list(i) for i in zip(*wagons_rows)]
