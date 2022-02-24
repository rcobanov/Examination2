import game
import highscore
# välkommen till råttboet chiefen!
# Tror inte det är lönt att du utgår från mina import, har nog kladdat bort allt som var värdefullt där,
# Samma när jag kallar på startPigs


def main():
    #hs = highscore.Highscore()
    #hs.showScoreBoard()
    game.Game.displayRule()
    name = input("Enter the player name: ")
    game.Game.startPigs(name, "roll")


if __name__ == "__main__":
    main()
