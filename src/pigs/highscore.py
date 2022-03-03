class Highscore():
    """Highscore class."""

    def show_score_board(self, filename):
        """Reading textfile and formatting the data to display the scoreboard."""
        with open(filename, "r") as file:
            print("{:*^50}".format(" HIGHSCORE TABLE "))
            data = file.readlines()
            all_scores = []
            for line in data:
                name, total, streak = line.split(";")
                score = (name, int(total), streak.rstrip())
                all_scores.append(score)
            all_scores.sort(key=lambda y: y[1], reverse=True)
            position = 1
            print(f"   Name:           Total Score:    Longest Streak:")
            for score in all_scores:
                print(f"{position}: {score[0]:15} {score[1]:<15} {score[2]}")
                position = position + 1

    def collect_score(self, name, score, longeststreak, filename):
        """Writing score from winning player to textfile."""
        with open(filename, "a") as file:
            file.write(name + ";" + str(score) + ";" + str(longeststreak) + "\n")
