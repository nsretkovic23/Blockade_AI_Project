import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def printGameMatrix(rows, cols, playerFields, hWalls, vWalls):
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
