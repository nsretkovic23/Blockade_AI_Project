# PLAYABLE - 1,1 - 4,4
playerFields = [["",   "",   "",   "",  ""],
                ["", "X1", "  ", "  ","  "],
                ["", "  ", "  ", "  ","  "],
                ["", "  ", "Y2", "  ","  "],
                ["", "  ", "  ", "  ","  "]]

hWalls = [
          ["", "= ", "= ", "= ", "= "],
          ["", "--", "--", "--", "--"],
          ["", "--", "--", "--", "--"],
          ["", "--", "--", "--", "--"],
          ["", "= ", "= ", "= ", "= "],]

vWalls = [["", "", "", "", ""],
          ["\u01c1", "|", "|", "|", "\u01c1"],
          ["\u01c1", "|", "|", "|", "\u01c1"],
          ["\u01c1", "|", "|", "|", "\u01c1"],
          ["\u01c1", "|", "|", "|", "\u01c1"]]

fields_and_V_Wals = ""
h_Wals = ""
for i in range(0, 5):
  for j in range(0, 5):
    # Stampaj samo = = = za gornju ivicu
    if(i == 0):
      h_Wals += hWalls[i][j] + " "

    if(i > 0):
      fields_and_V_Wals += playerFields[i][j] + vWalls[i][j]
      h_Wals +=hWalls[i][j] + " "
  if(i==0):
    print(h_Wals)
  else:
    print(fields_and_V_Wals)
    print(h_Wals)

  fields_and_V_Wals = ""
  h_Wals = ""



#print(" =  "+"=  "+"=  "+"=  ")
#row = ""
#row_hWalls = ""
#for i in range(0,4):
#  for j in range(0, 4):
#    row += str(playerFields[i][j]) + str(vWalls[i][j])
#    row_hWalls += (" "+hWalls[i][j]) 
#  print("\u01c1" +row)
#  print(row_hWalls)
#  row = ""  
#  row_hWalls = ""
#print("  = "+"= "+"= "+"= "+"=")


#if(vWalls[0][3] == "\u01c1"):
#  print("trueeeee")






#print(printFieldLabel(15, 1))

#def print2DMatrix(arr, rows, columns):
#   
#  for i in range(0, rows * columns):
#    row = i // columns
#    col = i % columns
# 
#    print(arr[row][col], end = ' ')
#
#
#mat = [ [ 1, 2, 3 ],
#          [ 4, 5, 6 ],
#          [ 7, 8, 9 ] ]
#   
#  # Dimensions of the matrix
#N = 3
#M = 3
# 
#print2DMatrix(mat, N, M)