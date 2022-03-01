import dice
import player
import highscore
import bot


class Game():

    def startPigs(name, choice):
        print("Enter a bot level: 1 = Easy, 2 = Medium, 3 = Hard")
        bot_level = input("Bot Level: ")
        p1 = player.Player(name, 0, 0, 0, 0)
        die = dice.Dice()
        hs = highscore.Highscore()
        anna = bot.Bot(0, 0, bot_level)

        while p1.total_score <= 100 and anna.total_score <= 100:
            if p1.is_holding is False:
                print("Quit(q) to end game and restart to restart the game")
                choice = input("Write roll(r) to continue and hold(h) to save score: ")
                if choice == "hold" or choice == "h":
                    p1.is_holding = True
                elif choice == "roll" or choice == "r":
                    p1.player_round(die)
                elif choice == "restart":
                    p1.reset_player()
                    anna.reset_bot()
                elif choice == "rosebud":
                    p1.is_cheating = True
                elif choice == "quit" or choice == "q":
                    break
            elif p1.is_holding is True:
                if p1.rolls_made > p1.longest_streak:
                    p1.longest_streak = p1.rolls_made
                p1.rolls_made = 0
                p1.add_curr_to_total()
                p1.reset_current_score()
                anna.bot_round(die)
                p1.is_holding = False

        if p1.total_score >= 100:
            print(f"Congratulations {p1.name}, you beat the bot. Your longest streak was {p1.longest_streak}")
            hs.collectScore(p1.name, p1.total_score, p1.longest_streak)
        elif anna.total_score >= 100:
            print("Oh no! The bot won :(")
            
    def startMultiplayerPigs(p1name, p2name):
        p1 = player.Player(p1name, 0, 0, 0, 0)
        p2 = player.Player(p2name, 0, 0, 0, 0)
        die = dice.Dice()
        hs = highscore.Highscore()
        p2.is_holding = True

        while p1.total_score <= 100 and p2.total_score <= 100:
            if p1.is_holding is False:
                print("Quit(q) to end game and restart to restart the game")
                p1choice = input(f"{p1.name}s turn - Write roll to continue and hold to save score: ")
                if p1choice == "hold" or p1choice == "h":
                    p1.is_holding = True
                    p2.is_holding = False
                elif p1choice == "roll" or p1choice == "r":
                    p1.player_round(die)
                    if die.this_roll == 1:
                        p2.is_holding = False
                elif p1choice == "restart":
                    p1.reset_player()
                    p2.reset_player()
                elif p1choice == "quit":
                    break
            if p1.is_holding is True:
                if p1.rolls_made > p1.longest_streak:
                    p1.longest_streak = p1.rolls_made
                p1.rolls_made = 0
                p1.add_curr_to_total()
                p1.reset_current_score()
                if p1.total_score >= 100:
                    break
            if p2.is_holding is False:
                print("Quit(q) to end game and restart to restart the game")
                p2choice = input(f"{p2.name} - write roll to continue and hold to save score: ")
                if p2choice == "hold" or p2choice == "h":
                    p2.is_holding = True
                    p1.is_holding = False
                elif p2choice == "roll" or p2choice == "r":
                    p2.player_round(die)
                    if die.this_roll == 1:
                        p1.is_holding = False
                elif p2choice == "restart":
                    p1.reset_player()
                    p2.reset_player()
                elif p1choice == "quit":
                    break
            if p2.is_holding is True:
                if p2.rolls_made > p2.longest_streak:
                    p1.longest_streak = p1.rolls_made
                p2.rolls_made = 0
                p2.add_curr_to_total()
                p2.reset_current_score()
                if p2.total_score >= 100:
                    break


        if p1.total_score >= 100:
            print(f"Congratulations {p1.name}, you beat {p2.name}. Your longest streak was {p1.longest_streak}")
            hs.collectScore(p1.name, p1.total_score, p1.longest_streak)
        elif p2.total_score >= 100:
            print(f"Congratulations {p2.name}, you beat {p1.name}. Your longest streak was {p2.longest_streak}")
            hs.collectScore(p2.name, p2.total_score, p2.longest_streak)


    def displayRule():
        print("""
Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":
If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.

The first player to score 100 or more points wins.

For example, the first player, Donald, begins a turn with a roll of 5.
Donald could hold and score 5 points, but chooses to roll again. Donald rolls a 2,
and could hold with a turn total of 7 points, but chooses to roll again. Donald rolls a 1,
and must end his turn without scoring. The next player, Alexis, rolls the sequence 4-5-3-5-5,
after which she chooses to hold, and adds her turn total of 22 points to her score.""")
