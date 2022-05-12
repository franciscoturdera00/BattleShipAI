from copy import deepcopy
from typing import Tuple
from strategies.strategy import CreateStrategy, PlayStrategy, Strategy
from structures.direction import Direction
from structures.field import Field
from util.util import generate_random_coordinate


class RandomCreateStrategy(CreateStrategy):
    """Create Board at random"""

    def create_board(self, *boats: int) -> Field:
        super().create_board(*boats)
        board = None
        while not board:
            board = self.__create_board(*boats)
        return board

    def __create_board(self, *boats: int):
        redo = 0
        max_redo = 1000
        board = Field(self.dimensions[0], self.dimensions[1])
        for boat_length in boats:
            set_boat = False
            while not set_boat and redo < max_redo:
                direction = Direction.generate_random()
                if boat_length == 1:
                    direction = None
                x, y = generate_random_coordinate(self.dimensions[0], self.dimensions[1])
                if board.can_add_boat(boat_length, x, y, direction):
                    board.add_boat(boat_length, x, y, direction)
                    set_boat = True
                    redo = 0
                    break
                else:
                    redo += 1
            if redo >= max_redo:
                return None
        return board


class RandomPlayStrategy(PlayStrategy):
    """Attack randomly"""

    def attack(self) -> Tuple[int, int]:
        x, y = generate_random_coordinate(self.dimensions[0], self.dimensions[1], self.attacked)
        self.attacked.add((x, y))
        return x, y

    def feedback(self, coords: Tuple[int, int], hit: bool) -> None:
        super().feedback(coords, hit)
        if hit:
            self.opponent.add_boat(1, coords[0], coords[1])
            self.opponent.hit(coords[0], coords[1])


class RandomStrategy(Strategy):
    def __init__(self, dimensions, *boats: int):
        create_strat = RandomCreateStrategy(dimensions)
        play_strat = RandomPlayStrategy(dimensions)
        super().__init__(create_strat, play_strat, dimensions, *boats)
