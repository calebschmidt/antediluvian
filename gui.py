import curses


class GUI:
    def __init__(self, game, screen_x, screen_y):
        self.game = game
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.stdscr = None
        self.things_to_draw = list()

    def initialize(self):
        self.stdscr = curses.initscr()
        curses.resizeterm(self.screen_y, self.screen_x)
        self.stdscr.keypad(True)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(False)

    def teardown(self):
        self.stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.curs_set(False)
        curses.endwin()

    def before_draw(self):
        self.stdscr.clear()

    def draw(self):
        self.stdscr.addstr(self.screen_y - 1, 0, 'PLAYER: ({}, {})'.format(self.game.player.window_x, self.game.player.window_y))

    def after_draw(self):
        self.stdscr.refresh()

    def get_input(self):
        return self.stdscr.getkey()

    def main_menu(self):
        self.stdscr.addstr(self.screen_y // 2 - 4, self.screen_x // 2 - 3, '(P)LAY')
        self.stdscr.addstr(self.screen_y // 2 - 3, self.screen_x // 2 - 3, '(Q)UIT')

    def paused(self):
        self.stdscr.addstr(self.screen_y // 2 - 4, self.screen_x // 2 - 3, 'PAUSED')

