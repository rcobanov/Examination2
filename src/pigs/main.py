import game
import dice
import player
# välkommen till råttboet chiefen!
# Tror inte det är lönt att du utgår från mina import, har nog kladdat bort allt som var värdefullt där,
# Samma när jag kallar på startPigs


def main():
    game.Game.displayRule()
    game.Game.startPigs()

if __name__ == "__main__":
    main()