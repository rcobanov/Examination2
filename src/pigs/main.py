import game
import highscore
# välkommen till råttboet chiefen!
# Tror inte det är lönt att du utgår från mina import, har nog kladdat bort allt som var värdefullt där,
# Samma när jag kallar på startPigs

def main_menu():
  print("---------------------")
  print("Welcome to Pigs!")
  print("1. Play against a bot")
  print("2. Play multiplayer")
  print("3. Show game rules")
  print("4. Cheat")
  print("5. Quit")
  print("---------------------")

def main():
  play = True
  while play:
    main_menu()
    choice = int(input("Make a choice: "))
    if choice == 1:
      name = input("Enter the player name: ")
      game.Game.startPigs(name, "roll")
    elif choice == 2:
      print("That feature is a work in progress!")
    elif choice == 3:
      game.Game.displayRule()
    elif choice == 4:
      print("Cheats have not yet been developed")
    elif choice == 5:
      play = False
  #hs = highscore.Highscore()
  #hs.showScoreBoard()
  

  


if __name__ == "__main__":
    main()
