EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(time_in_the_oven):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time_in_the_oven


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time for a given number of layers.

    :param number_of_layers: int - how many layers the lasagna has.
    :return: int - total preparation time.

    Function that takes the number of layers in the lasagna and returns the preparation time.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time that elapsed, including the preparation time and baking time.

    :param number_of_layers: int - how many layers are in the lasagna.
    :param elapsed_bake_time: int - how many minutes the lasagna has already been baking.
    :return: int - total elapsed time between the preparation and baking.

    Function that takes how many layers are in the lasagna how how long it is in the oven.
    The function returns the total time that has elapsed.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
