import os
import msvcrt as ms
import time


height = 17
width = 12

backround = "▒▒"
boxtext = "⛋ "
playertext = '⬜'

player = [0, 13]
boxes = [[2, 0], [5, 0]]

#test

def drawScreen(width, height):
    for y in range(-1, height+1):
        for x in range(-1, width+1):
            if (y == -1 or y == height or x == -1 or x == width): print(backround, end="")
            elif (player[0] == x and player[1] == y): print(playertext, end="")
            else: 
                hasbox = False
                for box in boxes:
                    if(box[0] == x and box[1] == y):
                        print(boxtext, end="")
                        hasbox = True
                if not hasbox: print("  ", end="")

        print()

while(True):
    

    x = ms.getch()
    os.system("cls")
    
    if(x == b'M'):
        player[0] += 1#prawo
    elif (x == b'K'):
        player[0] -= 1 #lewo

    drawScreen(width, height)
