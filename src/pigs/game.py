import dice
import player


class Game():

    def startPigs(self):
        name = input("Enter your name: ")
        p1 = player.Player(name, 0, 0, 0, 0, 0)                                  # Skapa upp en spelare


        while p1.totalScore < 100:                                               # Loopen för spelet
            if p1.isHolding == False:
                p1.currRoundScore += dice.roll()                                 # Uppdatera rundans poäng
                p1.rollsMade += 1                                                # Counter till tärningskast per runda
                input = input("Write roll to continue and hold to save score: ") # Gamecontrol
                if input == "hold":
                    p1.isHolding = True
            elif p1.isHolding == True:
                if p1.rollsMade > p1.longestStreak:
                        p1.longestStreak = p1.rollsMade                          # Längsta rollsMade sparas
                p1.rollsMade = 0                                                 # Rolls nollställs till nästa runda
                p1.addCurrToTotal()                                              # Uppdatera totalpoängen
                p1.resetCurrentScore()                                           # Reseta inför nästa runda
                p1.isHolding = False

        
    
    def displayRules(self):
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