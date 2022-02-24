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

    def playOneRound(self):
        pass
