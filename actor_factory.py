import random

import ai
import gameobjects


class ActorFactory:
    def __init__(self, world=None):
        self.world = world

    def generate_actors(self, number):
        actors = list()
        for _ in range(number):
            # TODO: Move to actor factory
            actor = gameobjects.Actor(
                random.choice('spTrXz'),
                self,
                random.randint(0, self.map.size_x - 1),
                random.randint(0, self.map.size_y - 1),
                ai.RandomBrain()
            )
            actors.append(actor)

        return actors
