from enum import Enum
import random
from typing import Tuple


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    @classmethod
    def calculate_endpoint(
        cls, starting_point: Tuple[int, int], length, direction: "Direction" = None
    ) -> Tuple[int, int]:
        if not direction and length > 1:
            raise ValueError("If length > 1, must have direction: Length passed: %d" % length)
        if length == 1:
            direction = None
        if not direction:
            return starting_point
        if direction == cls.NORTH:
            return (starting_point[0], starting_point[1] - length)
        if direction == cls.EAST:
            return (starting_point[0] + length, starting_point[1])
        if direction == cls.SOUTH:
            return (starting_point[0], starting_point[1] + length)
        if direction == cls.WEST:
            return (starting_point[0] - length, starting_point[1])

    @classmethod
    def out_of_bounds(cls, starting_point, length, outter_limit, direction: "Direction" = None) -> bool:
        if not direction and length > 1:
            raise ValueError("If length > 1, must have direction: Length passed: %d" % length)
        if not direction:
            return not (0 <= starting_point[0] < outter_limit[0] and 0 <= starting_point[1] < outter_limit[1])
        end_point = cls.calculate_endpoint(starting_point, length, direction)
        return (not (0 <= starting_point[0] < outter_limit[0] and 0 <= starting_point[1] < outter_limit[1])) or not (
            0 <= end_point[0] < outter_limit[0] and 0 <= end_point[1] < outter_limit[1]
        )

    @classmethod
    def generate_random(cls):
        return random.choice(list(cls))
