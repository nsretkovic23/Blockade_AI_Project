
playerFields22 = [["",   "",   "",   "",  ""], #0
                  ["", "X1", "  ", "  ","  "], #1
                  ["", "  ", "  ", "  ","  "], #2
                  ["", "  ", "Y2", "  ","  "], #3
                  ["", "  ", "  ", "  ","  "]] #4

hWall1 = [
          ["", "==", "==", "==", "=="], #0
          ["", "--", "--", "--", "--"], #1
          ["", "--", "--", "--", "--"], #2
          ["", "--", "--", "--", "--"], #3
          ["", "==", "==", "==", "=="]] #4

vWall1 = [["",        "",  "",  "",       ""],
          ["\u01c1", "|", "|", "|", "\u01c1"],
          ["\u01c1", "|", "|", "|", "\u01c1"],
          ["\u01c1", "|", "|", "|", "\u01c1"],
          ["\u01c1", "|", "|", "|", "\u01c1"]]

# ROWS, COLS actual dimensions for a game
# MatrixRows/Cols dimensions that are suitable for drawing all matrices on the screen
def createPlayingFields(rows, cols):
  fields = []
  matrixRows = rows+1
  matrixCols = cols +1
  for i in range (0, matrixRows):
    fields.append([])
  for i in range (0, matrixRows):
    for j in range(0, matrixCols):
      if(i == 0):
        fields[i].append("")
      if(i > 0 and j ==0):
        fields[i].append("")
      if(i > 0 and j > 0):
        fields[i].append("  ")
  return fields



# ROWS, COLS actual dimensions for a game
# MatrixRows/Cols dimensions that are suitable for drawing all matrices on the screen
def createHorizontalWalls(rows, cols):
  horizontal_Walls = []
  matrixRows = rows+1
  matrixCols = cols +1
  for i in range (0, matrixRows):
    horizontal_Walls.append([])
  for i in range (0, matrixRows):
    for j in range(0, matrixCols):
      if(j == 0):
        horizontal_Walls[i].append("")
      if(i == 0 and j > 0):
        horizontal_Walls[i].append("==")
      if(i==rows and j>0):
        horizontal_Walls[i].append("==")
      if(i > 0 and j > 0 and i < rows):
        horizontal_Walls[i].append("--")
  return horizontal_Walls



# ROWS, COLS actual dimensions for a game
# MatrixRows/Cols dimensions that are suitable for drawing all matrices on the screen
def createVerticalWalls(rows, cols):
  vertical_Walls = []
  matrixRows = rows+1
  matrixCols = cols +1
  for i in range (0, matrixRows):
    vertical_Walls.append([])
  for i in range (0, matrixRows):
    for j in range(0, matrixCols):
      if(i == 0):
        vertical_Walls[i].append("")
      if((i > 0 and j == 0) or (i > 0 and j == cols)):
        vertical_Walls[i].append("\u01c1")
      if(i > 0):
        if(j > 0 and j < cols):
          vertical_Walls[i].append("|")
  return vertical_Walls

vWalls = createVerticalWalls(14,11)

hWalls = createHorizontalWalls(14,11)

playerFields = createPlayingFields(14,11)

playerFields[4][4] = "X1"
playerFields[4][8] = "X2"
playerFields[11][4] = "O1"
playerFields[11][8] = "O2"


#for i in range (0, 8):
#  print(playerFields[i])

#PRINT--------------------------------------
def printTable(rows, cols):
  h_Wals =""
  fields_and_V_Wals = ""
  h_fieldNumbers = " "
  for i in range(0, rows+1):
    for j in range(0, cols+1):
      # Stampaj samo = = = za gornju ivicu
      if(i == 0):
        if(j < cols):
          h_fieldNumbers+= str(j+1) if (j+1 < 10) else str(chr(65+j-9))
          h_fieldNumbers+= "  "
        h_Wals += hWalls[i][j] +" " 
      if(i > 0):
        fields_and_V_Wals += playerFields[i][j] + vWalls[i][j]
        h_Wals +=hWalls[i][j] + " "
    if(j == cols):
      fields_and_V_Wals += " "
      fields_and_V_Wals += str(i) if (i < 10) else str(chr(65+i-10))
    if(i==0):
      print(h_fieldNumbers)
      print(h_Wals)
    else:
      print(fields_and_V_Wals)
      print(h_Wals)
    fields_and_V_Wals = ""
    h_Wals = ""

printTable(14,11)


