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

    def rollMultipleTimes(self, times_to_roll):
        total_rolls = 0
        for x in range(times_to_roll):
            roll = random.randint(1, self.faces)
            total_rolls += roll
            if roll == 1:
                return 1
                break
        return total_rolls
