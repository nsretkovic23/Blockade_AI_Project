def CreateNewGame(rows, cols):
    playingFields = createPlayingFields(rows, cols)
    hWalls = createHorizontalWalls(rows, cols)
    vWalls = createVerticalWalls(rows, cols)

    return [playingFields, hWalls, vWalls]


# ROWS, COLS are actual dimensions for a game
# MatrixRows/Cols are dimensions that are suitable for drawing all matrices on the screen
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