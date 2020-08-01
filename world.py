import collections
import random

import actor_factory


class World:
    def __init__(self):
        self.map = None
        self.actors = list()
        self.actor_factory = actor_factory.ActorFactory(self)

    def initialize_map(self, size_x=60, size_y=20, num_actors=10):
        # TODO: Move to map factory
        self.map = Map(size_x, size_y)
        self.actors = self.actor_factory.generate_actors(num_actors)
        self.place_actors()

    def place_actors(self):
        for actor in self.actors:
            x = random.randint(0, self.map.size_x - 1)
            y = random.randint(0, self.map.size_y - 1)
            actor.place(x, y)

    def on_map(self, x, y):
        return (0 <= x < self.map.size_x) and (0 <= y < self.map.size_y)

    def walkable(self, x, y):
        return self.map[y][x].walkable

    def blocks_sight(self, x, y):
        return self.map[y][x].blocks_sight

    def draw(self, stdscr):
        # Draw terrain first
        for row in self.map:
            for tile in row:
                tile.draw(stdscr)

        # Creatures next
        for actor in self.actors:
            actor.draw(stdscr)

    def update(self):
        for actor in self.actors:
            actor.update()


class Tile:
    def __init__(self, base_char, x, y, walkable=True, blocks_sight=False):
        self.base_char = base_char
        self.walkable = walkable
        self.blocks_sight = blocks_sight
        self.x = x
        self.y = y

    def draw(self, stdscr):
        stdscr.addch(self.y, self.x, self.base_char)


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
