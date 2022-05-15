from time import sleep
from strategies.strategy import Strategy
from structures.field import Field


def play_alone(strategy: Strategy, board: Field, draw_progress: bool = False) -> int:
    moves = 0
    while strategy.get_remaining_boat_spaces() > 0:
        moves += 1
        attack_x, attack_y = strategy.attack()
        # print(attack_x, attack_y)
        # sleep(1)
        hit = board.hit(attack_x, attack_y)
        strategy.feedback((attack_x, attack_y), hit)
        if draw_progress:
            board.draw_field()
            print()
    return moves
