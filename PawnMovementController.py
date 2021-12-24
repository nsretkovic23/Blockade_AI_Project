from os import error

def getPawnsCurrentPosition(pawn:str, state):
    if(pawn == "X1"):
        return state.x1Pos
    elif(pawn == "X2"):
        return state.x2Pos
    elif(pawn == "O1"):
        return state.o1Pos
    elif(pawn == "O2"):
        return state.o2Pos
    else:
        #Should never execute
        error("Wrong pawn")

def setNewPawnPosition(pawn:str, state, position:list):
    if(pawn == "X1"):
        state.x1Pos = position
    elif(pawn == "X2"):
        state.x2Pos = position
    elif(pawn == "O1"):
        state.o1Pos = position
    elif(pawn == "O2"):
        state.o2Pos = position
    else:
        #Should never execute
        error("Wrong pawn")

# TODO: Check if there are walls on the way!
def canPawnMoveThere(pawnCurrentPosition, row, column):
    if((   pawnCurrentPosition[0]     == row and pawnCurrentPosition[1]+2 == column)
       or (pawnCurrentPosition[0]     == row and pawnCurrentPosition[1]-2 == column)
       or (pawnCurrentPosition[0] + 2 == row and pawnCurrentPosition[1]   == column)
       or (pawnCurrentPosition[0] - 2 == row and pawnCurrentPosition[1]   == column)
       or (pawnCurrentPosition[0] + 1 == row and pawnCurrentPosition[1]+1 == column)
       or (pawnCurrentPosition[0] + 1 == row and pawnCurrentPosition[1]-1 == column)
       or (pawnCurrentPosition[0] - 1 == row and pawnCurrentPosition[1]-1 == column)
       or (pawnCurrentPosition[0] - 1 == row and pawnCurrentPosition[1]+1 == column)):

       return True
    else:
        return False

# TODO: Fix logic for marking starting positions because when pawn is returning to its start pos, it is being overwriten with XS/OS 
# Call this function to set starting positions to XS / OS if pawn moved from it's starting pos
def markStartingPosition(pawn, currentPosition:list, state):
    if(pawn == "X1"):
        if(state.x1StartingPos != currentPosition or state.x1StartingPos == state.x1Pos):
            state.playingFields[state.x1StartingPos[0]][state.x1StartingPos[1]] = "XS"
    elif(pawn == "X2"):
        if(state.x2StartingPos != currentPosition or state.x2StartingPos == state.x2Pos):
            state.playingFields[state.x2StartingPos[0]][state.x2StartingPos[1]] = "XS"
    elif(pawn == "O1"):
        if(state.o1StartingPos != currentPosition or state.o1StartingPos == state.o1Pos):
            state.playingFields[state.o1StartingPos[0]][state.o1StartingPos[1]] = "OS"
    elif(pawn == "O2"):
        if(state.o2StartingPos != currentPosition or state.o2StartingPos == state.o2Pos):
            state.playingFields[state.o2StartingPos[0]][state.o2StartingPos[1]] = "OS"