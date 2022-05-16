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
        if hit and draw_progress:
            board.draw_field()
            print()
    return moves


# def compete(strategy: Strategy):
#     ai_up = False
#     turn = int(input())
#     if turn == 1:
#         ai_up = True
#     # Give ships
#     ...
#     while True:
#         if ai_up:
#             strategy.attack()
#             feedback = input().split(":")
#             x, y = feedback[0].split(",")
#             hit = feedback[1] == "hit"
#             strategy.feedback((x, y), hit)
#             ai_up = False
#         else:
#             input()
#             ai_up = True
