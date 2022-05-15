from typing import Tuple
from strategies.random_strategy import RandomCreateStrategy, RandomPlayStrategy
from strategies.strategy import PlayStrategy, Strategy
from structures.direction import Direction
from util.util import calculate_grid_distance


class LocalPlayStrategy(PlayStrategy):
    """If it hits something, try the spaces around it"""

    def __init__(self, dimensions, backup=None):
        super().__init__(dimensions, backup)
        self.hit_list = list()
        self.turns_since_last_hit = None
        self.last_attempted = None

    def attack(self) -> Tuple[int, int]:
        if self.turns_since_last_hit is None or len(self.hit_list) == 0:
            # No data to go off of yet
            return self.backup.attack()

        last_hit = self.hit_list[-1]
        if len(self.hit_list) == 1 and self.turns_since_last_hit < 4:
            # Just hit something, look around
            return self.__attack_around(last_hit)
        elif len(self.hit_list) == 1:
            # Nothing around, keep searching
            return self.backup.attack()

        # What was hit right before the latest
        past = self.hit_list[-2]
        if calculate_grid_distance(last_hit, past) == 1:
            # Next to each other
            direction = Direction.calculate_direction(past, last_hit)
            # Attempt to hit the next in line
            attack = self.__attack_next_in_chain(direction, last_hit)
            if attack:
                return attack
            else:
                # Hit the opposite side of the line
                attack = self.__attack_opposite_end(direction)
                if attack:
                    return attack
        return self.__attack_around(last_hit)

    def __attack_around(self, last_hit):
        for dir in Direction:
            if not Direction.out_of_bounds(last_hit, 2, self.dimensions, dir):
                attack = Direction.calculate_endpoint(last_hit, 2, dir)
                if attack not in self.attacked:
                    return attack
        return self.backup.attack()

    def __attack_opposite_end(self, direction: Direction):
        other_end = Direction.calculate_start_of_chain(self.hit_list)
        attack = Direction.calculate_endpoint(other_end[1], 2, direction.opposite())
        if attack not in self.attacked and not Direction.out_of_bounds(
            attack, 1, self.dimensions, direction.opposite()
        ):
            self.hit_list = self.__reverse_chain(self.hit_list.copy(), other_end[0])
            return attack

    def __reverse_chain(self, hit_list, slice_point):
        return hit_list[slice_point::-1]

    def __attack_next_in_chain(self, direction: Direction, from_coord: Tuple[int, int]):
        to = Direction.calculate_endpoint(from_coord, 2, direction)
        if not Direction.out_of_bounds(to, 1, self.dimensions, direction) and to not in self.attacked:
            return to

    def feedback(self, coords: Tuple[int, int], hit: bool) -> None:
        super().feedback(coords, hit)
        if hit:
            self.opponent.add_boat(1, coords[0], coords[1], Direction.EAST)
            self.opponent.hit(coords[0], coords[1])
            self.hit_list.append(coords)
            self.turns_since_last_hit = 0
        elif self.turns_since_last_hit:
            self.turns_since_last_hit += 1


class LocalStrategy(Strategy):
    def __init__(self, dimensions, *boats):
        create_strat = RandomCreateStrategy(dimensions)
        play_strat = LocalPlayStrategy(dimensions, RandomPlayStrategy(dimensions))
        super().__init__(create_strat, play_strat, dimensions, *boats)
