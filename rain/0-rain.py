#!/usr/bin/python3
"""rain function."""


def rain(walls):
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water_retained = 0

    while left < right:
        if walls[left] <= walls[right]:
            left_max = max(left_max, walls[left])
            water_retained += left_max - walls[left]
            left += 1
        else:
            right_max = max(right_max, walls[right])
            water_retained += right_max - walls[right]
            right -= 1

    return water_retained
