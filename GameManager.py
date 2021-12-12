from External_Packages.ColorizeText import colored
from NewGameGenerator import CreateNewGame
from PawnMovementController import setNewPawnPosition, getPawnsCurrentPosition, markStartingPosition, canPawnMoveThere

class GameState:
     def __init__(self):
       self.playerSign = ""
       self.cpuSign = ""
       self.player_H_Walls = 0
       self.player_V_Walls = 0
       self.cpu_H_Walls = 0
       self.cpu_V_Walls = 0
       self.rows = 0
       self.cols = 0
       self.playingFields = []
       self.hWalls = []
       self.vWalls = []
       self.x1StartingPos = []
       self.x2StartingPos = []
       self.o1StartingPos = []
       self.o2StartingPos = []
       self.x1Pos = []
       self.x2Pos = []
       self.o1Pos = []
       self.o2Pos = []
    

def getBeginningState(whoPlaysFirst, numberOfWalls, rows, cols, xPos, oPos):
    state = GameState()
    state.playerSign = "X" if whoPlaysFirst == "me" else "O"
    state.cpuSign = "X" if whoPlaysFirst == "cpu" else "O"
    state.player_H_Walls  = numberOfWalls
    state.player_V_Walls = numberOfWalls
    state.cpu_H_Walls = numberOfWalls
    state.cpu_V_Walls = numberOfWalls
    state.rows = rows
    state.cols = cols
    matrices = CreateNewGame(rows, cols)
    state.playingFields = matrices[0]
    state.hWalls = matrices[1]
    state.vWalls = matrices[2]
    state.x1StartingPos = xPos[0]
    state.x2StartingPos = xPos[1]
    state.o1StartingPos = oPos[0]
    state.o2StartingPos = oPos[1]
    state.x1Pos = xPos[0]
    state.x2Pos = xPos[1]
    state.o1Pos = oPos[0]
    state.o2Pos = oPos[1]

    setPawnsOnStartingPositions(state.playingFields, [state.x1StartingPos, state.x2StartingPos], [state.o1StartingPos, state.o2StartingPos])
    return state

def setPawnsOnStartingPositions(playingFields, xPos, oPos):
    for i in range(0,4):
        if(i < 2):
            playingFields[xPos[i][0]][xPos[i][1]] = f"X{i+1}"
        else:
            playingFields[oPos[i%2][0]][oPos[i%2][1]] = f"O{i%2+1}"

def playTurn(state:GameState):
    move = []
    player = ""
    pawnCurrentPosition = []
    wall = []
    isMoveValid = False
    isWallValid = False
    isFirstInputDoneAlready = False
    row = 0
    column = 0

    while(player != "X1" and player != "X2" and player != "O1" and player != "O2"):
        player = input("Select player: ")

    while(isMoveValid is False):
        if(row < 1 or row > state.rows):
            if isFirstInputDoneAlready is True:
                print(colored("Wrong positions, try again!", 'red'))

            asciiToNumber = ord(input(colored("Select row: ", 'cyan')).upper())
            row = asciiToNumber - 48 if (asciiToNumber < 58) else asciiToNumber - 55
            
            isFirstInputDoneAlready = True
        else:
            move.append(row)

        if(column < 1 or column > state.cols):
           
            asciiToNumber = ord(input(colored("Select column: ", 'cyan')).upper())
            column = asciiToNumber - 48 if (asciiToNumber < 58) else asciiToNumber - 55
        
        else:
            move.append(column)
            # Assume that move is valid because cols and rows are in dimensions range:
            isMoveValid = True


        pawnCurrentPosition = getPawnsCurrentPosition(player, state)

        if isMoveValid is True:
            if canPawnMoveThere(pawnCurrentPosition, row, column) is True:
                isMoveValid = True
            else:
                print(colored("You can't move there, try again!", 'red', attrs=['bold']))
                isMoveValid = False
                row = 0
                column = 0

    # TODO: Check if has walls left
    wall.append(input("Select wall, Type v/h : ").lower())
    wall.append(int(input("Select wall's starting row: ")))
    wall.append(int(input("Select wall's starting column: ")))
    return [[player], move, wall]


def exectuteTurn(state:GameState, turn):
    currentPosition = getPawnsCurrentPosition(turn[0][0], state)

    state.playingFields[currentPosition[0]][currentPosition[1]] = "  "

    state.playingFields[turn[1][0]][turn[1][1]] = turn[0][0]

    #Check if pawn moved from STARTING and set to XX / OO
    markStartingPosition(turn[0][0], currentPosition, state)

    setNewPawnPosition(turn[0][0], state, turn[1])

    # TODO: Needs only one more check if there is a wall
    if(turn[2][0] == "h"):
        state.hWalls[turn[2][1]][turn[2][2]] = "=="
        state.hWalls[turn[2][1]][turn[2][2]+1] = "=="

