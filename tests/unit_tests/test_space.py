from game_logic.exceptions import IllegalMove, IllegalPlacement
from structures.space import Space, SpaceStatus
import pytest


def test_hit():
    space = Space(0, 0)
    assert space.is_hit == False
    space.hit()
    assert space.is_hit == True


def test_throw_hit():
    space = Space(0, 0)
    space.hit()
    with pytest.raises(IllegalMove):
        space.hit()


def test_has_boat():
    space = Space(0, 0)
    assert space.has_boat() == False
    space.status = SpaceStatus.BOAT
    assert space.has_boat() == True


def test_insert_boat():
    space = Space(0,0)
    assert space.status == SpaceStatus.EMPTY
    space.insert_boat()
    assert space.status == SpaceStatus.BOAT
    
    with pytest.raises(IllegalPlacement):
        space.insert_boat()
    