# from multiprocessing.sharedctypes import Value
import game
import highscore
import player
import dice
import bot

# ----------------------------- OCD dagboken --------------------------------------------------------------------

# städa upp game gui så de blir enkelt och tydligt att följa spelet när man spelar snabbt
#   placeringen på "print("Enter quit(q) to end game and restart to restart the game")" känns fel
#   när jag ändrade main menu till textblock så blev det en newline överst varje gång den printas
# STARTED - Lägg till felhantering för inputfel
# Börja skriva resterande tester
#   KLART - bot_test
#   KLART - player_test (ändra round testet för att testa is_cheating)
#   game_test
#   KLART - dice_test
#   highscore_test


def main():
    """Main function of this program."""
    play = True
    choice: int = 0
    die = dice.Dice()
    hs = highscore.Highscore()
    while play:
        main_menu()
        try:
            choice = int(input("Make a choice: "))
        except ValueError:
            print("Please input a number from the main menu options.")
            choice = 0
        if choice == 1:
            name = input("Enter the player name: ")
            print("Enter a bot level: 1 = Easy, 2 = Medium, 3 = Hard")
            bot_level = int(input("Bot Level: "))
            p1 = player.Player(name, 0, 0, 0, 0)
            anna = bot.Bot(0, 0, bot_level)

            while p1.total_score <= 100 and anna.total_score <= 100:
                if p1.is_holding is False:
                    choice = input(f"{p1.name} - write roll to continue and hold to save score: ")
                    p1.play_round(anna, die, choice)
                if anna.is_holding is False:
                    anna.bot_round(die)
                    p1.is_holding = False
                if p1.total_score >= 100 or p1.is_quitting is True or anna.total_score >= 100:
                    break

            if p1.total_score >= 100:
                print(f"Congratulations {p1.name}, you beat the bot. Your longest streak was {p1.longest_streak}")
                hs.collect_score(p1.name, p1.total_score, p1.longest_streak)
            elif anna.total_score >= 100:
                print("Oh no! The bot won :(")
            
        elif choice == 2:
            p1name = input("Enter player 1 name: ")
            p2name = input("Enter player 2 name: ")
            p1 = player.Player(p1name, 0, 0, 0, 0)
            p2 = player.Player(p2name, 0, 0, 0, 0)
            p2.is_holding = True

            while p1.total_score <= 100 and p2.total_score <= 100:
                if p1.is_holding is False:
                    choice = input(f"{p1.name} - write roll to continue and hold to save score: ")
                    p1.play_round(p2, die, choice)
                    if p1.total_score >= 100 or p1.is_quitting is True:
                        break
                if p2.is_holding is False:
                    choice = input(f"{p2.name} - write roll to continue and hold to save score: ")
                    p2.play_round(p1, die, choice)
                    if p2.total_score >= 100 or p2.is_quitting is True:
                        break

            if p1.total_score >= 100:
                print(f"Congratulations {p1.name}, you beat {p2.name}. Your longest streak was {p1.longest_streak}")
                hs.collect_score(p1.name, p1.total_score, p1.longest_streak)
            elif p2.total_score >= 100:
                print(f"Congratulations {p2.name}, you beat {p1.name}. Your longest streak was {p2.longest_streak}")
                hs.collect_score(p2.name, p2.total_score, p2.longest_streak)
        elif choice == 3:
            hs.show_score_board()
        elif choice == 4:
            display_rules()
        elif choice == 5:
            print("Write rosebud in the ingame to activate cheat")
        elif choice == 6:
            play = False

def main_menu():
    """Display of main menu."""
    print("""
---------------------
Welcome to Pigs!
1. Play against a bot
2. Play multiplayer
3. Show highscore table
4. Show game rules
5. Cheat
Q. Quit
---------------------""")

def display_rules():
    """Display the rules for the game pigs"""
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

if __name__ == "__main__":
    main()
