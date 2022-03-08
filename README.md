Python development environment
===============================

Terminal game program for object oriented Python with static code analyses, unit tests and documentation tools.
===============================

"Your project should contain a README.md that provides a description of the project and an instruction on how to install and run the game."
-----

"Your README.md should contain a section on how to run the complete testsuite and how to get the coverage report."
-----

## How one can generate the documentation from your code:

Open PowerShell as admin and write:  
*choco install graphviz*

Open the pigs folder in git bash.

To generate documentation:  
*make pdoc*

html files and uml diagrams is created in src/pigs/doc/.  
You can open all files generated in doc with your web browser.

## How to generate the UML diagrams of the documentation:

Open PowerShell as admin and write:  
*choco install graphviz*

Open the pigs folder in git bash.

To generate UML diagram:  
*make pyreverse*

To generate documenation and UML diagram:  
*make pdoc pyreverse*

html files and uml diagrams is created in src/pigs/doc/.  
You can open all files generated in doc with your web browser.

## Short explanation of each class in pigs:

highscore.py - We have two functions in this class, one to collect data from the winner and store in a text file and one to print this data on a scoreboard.

dice.py - This class can create a dice object that can be rolled and get a value between 1-6.

player.py - This is the heart of our program; this class can manipulate various data on the specific player. It also contains two functions that gives the player game control, one that runs every time the player rolls the dice, and one that contains the entire round. From when the player starts rolling until they choose hold.

bot.py - Here is the class that controls the bot that also contains various value manipulation and one function that lets the bot play one round, from first roll until hold. The intelligence is basically how many rolls the bot is going to do on one round. the easier level on the bot rolls so many times that its statistically is going to roll a one, the hardest level rolls lesser times to statistically hold before they’re rolling a one.
