class Highscore():

    def showScoreBoard(self):
        with open("highscores.txt", "r") as file:
            print("{:*^50}".format(" HIGHSCORE TABLE "))
            scores = file.readlines()
            list = []
            for line in scores:
                name, total, streak = line.split(";")
                myTuple = (name, int(total), streak.rstrip())
                list.append(myTuple)
            list.sort(key=lambda y: y[1], reverse=True)
            i = 0
            position = 1
            print(f"   Name:           Total Score:    Longest Streak:")
            for score in list:
                print(f"{position}: {score[i]:15} {score[i+1]:<15} {score[i+2]}")
                position = position + 1

    def collectScore(self, name, score, longeststreak):
        with open("highscores.txt", "a") as file:
            file.write(name + ";" + str(score) + ";" + str(longeststreak) + "\n")
