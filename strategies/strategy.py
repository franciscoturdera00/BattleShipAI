from abc import ABC, abstractmethod
from typing import Tuple

from structures.field import Field


class CreateStrategy(ABC):
    """Base Strategy for creating a board"""

    backup: "CreateStrategy"

    def __init__(self, dimensions, backup: Field = None):
        self.dimensions = dimensions
        self.backup = backup

    @abstractmethod
    def create_board(self, *boats: int) -> Field:
        """Given a series of lengths of boats, create its playing board"""
        self.populated_spots = sum(boats)


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
    def feedback(self, coords: Tuple[int, int], hit: bool) -> None:
        """Update knowledge based on feedback from attack"""
        if hit:
            self.success += 1


class Strategy:

    create_strategy: CreateStrategy
    play_strategy: PlayStrategy

    def __init__(self, create_strat: CreateStrategy, play_strat: PlayStrategy, dimensions, *boats):
        self.create_strategy = create_strat
        self.play_strategy = play_strat
        self.board = self.create_board(*boats)

    def create_board(self, *boats: int) -> Field:
        return self.create_strategy.create_board(*boats)

    def get_board(self):
        return self.board

    def get_remaining_boat_spaces(self):
        return self.create_strategy.populated_spots - self.play_strategy.success

    def attack(self) -> Tuple[int, int]:
        return self.play_strategy.attack()

    def feedback(self, coords: Tuple[int, int], hit: bool) -> None:
        self.play_strategy.feedback(coords, hit)
