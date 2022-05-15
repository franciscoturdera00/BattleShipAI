## Testing the strategies do not crash. Simple integration tests

import random

from game_logic.ai_play import play_alone
from strategies.random_strategy import RandomStrategy


ITERATIONS = 50


def test_random_strategy():
    for _ in range(ITERATIONS):
        boat_1 = random.randint(1, 5)
        boat_2 = random.randint(1, 4)
        boat_3 = random.randint(1, 3)
        boat_4 = random.randint(1, 2)
        ## Play Game
        strat = RandomStrategy((8, 8), boat_1, boat_2, boat_3, boat_4)
        moves = play_alone(strat, strat.create_board())
        assert type(moves) == int
