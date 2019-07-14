class GameObject:
    def __init__(self, char, world, window_x=None, window_y=None):
        self.char = char
        self.world = world
        self.window_x = window_x
        self.window_y = window_y

    def place(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y

    def move(self, dx, dy):
        new_x = self.window_x + dx
        new_y = self.window_y + dy

        if self.world.on_map(new_x, new_y) and self.world.walkable(new_x, new_y):
            self.window_x += dx
            self.window_y += dy
            return True
        return False

    def draw(self, stdscr):
        stdscr.addch(self.window_y, self.window_x, self.char)


class Actor(GameObject):
    def __init__(self, char, world, window_x, window_y, brain):
        super().__init__(char, world, window_x, window_y)
        self.brain = brain
        self.brain.initialize(self)

    def update(self):
        self.brain.update()
