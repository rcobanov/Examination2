import game
import highscore

# ----------------------------- OCD dagboken --------------------------------------------------------------------
# KLART - Lägga till restart och quit i Multiplayer
# KLART - Gör så att P2 kan vinna i Multiplayer 
# KLART - Försök göra så att p1 och p2 ser likadant ut i Multiplayer
# KLART - (kommer du på en snyggare lösning så ändra gärna) Skriva nåt cheat, kanske en cheat_dice eller liknande som ges till spelaren när man skrivit in
# städa upp game gui så de blir enkelt och tydligt att följa spelet när man spelar snabbt
# Lägg till felhantering för inputfel
# KLART ( men blev inte bra så tog bort, tror vi skiter i denna) - Lägg till metod för Win 
# KLART - Ta bort fav number från player
# Ändra Main menu till textblock
# Börja skriva resterande tester
#   KLART - bot_test
#   KLART - player_test (ändra round testet för att testa is_cheating)
#   game_test
#   dice_test
#   highscore_test
# KLART - används is_holding i bot? annars ta bort


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
      print("Write rosebud in the botgame to activate cheat")
    elif choice == 6:
      play = False



if __name__ == "__main__":
    main()
