import dice

class Bot():
    isHolding = False

    def __init__(self, currRoundScore, totalScore, level):
        self.currRoundScore = currRoundScore
        self.totalScore = totalScore
        self.level = level


    def getNumberOfRounds(self, llevel):
        roundsToRun = 0
        if llevel == 1:
            roundsToRun = 5
        elif llevel == 2:
            roundsToRun = 9
        elif llevel == 3:
            roundsToRun = 14
        return roundsToRun

    def addCurrToTotal(self):
        self.totalScore += self.currRoundScore

    def resetCurrentScore(self):
        self.currRoundScore = 0

    def bot_play_one_round(self, die):
        roundstoRun = self.getNumberOfRounds(int(self.level))
        for x in range(roundstoRun):
            self.currRoundScore += die.roll()
            print(f"The bot dice shows {die.this_roll}")
            if die.this_roll == 1:
                self.resetCurrentScore()
                print("The bot rolled a 1!!")
                print("--------------------")
                break
        self.addCurrToTotal()
        self.resetCurrentScore()
        print(f"Current bot round score {self.currRoundScore}")
        print(f"Total bot score {self.totalScore}")

    def reset_bot(self):
        self.currRoundScore = 0
        self.totalScore = 0
