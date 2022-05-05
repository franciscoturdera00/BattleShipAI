from enum import Enum

from game_logic.exceptions import IllegalMove, IllegalPlacement


class Space:
    def __init__(self, y_coord, x_coord, has_boat=False):
        self.x = x_coord
        self.y = y_coord
        self.status = SpaceStatus.EMPTY
        if has_boat:
            self.status = SpaceStatus.BOAT
        self.is_hit = False

    def hit(self):
        self.is_hit = True
        if self.has_boat():
            return True
        return False

    def insert_boat(self):
        if self.status == SpaceStatus.EMPTY:
            self.status = SpaceStatus.BOAT
            return
        raise IllegalPlacement("Boat already placed at (%d, %d)" % (self.x, self.y))

    def has_boat(self):
        return self.status == SpaceStatus.BOAT


class SpaceStatus(Enum):
    EMPTY = 1
    BOAT = 2
