import random

import ai
import gameobjects


class World:
    def __init__(self):
        self.map = None
        self.actors = list()

    def initialize_map(self, size_x=60, size_y=20):
        # TODO: Move to map factory
        self.map = list()

        for y in range(size_y):
            row = list()
            for x in range(size_x):
                row.append(Tile('.', x, y))
            self.map.append(row)

        # TODO: Move to actor factory
        for i in range(10):
            self.actors.append(
                gameobjects.Actor(
                    random.choice('spTrXz'),
                    self,
                    random.randint(0, size_x - 1),
                    random.randint(0, size_y - 1),
                    ai.RandomBrain()
                )
            )

    def on_map(self, x, y):
        return (0 <= x < len(self.map[0])) and (0 <= y < len(self.map))

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
