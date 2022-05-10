from structures.direction import Direction
import pytest


def test_calculate_endpoint_in_board():
    new_point = Direction.calculate_endpoint((0, 0), 5, Direction.SOUTH)
    assert new_point == (0, 5)
    new_point = Direction.calculate_endpoint((10, 0), 5, Direction.SOUTH)
    assert new_point == (10, 5)
    new_point = Direction.calculate_endpoint((0, 0), 5, Direction.EAST)
    assert new_point == (5, 0)


def test_calculate_endpoint_out_of_board():
    new_point = Direction.calculate_endpoint((0, 0), 5, Direction.WEST)
    assert new_point == (-5, 0)


def test_out_of_bounds():
    assert Direction.out_of_bounds((0, 0), 1, (2, 2)) == False
    assert Direction.out_of_bounds((0, 0), 1, (1, 1), Direction.EAST) == False
    assert Direction.out_of_bounds((0, 0), 2, (2, 3), Direction.SOUTH) == False
    assert Direction.out_of_bounds((0, 0), 2, (2, 2), Direction.SOUTH) == True
    assert Direction.out_of_bounds((0, 0), 2, (2, 3), Direction.NORTH) == True
    assert Direction.out_of_bounds((0, 0), 1, (1, 1)) == False
    with pytest.raises(ValueError):
        Direction.out_of_bounds((0, 0), 2, (8, 8))


def test_generate_random():
    assert type(Direction.generate_random()) == Direction
