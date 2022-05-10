## Testing the strategies do not crash. Simple integration tests

import random


ITERATIONS = 50


def test_random_strategy():
    for _ in range(ITERATIONS):
        boat_1 = random.randint(1, 5)
        boat_2 = random.randint(1, 4)
        boat_3 = random.randint(1, 3)
        boat_4 = random.randint(1, 2)
        ## Play Game
