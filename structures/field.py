from game_logic.exceptions import IllegalMove, OutOfBounds
from structures.space import Space, SpaceStatus
from structures.direction import Direction
from colorama import Fore


class Field:
    def __init__(self, dimension_x, dimension_y):
        self.spaces = list()
        for y in range(dimension_y):
            self.spaces.append(list())
            for x in range(dimension_x):
                self.spaces[y].append(Space(x, y))

        self.outter_limits = (dimension_x, dimension_y)

    def can_add_boat(self, length: int, anchor_x: int, anchor_y: int, direction: Direction = None) -> bool:
        if Direction.out_of_bounds((anchor_x, anchor_y), length, self.outter_limits, direction):
            return False
        final_x, final_y = Direction.calculate_endpoint((anchor_x, anchor_y), length, direction)
        if anchor_y != final_y:
            return self.__can_add_boat(anchor_y, final_y, anchor_x, False)
        elif anchor_x != final_x:
            return self.__can_add_boat(anchor_x, final_x, anchor_y, True)
        else:  # Singeton
            return not self.spaces[anchor_y][anchor_x].has_boat()

    def add_boat(self, length: int, anchor_x: int, anchor_y, direction: Direction = None) -> bool:
        if not self.can_add_boat(length, anchor_x, anchor_y, direction):
            raise IllegalMove("Boat cannot be located at (%d, %d)" % (anchor_x, anchor_y))
        final_x, final_y = Direction.calculate_endpoint((anchor_x, anchor_y), length, direction)
        if anchor_y != final_y:
            self.__add_boat(anchor_y, final_y, anchor_x, False)
        elif anchor_x != final_x:
            self.__add_boat(anchor_x, final_x, anchor_y, True)
        else:  # Singleton
            self.spaces[anchor_y][anchor_x].insert_boat()

    def hit(self, hit_x, hit_y) -> bool:
        return self.spaces[hit_y][hit_x].hit()

    def build_field(self, hide=False):
        builder = ""
        length = len(self.spaces[0])
        for y in self.spaces:
            builder += "\n"
            builder += "----" * length
            builder += "\n"
            builder += Fore.WHITE + "|"
            for space in y:
                # print((space.x, space.y), end="")
                if space.has_boat() and space.is_hit:
                    builder += Fore.RED + " X "
                    builder += Fore.WHITE + "|"
                elif space.has_boat() and not hide:
                    builder += Fore.GREEN + " O "
                    builder += Fore.WHITE + "|"
                elif not space.has_boat() and space.is_hit:
                    builder += Fore.YELLOW + " M "
                    builder += Fore.WHITE + "|"
                else:
                    builder += Fore.BLUE + " E "
                    builder += Fore.WHITE + "|"
        builder += "\n"
        builder += "----" * length
        return builder

    def draw_field(self, hide=False):
        print(self.build_field(hide))

    def __can_add_boat(self, begin, end, anchor, vertical: bool) -> bool:
        step = int((end - begin) / abs(end - begin))
        for val in range(begin, end, step):
            if vertical and self.spaces[anchor][val].has_boat():
                return False
            elif self.spaces[val][anchor].has_boat():
                return False
        return True

    def __add_boat(self, begin, end, anchor, vertical: bool):
        step = int((end - begin) / abs(end - begin))
        # Add boat
        for val in range(begin, end, step):
            if vertical:
                self.spaces[anchor][val].insert_boat()
            else:
                self.spaces[val][anchor].insert_boat()
