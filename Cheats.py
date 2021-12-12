from GameManager import GameState, getBeginningState

def loadDefaultGameplay():
    state = getBeginningState("me", 
                                9,
                                14,
                                11,
                                [[11,4],[11,8]],
                                [[4,4],[4,8]])
    return state
    
    