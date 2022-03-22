from functools import reduce
from logging import getLogger

logger = getLogger()


def rainfall(height_list: list[int]) -> int:
    """
    Calculate the total rainfall for a list of heights
    :param height_list: list of heights
    :return: total rainfall
    """
    # Let us setup arrays for highest seen peaks from left and right
    left = [0] * len(height_list)
    right = [0] * len(height_list)

    # Now let's fill these arrays with the highest value left of every point
    # moving from left to right
    left[0] = height_list[0]  # At the zeroth point looking left
    # Start at 1 since I have already determined height of first left elem
    for i in range(1, len(height_list)):
        heighest_left_of = left[i - 1]
        current_height = height_list[i]
        left[i] = max(heighest_left_of, current_height)

    # Now let's fill these arrays with the highest value right of every point
    # moving from right to left
    right[len(right) - 1] = height_list[len(right) - 1]
    for i in range(len(height_list) - 2, -1, -1):
        heighest_right_of = right[i + 1]
        current_height = height_list[i]
        right[i] = max(heighest_right_of, current_height)

    # Now I'm ready to calculate rain fall at every point in our map
    return reduce(
        lambda accum, height_elem: accum
        + (min(right[height_elem[0]], left[height_elem[0]]) - height_elem[1]),
        enumerate(height_list),
        0,
    )
