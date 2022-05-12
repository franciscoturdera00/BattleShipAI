from strategies.random_strategy import RandomCreateStrategy


def test_random_create():
    create = RandomCreateStrategy((8, 8))
    board = create.create_board(5, 4, 3, 2, 1)
    assert board is not None
    count = 0
    for column in board.spaces:
        for space in column:
            if space.has_boat():
                count += 1

    assert count == create.populated_spots
    assert count == sum([5, 4, 3, 2, 1])
