from game_logic.exceptions import IllegalMove
from structures.direction import Direction
from structures.field import Field
from structures.space import SpaceStatus
import pytest


def test_can_add_boat_basic():
    field = Field(1, 1)
    assert field.can_add_boat(1, 0, 0) == True
    # Ensure can_add_boat does NOT add boat
    assert field.can_add_boat(1, 0, 0) == True

    field.spaces[0][0].status = SpaceStatus.BOAT
    assert field.can_add_boat(1, 0, 0) == False


def test_can_add_boat():
    field = Field(1, 1)
    assert field.can_add_boat(1, 0, 0, Direction.SOUTH) == True

    bigger_field = Field(6, 6)
    bigger_field.can_add_boat(2, 3, 3, Direction.NORTH) == True
    bigger_field.can_add_boat(2, 3, 3, Direction.EAST) == True
    bigger_field.can_add_boat(2, 3, 3, Direction.WEST) == True
    bigger_field.can_add_boat(2, 3, 3, Direction.SOUTH) == True

    with pytest.raises(ValueError):
        bigger_field.can_add_boat(2, 3, 3)

    bigger_field.can_add_boat(5, 3, 3, Direction.SOUTH) == False

    empty_field = Field(5, 5)
    assert empty_field.can_add_boat(4, -1, 0, Direction.EAST) == False
    assert empty_field.can_add_boat(4, 0, -1, Direction.SOUTH) == False
    assert empty_field.can_add_boat(1, -1, 0) == False
    assert empty_field.can_add_boat(1, 0, -1) == False
    assert empty_field.can_add_boat(1, 5, 0) == False
    assert empty_field.can_add_boat(1, 0, 5) == False
    assert empty_field.can_add_boat(3, 5, 0, Direction.WEST) == False
    assert empty_field.can_add_boat(3, 0, 5, Direction.NORTH) == False


def test_add_boat_raises():
    field = Field(1, 1)
    field.add_boat(1, 0, 0)
    with pytest.raises(IllegalMove):
        field.add_boat(1, 0, 0)


def test_add_boat_east():
    field = Field(6, 6)
    field.add_boat(3, 1, 1, Direction.EAST)
    assert field.spaces[1][0].has_boat() == False
    assert field.spaces[1][1].has_boat()
    assert field.spaces[1][2].has_boat()
    assert field.spaces[1][3].has_boat()
    assert field.spaces[1][4].has_boat() == False


def test_add_boat_south():
    field = Field(6, 6)
    field.add_boat(3, 1, 1, Direction.SOUTH)
    assert field.spaces[0][1].has_boat() == False
    assert field.spaces[1][1].has_boat()
    assert field.spaces[2][1].has_boat()
    assert field.spaces[3][1].has_boat()
    assert field.spaces[4][1].has_boat() == False


def test_add_boat_west():
    field = Field(6, 6)
    field.add_boat(3, 4, 4, Direction.WEST)
    assert field.spaces[4][5].has_boat() == False
    assert field.spaces[4][4].has_boat()
    assert field.spaces[4][3].has_boat()
    assert field.spaces[4][2].has_boat()
    assert field.spaces[4][1].has_boat() == False


def test_add_boat_north():
    field = Field(6, 6)
    field.add_boat(3, 4, 4, Direction.NORTH)
    assert field.spaces[5][4].has_boat() == False
    assert field.spaces[4][4].has_boat()
    assert field.spaces[3][4].has_boat()
    assert field.spaces[2][4].has_boat()
    assert field.spaces[1][4].has_boat() == False


def test_add_boat_singleton():
    field = Field(6, 6)
    field.add_boat(1, 3, 3)
    assert field.spaces[3][3].has_boat()
    assert field.spaces[3][4].has_boat() == False
    assert field.spaces[4][3].has_boat() == False
    assert field.spaces[3][2].has_boat() == False
    assert field.spaces[2][3].has_boat() == False


def test_add_boat_singleton_with_direction():
    field = Field(6, 6)
    field.add_boat(1, 3, 3, Direction.EAST)
    assert field.spaces[3][3].has_boat()
    assert field.spaces[3][4].has_boat() == False
    assert field.spaces[4][3].has_boat() == False
    assert field.spaces[3][2].has_boat() == False
    assert field.spaces[2][3].has_boat() == False
