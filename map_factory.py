import game_map


class MapFactory:
    def __init__(self, world=None):
        self.world = world

    def generate_map(self, size_x, size_y):
        # TODO: Fancify via kwargs
        return game_map.Map(size_x, size_y)

