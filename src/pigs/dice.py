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