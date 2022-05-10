#!/usr/bin/env python3

from strategies.random_strategy import RandomStrategy
from structures.direction import Direction
from structures.field import Field


if __name__ == "__main__":
    random_strat = RandomStrategy((8, 8), 5, 3, 6, 1)
    board = random_strat.get_board()
    board.draw_field()
    print()
    # board.draw_field()
    moves = 0
    while random_strat.get_remaining_boats() > 0:
        moves += 1
        attack_x, attack_y = random_strat.attack()
        hit = board.hit(attack_x, attack_y)
        random_strat.feedback(attack_x, attack_y, hit)
        if hit:
            board.draw_field()
            print()
        # random_strat.play_strategy.opponent.draw_field()
    print()
    print("Moves: %s" % moves)


# if __name__ == "__main__":
# board = Field(4, 4)
# board.add_boat(4, 0, 1, Direction.EAST)
# board.add_boat(1, 1, 0)
# board.add_boat(1, 2, 2)
# board.draw_field()
# random_strat = RandomStrategy((8, 8), 5, 3, 6, 1)
# random_strat.get_board().draw_field()
