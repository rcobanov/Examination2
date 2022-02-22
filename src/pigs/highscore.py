class Highscore():

    def showScoreBoard(self):
        with open("highscores.txt", "r") as file:
            print("****** HIGHSCORE TABLE ********")
            scores = file.readlines()
            scores.sort(key=lambda y: y.split(";")[1], reverse = True)      #Sortering av andra elementet funkar ej, nu sorterar den på bokstav 2 i omvänd ordning.
            for line in scores:
                name,total,streak = line.split(";")
                print(f"Name: {name:15} Total Score: {total:6} Longest Streak: {streak}")
    
    
    def collectScore(self, name, score, longeststreak):
        with open("highscores.txt", "a") as file:
            file.write(name + ";" + str(score) + ";" + str(longeststreak) + "\n")

        