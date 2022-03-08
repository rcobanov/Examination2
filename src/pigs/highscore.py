"""We have two functions in this class.
one to collect data from the winner and store in a text file,
and one to print this data on a scoreboard."""

class Highscore():
    """Highscore class."""

    def show_score_board(self, filename):
        """Read textfile, format the data to display the scores."""
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
            print("    Name:           Total Score:    Longest Streak:")
            for score in all_scores:
                print(f"{position:>2}: {score[0]:15} {score[1]:<15} {score[2]}")
                position = position + 1

    def collect_score(self, name, score, longeststreak, filename):
        """Writing score from winning player to textfile."""
        with open(filename, "a") as file:
            file.write(name + ";" + str(score) + ";" + str(longeststreak) + "\n")
