import random


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
