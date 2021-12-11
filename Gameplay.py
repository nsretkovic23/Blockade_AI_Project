import sys
from UIController import clearConsole
from GameManager import GameManager

state = GameManager()

print("Welcome to the BLOCKADE GAME!")
print("Who do you want to play first? Type me/cpu")

if(input("who plays") == "cpu"):
    clearConsole()
