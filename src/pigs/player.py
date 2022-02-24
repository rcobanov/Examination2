class Player():
    isHolding = False

    def __init__(self, name, currRoundScore, totalScore, rollsMade, longestStreak, favNumber):
        self.name = name
        self.currRoundScore = currRoundScore
        self.totalScore = totalScore
        self.rollsMade = rollsMade
        self.longestStreak = longestStreak
        self.favNumber = favNumber

    def setName(self, name):
        self.name = name

    def addCurrToTotal(self):
        self.totalScore += self.currRoundScore

    def resetCurrentScore(self):
        self.currRoundScore = 0
