import random


class Dice():
    faces = 6
    thisRoll = 0

    def __init__(self):
        random.seed()

    def roll(self):
        roll = random.randint(1, self.faces)
        self.thisRoll = roll
        return roll

    def rollMultipleTimes(self, timesToRoll):
        totalRoll = 0
        for x in range(timesToRoll):
            roll = random.randint(1, self.faces)
            totalRoll += roll
            if roll == 1:
                return 1
                break
        return totalRoll
