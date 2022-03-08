#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main holds the logic for the menu, and also the game loop."""

import highscore
import player
import dice
import bot


def main():
    """Menu control and game loop."""
    play = True
    die = dice.Dice()
    score_board = highscore.Highscore()
    while play:
        main_menu()
        choice = input("Make a choice: ")
        if choice == "1":
            name = input("Enter the player name: ")
            if name == "":
                name = "Anonymous"
            print("Enter a bot level: 1 = Easy, 2 = Medium, 3 = Hard")
            while True:
                bot_level = input("Bot Level: ")
                try:
                    bot_level = int(bot_level)
                except ValueError:
                    print("Must enter a number.")
                    continue
                if 1 <= bot_level <= 3:
                    break
            player_1 = player.Player(name, 0, 0, 0, 0)
            anna = bot.Bot(0, 0, bot_level)

            while player_1.total_score <= 100 and anna.total_score <= 100:
                if player_1.is_holding is False:
                    print("Enter quit(q) to end game and " +
                          "restart to restart the game")
                    choice = input(f"{player_1.name} - write roll(r) to " +
                                   "continue and hold(h) to save score: ")
                    player_1.play_round(anna, die, choice)
                if anna.is_holding is False:
                    anna.bot_round(die)
                    player_1.is_holding = False
                if (player_1.total_score >= 100 or player_1.is_quitting is True
                        or anna.total_score >= 100):
                    break

            if player_1.total_score >= 100:
                print(f"Congratulations {player_1.name}, you beat the bot." +
                      f"Your longest streak was {player_1.longest_streak}")
                score_board.collect_score(player_1.name,
                                          player_1.total_score,
                                          player_1.longest_streak,
                                          "highscore.txt")
            elif anna.total_score >= 100:
                print("Oh no! The bot won :(")

        elif choice == "2":
            player_1_name = input("Enter player 1 name: ")
            if player_1_name == "":
                player_1_name = "Anonymous"
            player_2_name = input("Enter player 2 name: ")
            if player_2_name == "":
                player_2_name = "Anonymous"
            player_1 = player.Player(player_1_name, 0, 0, 0, 0)
            player_2 = player.Player(player_2_name, 0, 0, 0, 0)
            player_2.is_holding = True

            while player_1.total_score <= 100 and player_2.total_score <= 100:
                if player_1.is_holding is False:
                    choice = input(f"{player_1.name} - write roll to continue"
                                   + " and hold to save score: ")
                    player_1.play_round(player_2, die, choice)
                    if (player_1.total_score >= 100 or
                            player_1.is_quitting is True):
                        break
                if player_2.is_holding is False:
                    choice = input(f"{player_2.name} - write roll to continue"
                                   + "and hold to save score: ")
                    player_2.play_round(player_1, die, choice)
                    if (player_2.total_score >= 100 or
                            player_2.is_quitting is True):
                        break

            if player_1.total_score >= 100:
                print(f"Congratulations {player_1.name}, you beat " +
                      f"{player_2.name}. Your longest streak was " +
                      f"{player_1.longest_streak}")
                score_board.collect_score(player_1.name,
                                          player_1.total_score,
                                          player_1.longest_streak,
                                          "highscore.txt")
            elif player_2.total_score >= 100:
                print(f"Congratulations {player_2.name}, you beat " +
                      f"{player_1.name}. Your longest streak was " +
                      f"{player_2.longest_streak}")
                score_board.collect_score(player_2.name,
                                          player_2.total_score,
                                          player_2.longest_streak,
                                          "highscore.txt")
        elif choice == "3":
            score_board.show_score_board("highscore.txt")
        elif choice == "4":
            display_rules()
        elif choice == "5":
            print("Write rosebud in the ingame to activate cheat.")
        elif choice in ("q", "Q"):
            play = False
        else:
            print("That is not a valid choice")


def main_menu():
    """Display of main menu."""
    print("""---------------------
Welcome to Pigs!
1. Play against a bot
2. Play multiplayer
3. Show highscore table
4. Show game rules
5. Cheat
Q. Quit
---------------------""")


def display_rules():
    """Display the rules for the game pigs."""
    print("""
Each turn, a player repeatedly rolls a die until either a 1 is rolled or
the player decides to "hold". If the player rolls a 1, they score
nothing and it becomes the next player's turn. If the player rolls any
other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score,
and it becomes the next player's turn.

The first player to score 100 or more points wins.

For example, the first player, Donald, begins a turn with a roll of 5.
Donald could hold and score 5 points, but chooses to roll again.
Donald rolls a 2, and could hold with a turn total of 7 points,
but chooses to roll again. Donald rolls a 1, and must end his turn
without scoring. The next player, Alexis, rolls the sequence 4-5-3-5-5,
after which she chooses to hold, and adds her turn total of 22 points
to her score.""")


if __name__ == "__main__":
    main()
