"""Functions to help the company calculate their power usage."""


def get_extra_hours(hours: int) -> int:
    """Return the amount of hours."""
    return (hours + 3) % 24


def get_kW_amount(watts: int) -> float:
    """Return the kW value of a given watt value."""
    return round(watts / 1000, 1)


def get_kwh_amount(watts: int) -> int:
    """Return the kWh value of a given watt value and hours."""
    return int(get_kW_amount(watts) / 60 / 60)


def get_efficiency(power_factor: int) -> float:
    """Return the efficiency calculated from the power factor."""
    return power_factor / 100


def get_cost(watts: int, power_factor: int, price: float) -> float:
    """Calculate the cost of a given kWh value, efficiency and price."""
    return price * get_kwh_amount(watts) / get_efficiency(power_factor)
