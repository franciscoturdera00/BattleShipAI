import random

from structures.field import Field


def generate_random_coordinate(max_x, max_y, unavailable=None):
    coords = list()
    for x in range(max_x):
        for y in range(max_y):
            if unavailable and (x, y) not in unavailable:
                coords.append((x, y))
            elif not unavailable:
                coords.append((x, y))
    final_x, final_y = random.choice(coords)
    return final_x, final_y


def calculate_non_hit_spaces(board: Field) -> int:
    num = 0
    for y in board.spaces:
        for space in y:
            if not space.is_hit:
                num += 1
    return num
