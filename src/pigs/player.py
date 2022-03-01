import dice

class Player():

    is_holding = False
    is_cheating = False

    def __init__(self, name, curr_round_score, total_score, rolls_made, longest_streak):
        self.name = name
        self.curr_round_score = curr_round_score
        self.total_score = total_score
        self.rolls_made = rolls_made
        self.longest_streak = longest_streak

    def set_name(self, name):
        self.name = name

    def add_curr_to_total(self):
        self.total_score += self.curr_round_score

    def reset_current_score(self):
        self.curr_round_score = 0

    def reset_player(self):
        self.curr_round_score = 0
        self.total_score = 0
        self.rolls_made = 0
        self.longest_streak = 0
        self.fav_number = 0

    def player_round(self, die):
        if self.is_cheating == False:
            self.curr_round_score += die.roll()
            print(f"{self.name} - The dice shows {die.this_roll}")
            print(f"{self.name} - Current round score {self.curr_round_score}")
            print(f"{self.name} - Total score {self.total_score}")
            self.rolls_made += 1
            if die.this_roll == 1:
                self.reset_current_score()
                print(f"Oh no, {self.name} rolled a 1!")
                print("----------------------")
                self.is_holding = True
        else:
            cheat_dice = 6
            self.curr_round_score += cheat_dice
            print(f"{self.name} - The dice shows {cheat_dice}")
            print(f"{self.name} - Current round score {self.curr_round_score}")
            print(f"{self.name} - Total score {self.total_score}")
            self.rolls_made += 1



