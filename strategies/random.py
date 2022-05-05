# from strategies.strategy import CreateStrategy, PlayStrategy
# from structures.direction import Direction
# from structures.field import Field


# class RandomStrategy(CreateStrategy):
#     """Create Board at random"""

#     def create_board(self, *boats: int) -> Field:
#         board = Field(self.dimensions[0], self.dimensions[1])
#         for boat_length in boats:
#             set_boat = False
#             while not set_boat:
#                 direction = Direction.generate_random()
