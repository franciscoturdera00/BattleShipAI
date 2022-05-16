from pprint import pprint
import random
from typing import Tuple

import numpy
from strategies.random_strategy import RandomCreateStrategy, RandomPlayStrategy

from strategies.strategy import PlayStrategy, Strategy
from structures.direction import Direction


class PlayEducatedGuess(PlayStrategy):
    def attack(self) -> Tuple[int, int]:
        weights = self.create_weights()
        for y, vals in enumerate(self.opponent.spaces):
            for x, space in enumerate(vals):
                if not space.is_hit:
                    # Look in every direction and weigh appropiately
                    weights[y][x] = self.calculate_weight(weights, x, y)
                else:
                    weights[y][x] = -1
        best_val = numpy.amax(weights)
        result = numpy.where(weights == best_val)
        best_coordinates = list(zip(result[0], result[1]))
        choice = None
        while not choice or choice in self.attacked:
            if len(best_coordinates) == 0:
                return self.backup.attack()
            choice = random.choice(best_coordinates)
            best_coordinates.remove(choice)
        return choice

    def calculate_weight(self, wmap, x_coord, y_coord):
        weight = 0
        reduction = 0.5
        for dir in Direction:
            weight += 1.0 * self.opponent.calculate_linear_empty_space((x_coord, y_coord), dir) ** reduction
        return weight

    def create_weights(self):
        weights = list()
        for y, vals in enumerate(self.opponent.spaces):
            weights.append(list())
            for _ in enumerate(vals):
                weights[y].append(0)
        return weights

    def feedback(self, coords: Tuple[int, int], hit: bool) -> None:
        super().feedback(coords, hit)


class EducatedGuess(Strategy):
    def __init__(self, dimensions, *boats):
        create_strat = RandomCreateStrategy(dimensions)
        play_strat = PlayEducatedGuess(dimensions, RandomPlayStrategy(dimensions))
        super().__init__(create_strat, play_strat, dimensions, *boats)
