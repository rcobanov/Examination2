Python development environment
===============================

Terminal game program for object oriented Python with static code analyses, unit tests and documentation tools.
===============================

"Your project should contain a README.md that provides a description of the project and an instruction on how to install and run the game."
===============================

"Your README.md should contain a section on how to run the complete testsuite and how to get the coverage report."
===============================

"You README.md should contain details on how one can regenerate the documentation from your code."

===============================

Document in your README.md on how to regenerate the UML diagrams of the documentation.

download extension to vscode called graphviz

Name: Graphviz (dot) language support for Visual Studio Code
Id: joaompinto.vscode-graphviz
Description: This extension provides GraphViz (dot) language support for Visual Studio Code
Version: 0.0.6
Publisher: João Pinto
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=joaompinto.vscode-graphviz

input in gitbash:
    install -d doc/pyreverse
    pyreverse *.py

enter the dot file in vscode and enter ctrl+shift+v

to remove dot files:
    rm -f classes.dot packages.dot
===============================

highscore.py - We have two functions in this class, one to collect data from the winner and store in a text file and one to print this data on a scoreboard.

dice.py - This class can create a dice object that can be rolled and get a value between 1-6.

player.py - This is the heart of our program; this class can manipulate various data on the specific player. It also contains two functions that gives the player game control, one that runs every time the player rolls the dice, and one that contains the entire round. From when the player starts rolling until they choose hold.

bot.py - Here is the class that controls the bot that also contains various value manipulation and one function that lets the bot play one round, from first roll until hold. The intelligence is basically how many rolls the bot is going to do on one round. the easier level on the bot rolls so many times that its statistically is going to roll a one, the hardest level rolls lesser times to statistically hold before they’re rolling a one.