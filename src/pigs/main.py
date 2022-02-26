import game
import highscore
# nu är detta en OCDS människa värsta mardröm(eller är det himmelriket?)
# lite som behövs kikas på:
# i game vore det snyggt att städa genom att skapa metoder på player/bot istället för att skriva ut allt.(t.ex displayScore kanske, eller playOneRound för bot?
# snygga till helt enkelt, blir en del DRY i Game


# ----------------------------- OCD dagboken --------------------------------------------------------------------
#  # printen på rules blir ej så snygg, tänkte om man kunde snygga till printen på main menu genom att bara ha
# ett print statement men klura jag ej ut de på rules så vetifan.

# Börja skriva resterande tester

# städa upp game gui så de blir enkelt och tydligt att följa spelet när man spelar snabbt

# skriva metod som samlar fav_number på varje spelare och skriver ut det i highscorestatistiken

# skriva nåt cheat, kanske en cheat_dice eller liknande som ges till spelaren när man skrivit in

# namnge boten?


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
