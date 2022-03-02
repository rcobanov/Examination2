import random


class Dice():
    faces = 6
    this_roll = 0

    def __init__(self):
        random.seed()

    def roll(self):
        roll = random.randint(1, self.faces)
        self.this_roll = roll
        return roll
