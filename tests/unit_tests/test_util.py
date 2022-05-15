from util.util import generate_random_coordinate


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
