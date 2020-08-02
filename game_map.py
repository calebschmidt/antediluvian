import collections


class Map(collections.UserList):
    def __init__(self, size_x, size_y):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y

        for y in range(self.size_y):
            row = list()
            for x in range(self.size_x):
                row.append(Tile('.', x, y))
            self.append(row)


class Tile:
    def __init__(self, base_char, x, y, walkable=True, blocks_sight=False):
        self.base_char = base_char
        self.walkable = walkable
        self.blocks_sight = blocks_sight
        self.x = x
        self.y = y

    def draw(self, stdscr):
        stdscr.addch(self.y, self.x, self.base_char)

