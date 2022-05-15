import pytest
from structures.direction import Direction


def test_calculate_endpoint_in_board():
    new_point = Direction.calculate_endpoint((0, 0), 5, Direction.SOUTH)
    assert new_point == (0, 4)
    new_point = Direction.calculate_endpoint((10, 0), 5, Direction.SOUTH)
    assert new_point == (10, 4)
    new_point = Direction.calculate_endpoint((0, 0), 5, Direction.EAST)
    assert new_point == (4, 0)


def test_calculate_endpoint_out_of_board():
    new_point = Direction.calculate_endpoint((0, 0), 5, Direction.WEST)
    assert new_point == (-4, 0)


def test_out_of_bounds():
    assert Direction.out_of_bounds((0, 0), 1, (2, 2), Direction.EAST) == False
    assert Direction.out_of_bounds((0, 0), 1, (1, 1), Direction.EAST) == False
    assert Direction.out_of_bounds((0, 0), 2, (2, 3), Direction.SOUTH) == False
    assert Direction.out_of_bounds((0, 0), 2, (2, 2), Direction.SOUTH) == False
    assert Direction.out_of_bounds((0, 0), 2, (2, 3), Direction.NORTH) == True
    assert Direction.out_of_bounds((0, 0), 1, (1, 1), Direction.EAST) == False
    assert Direction.out_of_bounds((0, 0), 3, (2, 2), Direction.SOUTH) == True


def test_generate_random():
    assert type(Direction.generate_random()) == Direction


def test_calculate_direction():
    assert Direction.calculate_direction((1, 1), (1, 2)) == Direction.SOUTH
    assert Direction.calculate_direction((1, 1), (2, 1)) == Direction.EAST
    assert Direction.calculate_direction((1, 1), (0, 1)) == Direction.WEST
    assert Direction.calculate_direction((1, 1), (1, 0)) == Direction.NORTH
    with pytest.raises(ValueError):
        Direction.calculate_direction((1, 1), (2, 2))
    
    with pytest.raises(ValueError):
        Direction.calculate_direction((1, 1), (1, 1))