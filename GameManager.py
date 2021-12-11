from NewGameGenerator import CreateNewGame

class GameManager:
    def __init__(self, playerSign, cpuSign, wallNumber,
     playingFields, hWalls, vWalls, rows, cols ):
        self.playerSign = playerSign
        self.cpuSign = cpuSign
        self.player_H_Walls = wallNumber
        self.player_V_Walls = wallNumber
        self.cpu_H_Walls = wallNumber
        self.cpu_V_Walls = wallNumber
        self.rows = rows
        self.cols = cols
        self.playingFields = playingFields
        self.hWalls = hWalls
        self.vWalls = vWalls

def GetBeginningState(whoPlaysFirst, numberOfWalls, rows, cols):
    state = GameManager()
    state.playerSign = "X" if whoPlaysFirst == "me" else "O"
    state.cpuSign = "X" if whoPlaysFirst == "cpu" else "O"
    state.player_H_Walls  = numberOfWalls
    state.player_V_Walls = numberOfWalls
    state.cpu_H_Walls = numberOfWalls
    state.cpu_V_Walls = numberOfWalls
    matrices = CreateNewGame(rows, cols)
    state.playingFields = matrices[0]
    state.hWalls = matrices[1]
    state.vWalls = matrices[2]

