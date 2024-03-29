from UIController import clearConsole, printGameMatrix
from GameManager import GameState, getBeginningState, exectuteTurn, isGameOver, playTurn
from External_Packages.ColorizeText import colored
from Cheats import loadDefaultGameplay

whoPlaysFirst = ""
numberOfWalls = 0
rows = 0
cols = 0
xPositions = []
oPositions = []
positionInput = 0

clearConsole()


# CHEAT - LOAD GAME WITH DEFAULT SETTINGS INSTANTLY FOR TESTING
#defaultGame = loadDefaultGameplay()
#printGameMatrix(defaultGame)
#
#while(True):
#    turn = playTurn(defaultGame)
#    exectuteTurn(defaultGame, turn)
#    printGameMatrix(defaultGame)



print(colored("\n-----------------------------------", 'red', attrs=['bold']))
print(colored(" Welcome to the BLOCKADE GAME!", 'red', attrs=['bold']))
print(colored("-----------------------------------\n", 'red', attrs=['bold']))

while(whoPlaysFirst != 'me' and whoPlaysFirst !='cpu'):
    whoPlaysFirst = input(colored("Who do you want to play first? Type me/cpu: ", 'cyan')).lower()

print(colored("\nLet's create the table!", 'yellow')) 
print(" Tip: Recommended dimensions are 14x11\n Rule: Max dimensions are 28x22, Minimum dimensions are 10x8!\n")
while(rows < 10 or rows > 28):
    try:
        rows = int(input(colored("Enter the number of rows: ", 'cyan')))
    except:
        print(colored("Invalid input", 'red', attrs=['bold']))

while(cols < 8 or cols > 22):
    try:
        cols = int(input(colored("Enter the number of columns: ", 'cyan')))
    except:
        print(colored("Invalid input", 'red', attrs=['bold']))

print(colored("\nGood choice! Let's choose the number of walls!", 'yellow'))
print(" Tip: Recommended number is 9\n Rule: Maximum is 18, Minimum is 5!\n")

while(numberOfWalls < 5 or numberOfWalls > 18):
    try:
        numberOfWalls = int(input(colored("Enter number of walls: ", 'cyan')))
    except:
        print(colored("Invalid input", 'red', attrs=['bold']))

print(colored("\nGreat! Now let's set starting positions!", 'yellow'))

for i in range (0,4):
    while(positionInput < 1 or positionInput > rows):
        if(i < 2):
            asciiToNumber = ord(input(colored(f"X{i%2 + 1} row: ", 'cyan')).upper())
            positionInput = asciiToNumber - 48 if (asciiToNumber < 58) else asciiToNumber - 55
            #positionInput = int(input(colored(f"X{i%2 + 1} row: ", 'cyan')))
            if(positionInput > 0 and positionInput <= rows):
                xPositions.append([positionInput])
        else:
            asciiToNumber = ord(input(colored(f"O{i%2 + 1} row: ", 'cyan')).upper())
            positionInput = asciiToNumber - 48 if (asciiToNumber < 58) else asciiToNumber - 55
            #positionInput = int(input(colored(f"O{i%2 + 1} row: ", 'cyan')))
            if(positionInput > 0 and positionInput <= rows):
                oPositions.append([positionInput])
    positionInput = 0
    while(positionInput < 1 or positionInput > cols):
        if(i<2):
            asciiToNumber = ord(input(colored(f"X{i%2 + 1} column: ", 'cyan')).upper())
            positionInput = asciiToNumber - 48 if (asciiToNumber < 58) else asciiToNumber - 55
            #positionInput = int(input(colored(f"X{i%2 + 1} column: ", 'cyan')))
            if(positionInput > 0 and positionInput <= cols):
                xPositions[i].append(positionInput)
        else:
            asciiToNumber = ord(input(colored(f"O{i%2 + 1} column: ", 'cyan')).upper())
            positionInput = asciiToNumber - 48 if (asciiToNumber < 58) else asciiToNumber - 55
            #positionInput = int(input(colored(f"O{i%2 + 1} column: ", 'cyan')))
            if(positionInput > 0 and positionInput <= cols):
                oPositions[i%2].append(positionInput)
    positionInput = 0

state = getBeginningState(whoPlaysFirst, numberOfWalls, rows, cols, xPositions, oPositions)

printGameMatrix(state)

while(isGameOver(state) == False):
    turn = playTurn(state)
    exectuteTurn(state, turn)
    printGameMatrix(state)

