# Terminal game for object oriented Python with static code analyses, unit tests and documentation tools.

## How to install and run the game:

1. Unzip game.zip
2. Start your cmd
3. Change directory to ../Examination2/src/pigs
4. Write python main.py
5. Enjoy!

## Short explanation of each class in pigs:

**highscore.py** - We have two functions in this class, one to collect data from the winner and store in a text file and one to print this data on a scoreboard.

**dice.py** - This class can create a dice object that can be rolled and get a value between 1-6.

**player.py** - This is the heart of our program; this class can manipulate various data on the specific player. It also contains two functions that gives the player game control, one that runs every time the player rolls the dice, and one that contains the entire round. From when the player starts rolling until they choose hold.

**bot.py** - Here is the class that controls the bot that also contains various value manipulation and one function that lets the bot play one round, from first roll until hold. The intelligence is basically how many rolls the bot is going to do on one round. the easier level on the bot rolls so many times that its statistically is going to roll a one, the hardest level rolls lesser times to statistically hold before they’re rolling a one.

## Creating the virtual testenviroment:

Install package manager Chocolatey:  
https://chocolatey.org/install

Open the Examination2 folder in git bash. 

Creating the base for your virtual enviroment:  
*make venv*

Activate enviroment:  
*. .venv/Scripts/activate*

Installing all packages from requirments.txt:  
*make install*

## How to run the complete testsuite:

Open Examination2/src/pigs in git bash. 

Testing pylint:  
*make pylint*

Testing flake8:
*make flake8*

Testing both:  
*make lint*

Testing unittest:  
*make unittest*

Getting coverage report:  
*make coverage*

Test all of the above:  
*make test*

## How one can generate the documentation from your code:  

Open PowerShell as admin and write:  
*choco install graphviz*

Open ../Examination2/src/pigs in git bash.

To generate documentation:  
*make pdoc*

html files and uml diagrams is created in src/pigs/doc/*.  
You can open all files generated in doc with your web browser.

## How to generate the UML diagrams of the documentation:

Open PowerShell as admin and write:  
*choco install graphviz*

Open ../Examination2/src/pigs in git bash.

To generate UML diagram:  
*make pyreverse*

To generate documenation and UML diagram:  
*make pdoc pyreverse*

html files and uml diagrams is created in src/pigs/doc/*.  
You can open all files generated in doc with your web browser.
