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
            