from structures.direction import Direction
from structures.field import Field


if __name__ == "__main__":
    battleship = Field(8, 8)
    print(battleship.add_boat(5, 0, 0, Direction.SOUTH))
    print(battleship.add_boat(5, 1, 0, Direction.EAST))
    print(battleship.hit(0, 0))
    print(battleship.hit(1, 1))
    battleship.draw_field()
