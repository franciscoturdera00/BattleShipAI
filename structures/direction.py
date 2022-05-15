from enum import Enum
import random
from typing import Tuple

from util.util import calculate_grid_distance


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    @classmethod
    def calculate_endpoint(cls, starting_point: Tuple[int, int], length, direction: "Direction") -> Tuple[int, int]:
        if length < 1:
            raise ValueError("Length must be > 0: Length passed: %d" % length)
        if not direction:
            raise ValueError("Must pass a direction")
        if direction == cls.NORTH:
            return (starting_point[0], starting_point[1] - (length - 1))
        if direction == cls.EAST:
            return (starting_point[0] + (length - 1), starting_point[1])
        if direction == cls.SOUTH:
            return (starting_point[0], starting_point[1] + (length - 1))
        if direction == cls.WEST:
            return (starting_point[0] - (length - 1), starting_point[1])

    @classmethod
    def out_of_bounds(cls, starting_point, length, outter_limit, direction: "Direction") -> bool:
        end_point = cls.calculate_endpoint(starting_point, length, direction)
        return (not (0 <= starting_point[0] < outter_limit[0] and 0 <= starting_point[1] < outter_limit[1])) or not (
            0 <= end_point[0] < outter_limit[0] and 0 <= end_point[1] < outter_limit[1]
        )

    @classmethod
    def generate_random(cls):
        return random.choice(list(cls))

    @classmethod
    def calculate_direction(cls, start: Tuple[int, int], end: Tuple[int, int]):
        """
        Calculates the direction just taken.
        Expects coordiantes within one grid distance from each other
        """
        dist = calculate_grid_distance(start, end)
        if dist != 1:
            raise ValueError("Expecting grid distance = 1. Distance between %s and %s: %d" % (start, end, dist))
        if dist == 0:
            return None
        if start[0] != end[0]:
            if start[0] > end[0]:
                return cls.WEST
            else:
                return cls.EAST
        elif start[1] > end[1]:
            return cls.NORTH
        return cls.SOUTH

    def opposite(self):
        if self.name == "NORTH":
            return Direction.SOUTH
        if self.name == "SOUTH":
            return Direction.NORTH
        if self.name == "EAST":
            return Direction.WEST
        if self.name == "WEST":
            return Direction.EAST

    @classmethod
    def calculate_start_of_chain(cls, coords: list) -> Tuple[int, int]:
        if len(coords) < 1:
            raise ValueError("Empty List")
        if len(coords) == 1:
            return 0, coords[0]
        c = coords.copy()
        c.reverse()
        direction = cls.calculate_direction(c[0], c[1])
        for i, coord in enumerate(c):
            if i == len(c) - 1:
                return i, coord
            if calculate_grid_distance(coord, c[i + 1]) == 1 and direction == cls.calculate_direction(coord, c[i + 1]):
                continue
            return i, coord
