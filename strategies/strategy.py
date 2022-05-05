from abc import ABC, abstractmethod
from typing import Tuple

from structures.field import Field


class PlayStrategy(ABC):
    """Abstract Strategy for making attacks"""

    def __init__(self, dimensions):
        self.opponent = Field(dimensions[0], dimensions[1])

    @abstractmethod
    def attack(self) -> Tuple[int, int]:
        """Attack a coordinate"""
        pass

    @abstractmethod
    def feedback(self, x_coord: int, y_coord: int, hit: bool) -> None:
        """Update knowledge based on feedback from attack"""
        pass


class CreateStrategy(ABC):
    """Base Strategy for creating a board"""

    def __init__(self, dimensions):
        self.dimensions = dimensions

    @abstractmethod
    def create_board(self, *boats: int) -> Field:
        """Given a series of lengths of boats, create its playing board"""
        pass


class Strategy:
    def __init__(self, create_strat: CreateStrategy, play_strat: PlayStrategy, dimensions):
        self.create_strategy = create_strat(dimensions)
        self.play_strategy = play_strat(dimensions)

    def create_board(self, *boats: int) -> Field:
        return self.create_strategy.create_board(*boats)

    def attack(self) -> Tuple[int, int]:
        return self.play_strategy.attack()

    def feedback(self, x_coord: int, y_coord: int, hit: bool) -> None:
        self.play_strategy.feedback(x_coord, y_coord, hit)
