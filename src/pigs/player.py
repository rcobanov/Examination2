import dice

class Player():

    is_holding = False
    is_cheating = False
    is_quitting = False

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

    def reset_scores(self):
        self.curr_round_score = 0
        self.total_score = 0
        self.rolls_made = 0
        self.longest_streak = 0
        self.fav_number = 0

    def player_roll(self, die):
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
            die.this_roll = 6
            self.curr_round_score += cheat_dice
            print(f"{self.name} - The dice shows {cheat_dice}")
            print(f"{self.name} - Current round score {self.curr_round_score}")
            print(f"{self.name} - Total score {self.total_score}")
            self.rolls_made += 1

    def play_round(self, other_player, die, choice):
        print("Quit(q) to end game and restart to restart the game")
        #choice = input(f"{self.name} - write roll to continue and hold to save score: ")
        if choice == "hold" or choice == "h":
            self.is_holding = True
            other_player.is_holding = False
        elif choice == "roll" or choice == "r":
            self.player_roll(die)
            if die.this_roll == 1:
                other_player.is_holding = False
        elif choice == "restart":
            self.reset_scores()
            other_player.reset_scores()
        elif choice == "rosebud":
            self.is_cheating = True
        elif choice == "quit":
            self.is_quitting = True
        else:
            print("That is not a valid input. Try again.")
        if self.is_holding is True:
            if self.rolls_made > self.longest_streak:
                self.longest_streak = self.rolls_made
            self.rolls_made = 0
            self.add_curr_to_total()
            self.reset_current_score()

