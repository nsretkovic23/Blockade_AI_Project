from os import error
from NewGameGenerator import CreateNewGame

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
            playingFields[oPos[i%2][0]][oPos[i%2][1]] = f"O{i+1}"

# TODO: Move: checkIfCanMove, checkIfCanPlaceWall
# Format: [["X1"], [5,7], ["h", 3,4]]
def playTurn(state:GameState, turn):
    currentPosition = []
    if(turn[0][0] == "X1"):
        currentPosition = state.x1Pos
    elif(turn[0][0] == "X2"):
        currentPosition = state.x2Pos
    elif(turn[0][0] == "O1"):
        currentPosition = state.o1Pos
    elif(turn[0][0] == "O2"):
        currentPosition = state.o2Pos
    else:
        error("Wrong pawn")
    state.playingFields[currentPosition[0]][currentPosition[1]] = "  "

    state.playingFields[turn[1][0]][turn[1][1]] = turn[0][0]

    # TODO: Needs only one more check if there is a wall
    if(turn[2][0] == "h" and turn[2][1] > 0 and turn[2][1] <= state.rows and turn[2][2] < state.cols-1 and turn[2][2] > 0):
        state.hWalls[turn[2][1]][turn[2][2]] = "=="
        state.hWalls[turn[2][1]][turn[2][2]+1] = "=="

# TODO: Implement checkers to give an error before it goes to playTurn
#       Rename this to playTurn and playTurn to Execute Turn
def serializeTurn():
    move = []
    player = ""
    wall = []

    while(player != "X1" and player != "X2" and player != "O1" and player != "O2"):
        player = input("Select player: ")

    # TODO: Checkers if out of row/col
    row = int(input("Select row: "))
    column = int(input("Select column: "))
    move = [row, column]
    # TODO: Check if has walls left
    wall.append(input("Select wall, Type v/h : ").lower())
    wall.append(int(input("Select wall's starting row: ")))
    wall.append(int(input("Select wall's starting column: ")))
    return [[player], move, wall]