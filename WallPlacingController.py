from External_Packages.ColorizeText import colored

#TODO: Phase 2 -> check if you are closing every path to a player

def tryToPlaceHorizontalWall(state, wallPos):
    if(state.hWalls[wallPos[0]][wallPos[1]] == "==" or state.hWalls[wallPos[0]][wallPos[1]+1] == "=="):
        print(colored("You can't place the wall here, try again!",'red', attrs=['bold']))
        return False
    else:
        state.hWalls[wallPos[0]][wallPos[1]] = "=="
        state.hWalls[wallPos[0]][wallPos[1]+1] = "=="
        return True

def tryToPlaceVerticalWall(state, wallPos):
    if(state.vWalls[wallPos[0]][wallPos[1]] == "\u01c1"
    or state.vWalls[wallPos[0]+1][wallPos[1]] == "\u01c1"):
        print(colored("You can't place the wall here, try again!",'red', attrs=['bold']))
        return False
    else:
        state.vWalls[wallPos[0]][wallPos[1]] = "\u01c1"
        state.vWalls[wallPos[0]+1][wallPos[1]] = "\u01c1"
        return True
