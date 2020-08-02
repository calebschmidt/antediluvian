import gui
import world
import player
from contexts import contexts


class Game:
    def __init__(self):
        self.world = world.World()

        self.player = player.Player(self.world)
        self.player.place(10, 10)

        self.gui = gui.GUI(self, 100, 40)

        self.context = list()
        self.key = None

    def __enter__(self):
        self.initialize()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.teardown()

    @property
    def current_context(self):
        return self.context[-1]

    def initialize(self):
        self.context.append(contexts.MAIN_MENU)
        self.gui.initialize()
        self.world.initialize_map(100, 35)

    def teardown(self):
        self.gui.teardown()

    def run(self):
        while self.context:
            self.draw()
            self.get_input()
            self.update()

    def draw(self):
        # Clear screen
        self.gui.before_draw()

        if self.current_context == contexts.PLAYING:
            self.world.draw(self.gui.stdscr)
            self.player.draw(self.gui.stdscr)
            self.gui.draw()
        elif self.current_context == contexts.MAIN_MENU:
            self.gui.main_menu()
        elif self.current_context == contexts.PAUSED:
            self.world.draw(self.gui.stdscr)
            self.player.draw(self.gui.stdscr)
            self.gui.draw()
            self.gui.paused()

        # Refresh with new contents
        self.gui.after_draw()

    def get_input(self):
        self.key = self.gui.get_input()

    def update(self):
        # TODO: Delegate
        if self.current_context == contexts.PLAYING:
            if self.key in 'pP':
                # Pause playing
                self.context.append(contexts.PAUSED)
            elif self.key in 'qQ':
                # Quit to main menu
                self.context.pop()
            else:
                # Let player act
                turn_taken = self.player.update(self.key)
                # Only update everything else if a turn was taken
                if turn_taken:
                    self.world.update()

        elif self.current_context == contexts.MAIN_MENU:
            if self.key in 'qQ':
                # Quit
                self.context.pop()
            elif self.key in 'pP':
                # Play
                self.context.append(contexts.PLAYING)

        elif self.current_context == contexts.PAUSED:
            # Un-pause
            if self.key in 'pP':
                self.context.pop()
