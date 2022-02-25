import game
import highscore
# nu är detta en OCDS människa värsta mardröm(eller är det himmelriket?)
# lite som behövs kikas på:
# i game vore det snyggt att städa genom att skapa metoder på player/bot istället för att skriva ut allt.(t.ex displayScore kanske, eller playOneRound för bot?
# snygga till helt enkelt, blir en del DRY i Game

def main_menu():
  print("---------------------")
  print("Welcome to Pigs!")
  print("1. Play against a bot")
  print("2. Play multiplayer")
  print("3. Show highscore table")
  print("4. Show game rules")
  print("5. Cheat")
  print("6. Quit")
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
      player1 = input("Enter player 1 name: ")
      player2 = input("Enter player 2 name: ")
      game.Game.startMultiplayerPigs(player1, player2)
    elif choice == 3:
      highscore.Highscore().showScoreBoard()
    elif choice == 4:
      game.Game.displayRule()
    elif choice == 5:
      print("Cheats have not yet been developed")
    elif choice == 6:
      play = False



if __name__ == "__main__":
    main()
