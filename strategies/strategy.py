from abc import ABC, abstractmethod
from typing import Tuple

from structures.field import Field


class CreateStrategy(ABC):
    """Base Strategy for creating a board"""

    backup: "CreateStrategy"

    def __init__(self, dimensions, backup: Field, *boats: int):
        self.dimensions = dimensions
        self.board = self.create_board(None, *boats)
        self.populated_spots = sum(boats)
        self.backup = backup

    @abstractmethod
    def create_board(self, board, *boats: int) -> Field:
        """Given a series of lengths of boats, create its playing board"""
        pass


class PlayStrategy(ABC):
    """Abstract Strategy for making attacks"""

    opponent: Field
    attacked: set
    backup: "PlayStrategy"

    def __init__(self, dimensions, backup=None):
        self.dimensions = dimensions
        self.opponent = Field(dimensions[0], dimensions[1])
        self.attacked = set()
        self.success = 0
        self.backup = backup

    @abstractmethod
    def attack(self) -> Tuple[int, int]:
        """Attack a coordinate"""
        pass

    @abstractmethod
    def feedback(self, x_coord: int, y_coord: int, hit: bool) -> None:
        """Update knowledge based on feedback from attack"""
        pass


class Strategy:

    create_strategy: CreateStrategy
    play_strategy: PlayStrategy

    def __init__(self, create_strat: CreateStrategy, play_strat: PlayStrategy, dimensions, *boats):
        self.create_strategy = create_strat
        self.play_strategy = play_strat

    def create_board(self, *boats: int) -> Field:
        print(boats)
        return self.create_strategy.create_board(None, *boats)

    def get_board(self):
        return self.create_strategy.board

    def get_remaining_boats(self):
        return self.create_strategy.populated_spots - self.play_strategy.success

    def attack(self) -> Tuple[int, int]:
        return self.play_strategy.attack()

    def feedback(self, x_coord: int, y_coord: int, hit: bool) -> None:
        self.play_strategy.feedback(x_coord, y_coord, hit)
