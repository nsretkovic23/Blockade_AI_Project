import os
#from termcolor import colored
from External_Packages.ColorizeText import colored


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def printGameMatrix(state):
  h_Wals =""
  fields_and_V_Wals = ""
  h_fieldNumbers = " "
  for i in range(0, state.rows+1):
    for j in range(0, state.cols+1):
      # Stampaj samo = = = za gornju ivicu
      if(i == 0):
        if(j < state.cols):
          h_fieldNumbers+= str(j+1) if (j+1 < 10) else str(chr(65+j-9))
          h_fieldNumbers+= "  "
        #h_Wals += hWalls[i][j] +" "
        h_Wals += state.hWalls[i][j] if state.hWalls[i][j] == "--" else colored(state.hWalls[i][j], 'green')
        h_Wals += " " 
      if(i > 0):
        #fields_and_V_Wals += playerFields[i][j] + vWalls[i][j]
        playerColored = ""
        if "X" in state.playingFields[i][j]:
          playerColored = colored(state.playingFields[i][j], 'red', attrs=['bold'])
        elif "O" in state.playingFields[i][j]:
          playerColored = colored(state.playingFields[i][j], 'yellow', attrs=['bold'])
        else:
          playerColored = state.playingFields[i][j]
        fields_and_V_Wals += playerColored
        fields_and_V_Wals += state.vWalls[i][j] if state.vWalls[i][j] == "|" else colored(state.vWalls[i][j], 'blue')
        #h_Wals +=hWalls[i][j] + " "
        h_Wals += state.hWalls[i][j] if state.hWalls[i][j] == "--" else colored(state.hWalls[i][j], 'green')
        h_Wals += " " 
    if(j == state.cols):
      fields_and_V_Wals += " "
      fields_and_V_Wals += str(i) if (i < 10) else str(chr(65+i-10))
    if(i==0):
      print(h_fieldNumbers)
      print(colored(h_Wals))
    else:
      print(fields_and_V_Wals)
      print(h_Wals)
    fields_and_V_Wals = ""
    h_Wals = ""
