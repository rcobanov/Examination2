class Player():
    
    is_holding = False

    def __init__(self, name, curr_round_score, total_score, rolls_made, longest_streak, fav_number):
        self.name = name
        self.curr_round_score = curr_round_score
        self.total_score = total_score
        self.rolls_made = rolls_made
        self.longest_streak = longest_streak
        self.fav_number = fav_number

    def setName(self, name):
        self.name = name

    def addCurrToTotal(self):
        self.total_score += self.curr_round_score

    def resetCurrentScore(self):
        self.curr_round_score = 0
