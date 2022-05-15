#!/usr/bin/env python3

from game_logic.ai_play import play_alone
from strategies.local_strategy import LocalStrategy
from strategies.random_strategy import RandomStrategy
from structures.direction import Direction
from structures.field import Field


if __name__ == "__main__":
    # strat = RandomStrategy((8, 8), 5, 3, 6, 1)
    strat = LocalStrategy((8, 8), 5, 3, 6, 4)
    board = strat.get_board()
    board.draw_field()
    print()
    # board.draw_field()
    moves = play_alone(strat, board, True)
    print()
    print("Moves: %s" % moves)
    # moves = 0
    # while random_strat.get_remaining_boats() > 0:
    #     moves += 1
    #     attack_x, attack_y = random_strat.attack()
    #     hit = board.hit(attack_x, attack_y)
    #     random_strat.feedback(attack_x, attack_y, hit)
    #     if hit:
    #         board.draw_field()
    #         print()
    #     # random_strat.play_strategy.opponent.draw_field()
    # print()
    # print("Moves: %s" % moves)


# if __name__ == "__main__":
# board = Field(4, 4)
# board.add_boat(4, 0, 1, Direction.EAST)
# board.add_boat(1, 1, 0)
# board.add_boat(1, 2, 2)
# board.draw_field()
# random_strat = RandomStrategy((8, 8), 5, 3, 6, 1)
# random_strat.get_board().draw_field()
