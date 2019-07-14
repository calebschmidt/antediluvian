import curses

import gameobjects


class Player(gameobjects.GameObject):
    def __init__(self, world):
        super().__init__('@', world=world)

    def draw(self, stdscr):
        stdscr.addch(self.window_y, self.window_x, self.char, curses.A_REVERSE)

    def update(self, key):
        dx = 0
        dy = 0
        turn_taken = False

        if key == 'KEY_UP':
            dy -= 1
        elif key == 'KEY_DOWN':
            dy += 1
        if key == 'KEY_LEFT':
            dx -= 1
        elif key == 'KEY_RIGHT':
            dx += 1

        turn_taken = self.move(dx, dy)

        return turn_taken
