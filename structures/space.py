class Space:
    def __init__(self, y_coord, x_coord, has_boat=False):
        self.x = x_coord
        self.y = y_coord
        self.has_boat = has_boat
        self.is_hit = False

    def hit(self):
        if self.has_boat:
            self.is_hit = True
            return True
        return False
