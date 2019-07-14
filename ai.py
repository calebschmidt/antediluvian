import random


class Brain:
    def __init__(self):
        self.body = None

    def initialize(self, body):
        self.body = body

    def update(self):
        raise NotImplementedError


class RandomBrain(Brain):
    def update(self):
        while True:
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            if self.body.move(dx, dy):
                break
