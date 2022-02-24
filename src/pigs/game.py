import dice
import player
import highscore
import bot


class Game():

    def startPigs(name, choice):
        print("Enter a bot level: 1 = Hard, 2 = Medium, 3 = Easy")
        botLevel = input("Bot Level: ")
        p1 = player.Player(name, 0, 0, 0, 0, 0)                                  # Skapa upp en spelare
        die = dice.Dice()                                                        # Skapa upp en tärning
        hs = highscore.Highscore()                                               # Skapa upp scoreboard
        boten = bot.Bot(0, 0, botLevel)                                          # Skapa upp en bot

        while p1.totalScore <= 100 and boten.totalScore <= 100:                      # Loopen för spelet
            if p1.isHolding is False:
                choice = input("Write roll to continue and hold to save score: ")    # Gamecontrol
                if choice == "hold":
                    p1.isHolding = True
                else:
                    p1.currRoundScore += die.roll()                                  # Uppdatera rundans poäng
                    print(f"The dice shows {die.thisRoll}")
                    print(f"Current round score {p1.currRoundScore}")
                    print(f"Total score {p1.totalScore}")
                    p1.rollsMade += 1                                                # Counter till tärningskast per runda
                    if die.thisRoll == 1:                                            # Hanterar när kastet visar 1
                        p1.currRoundScore = 1
                        p1.addCurrToTotal()
                        p1.resetCurrentScore()
                        print("Oh no, you rolled a 1!")
                        print("----------------------")
                        p1.isHolding = True
            elif p1.isHolding is True:
                if p1.rollsMade > p1.longestStreak:
                    p1.longestStreak = p1.rollsMade                              # Längsta rollsMade sparas
                p1.rollsMade = 0                                                 # Rolls nollställs till nästa runda
                p1.addCurrToTotal()                                              # Uppdatera totalpoängen
                p1.resetCurrentScore()                                           # Reseta inför nästa runda
                roundstoRun = boten.getNumberOfRounds(int(botLevel))
                for x in range(roundstoRun):
                    boten.currRoundScore += die.roll()
                    print(f"The bot dice shows {die.thisRoll}")
                    if die.thisRoll == 1:
                        boten.currRoundScore = 1
                        print("The bot rolled a 1!!")
                        print("--------------------")
                        break
                boten.addCurrToTotal()
                boten.resetCurrentScore()
                print(f"Current bot round score {boten.currRoundScore}")
                print(f"Total bot score {boten.totalScore}")
                p1.isHolding = False

        if p1.totalScore >= 100:
            print(f"Congratulations {p1.name}, you've won the game. Your longest streak was {p1.longestStreak}")
            hs.collectScore(p1.name, p1.totalScore, p1.longestStreak)             # Lägger till spelare i highscore
        elif boten.totalScore >= 100:
            print("Oh no! The bot won :(")

    def displayRule():
        print("""Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

            If the player rolls a 1, they score nothing and it becomes the next player's turn.
            If the player rolls any other number, it is added to their turn total and the player's turn continues.
            If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.

            The first player to score 100 or more points wins.

            For example, the first player, Donald, begins a turn with a roll of 5.
            Donald could hold and score 5 points, but chooses to roll again. Donald rolls a 2,
            and could hold with a turn total of 7 points, but chooses to roll again. Donald rolls a 1,
            and must end his turn without scoring. The next player, Alexis, rolls the sequence 4-5-3-5-5,
            after which she chooses to hold, and adds her turn total of 22 points to her score. """)
