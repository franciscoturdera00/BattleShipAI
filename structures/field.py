from game_logic.exceptions import OutOfBounds
from structures.space import Space
from structures.direction import Direction
from colorama import Fore


class Field:
    def __init__(self, dimension_x, dimension_y):
        self.dimensions = list()
        for x in range(dimension_x):
            self.dimensions.append(list())
            for y in range(dimension_y):
                self.dimensions[x].append(Space(x, y))

        self.outter_limits = (dimension_x, dimension_y)

    def can_add_boat(self, length: int, anchor_x: int, anchor_y, direction: Direction) -> bool:
        if Direction.out_of_bounds((anchor_x, anchor_y), length, self.outter_limits, direction):
            return False
        final_y, final_x = Direction.calculate_endpoint((anchor_x, anchor_y), length, direction)
        if anchor_y != final_y:
            return self.__can_add_boat(anchor_y, final_y, anchor_x, False)
        elif anchor_x != final_x:
            return self.__can_add_boat(anchor_x, final_x, anchor_y, True)

    def add_boat(self, length: int, anchor_x: int, anchor_y, direction: Direction) -> bool:
        if not self.can_add_boat(length, anchor_x, anchor_y, direction):
            raise OutOfBounds("Boat cannot be located here")
        final_y, final_x = Direction.calculate_endpoint((anchor_x, anchor_y), length, direction)
        if anchor_y != final_y:
            return self.__add_boat(anchor_y, final_y, anchor_x, False)
        elif anchor_x != final_x:
            return self.__add_boat(anchor_x, final_x, anchor_y, True)

    def hit(self, hit_x, hit_y) -> bool:
        return self.dimensions[hit_y][hit_x].hit()

    def draw_field(self, hide=False):
        for y in self.dimensions:
            print()
            print(" -- " * len(y))
            for space in y:
                # print((space.x, space.y), end="")
                if space.has_boat and space.is_hit:
                    print(Fore.RED + " X ", end="")
                    print(Fore.WHITE + "|", end="")
                elif space.has_boat and not hide:
                    print(Fore.GREEN + " O ", end="")
                    print(Fore.WHITE + "|", end="")
                else:
                    print(Fore.BLUE + " E ", end="")
                    print(Fore.WHITE + "|", end="")

    def __can_add_boat(self, begin, end, anchor, vertical: bool) -> bool:
        step = int((end - begin) / abs(end - begin))
        # First, check we can add boat
        for val in range(begin, end, step):
            if vertical and self.dimensions[anchor][val].has_boat:
                return False
            elif self.dimensions[val][anchor].has_boat:
                return False
        return True

    def __add_boat(self, begin, end, anchor, vertical: bool):
        step = int((end - begin) / abs(end - begin))
        # Add boat
        for val in range(begin, end, step):
            if vertical:
                self.dimensions[val][anchor].has_boat = True
            else:
                self.dimensions[anchor][val].has_boat = True
