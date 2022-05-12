from game_logic.ai_play import play_alone
from strategies.random_strategy import RandomStrategy
from structures.direction import Direction
from structures.field import Field
from util.util import calculate_non_hit_spaces


def test_play_alone_basic():
    board = Field(1, 1)
    board.add_boat(1, 0, 0)
    strat = RandomStrategy((1, 1), 1)
    moves = play_alone(strat, board)
    assert moves == 1


def test_play_alone_complex():
    size = 8
    board = Field(size, size)
    board.add_boat(5, 0, 0, Direction.EAST)
    board.add_boat(3, 1, 1, Direction.SOUTH)
    board.add_boat(1, 6, 6)
    strat = RandomStrategy((size, size), 1)
    moves = play_alone(strat, board)
    assert moves == size**2 - calculate_non_hit_spaces(board)
