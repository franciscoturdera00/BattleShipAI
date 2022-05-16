## Testing the strategies do not crash. Simple integration tests

import random

from game_logic.ai_play import play_alone
from strategies.educated_guess import EducatedGuess
from strategies.local_strategy import LocalStrategy
from strategies.random_strategy import RandomStrategy
from strategies.strategy import Strategy


ITERATIONS = 50


def test_random_strategy():
    strat = RandomStrategy
    play(strat)


def test_local_strategy():
    strat = LocalStrategy
    play(strat)


def test_local_strategy():
    strat = EducatedGuess
    play(strat)


def play(strat: Strategy):
    for _ in range(ITERATIONS):
        boat_1 = random.randint(1, 5)
        boat_2 = random.randint(1, 4)
        boat_3 = random.randint(1, 3)
        boat_4 = random.randint(1, 2)
        strategy = strat((8, 8), boat_1, boat_2, boat_3, boat_4)
        moves = play_alone(strategy, strategy.create_board())
        assert type(moves) == int
