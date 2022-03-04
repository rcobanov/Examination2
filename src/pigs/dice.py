import random


class Dice():
    """The dice class."""

    faces = 6
    this_roll = 0

    def __init__(self):
        """Initiate a dice object."""
        random.seed()

    def roll(self):
        """Roll the dice."""
        roll = random.randint(1, self.faces)
        self.this_roll = roll
        return roll
