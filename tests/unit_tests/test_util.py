from structures.field import Field
from util.util import calculate_non_hit_spaces, generate_random_coordinate


def test_generate_random_coordinate_basic():
    assert generate_random_coordinate(1, 1) == (0, 0)


def test_generate_random_coordinate():
    size = 5
    for _ in range(size**5):
        x, y = generate_random_coordinate(size, size)
        assert 0 <= x < size and 0 <= y < size


def test_generate_random_coordinate_with_list():
    size = 5
    unavailable = set()
    for _ in range(size**2):
        x, y = generate_random_coordinate(size, size, unavailable)
        unavailable.add((x, y))
        assert 0 <= x < size and 0 <= y < size

    for i in range(size):
        for j in range(size):
            assert (i, j) in unavailable


def test_calculate_non_empty_spaces():
    board = Field(5, 5)
    assert calculate_non_hit_spaces(board) == 25
    board.hit(1, 1)
    assert calculate_non_hit_spaces(board) == 24
    board.add_boat(1, 4, 4)
    assert calculate_non_hit_spaces(board) == 24
    board.hit(4, 4)
    assert calculate_non_hit_spaces(board) == 23
