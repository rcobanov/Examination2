class Bot():
    """Bot class."""

    is_holding = True

    def __init__(self, curr_round_score, total_score, level):
        """Initiate a bot object."""
        self.curr_round_score = curr_round_score
        self.total_score = total_score
        self.level = level

    def get_number_of_rounds(self, bot_level):
        """Get how many rounds bot should run based on level."""
        rounds_to_run = 0
        if bot_level == 1:
            rounds_to_run = 14
        elif bot_level == 2:
            rounds_to_run = 9
        elif bot_level == 3:
            rounds_to_run = 5
        return rounds_to_run

    def add_curr_to_total(self):
        """Add current score to total."""
        self.total_score += self.curr_round_score

    def reset_current_score(self):
        """Reset current score to zero."""
        self.curr_round_score = 0

    def bot_round(self, die):
        """One round for the bot."""
        rounds_to_run = self.get_number_of_rounds(int(self.level))
        for x in range(rounds_to_run):
            self.curr_round_score += die.roll()
            print(f"The bot dice shows {die.this_roll}")
            if die.this_roll == 1:
                self.reset_current_score()
                self.is_holding = True
                print("The bot rolled a 1!!")
                print("--------------------")
                break
        self.add_curr_to_total()
        self.reset_current_score()
        print(f"Current bot round score {self.curr_round_score}")
        print(f"Total bot score {self.total_score}")

    def reset_scores(self):
        """Sets all bot scores to zero"""
        self.curr_round_score = 0
        self.total_score = 0
