import os
import msvcrt as ms
import time
import console_cursor as cursor

#0 - flicker mode (redraws the whole screen every move)
#1 - only cursor flicker mode (redraws only specific regions where there was movement)
renderMode = 1

height = 17
width = 12

backround = "▒▒"
boxtext = "⛋ "
playertext = '⬜'
whitespace = '  '

centerBorder = "▒▒"+(whitespace*width)+"▒▒"

os.system("cls")

# 0 - x, 1 - y
player = [0, 13]
boxes = [[2, 0], [5, 0], [3, 4], [7, 4], [1, 7]]

LINE_UP = '\033[2A'
LINE_DOWN = '\033[1B'
LINE_CLEAR = '\x1b[2K'


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
                        
                if not hasbox: print(whitespace, end="")

        print()

#draws the correct possition of the player
def updatePlayer():
    cursor.lineUp(5)

    print(backround, end="")

    for i in range(width):
        if(player[0] == i): print(playertext, end="")
        else: print(whitespace, end="")

    print(backround, end="")

    cursor.lineDown(5)

#groups all the boxes in a specific line
def setBoxesByYInSpecificHeight(boxes, height):
    newBoxes = []
    for box in boxes:
        if(box[1] == height): newBoxes.append(box)
    return newBoxes
        
#it updates a specific line of boxes on the screen
def updateBoxesOnLine(line):
    existingBoxes = setBoxesByYInSpecificHeight(boxes, line)
   
   
    cursor.lineUp(height-(line-1))
    print(backround, end="")

    for i in range(width):
        isBox = False
        for box in existingBoxes:  
            if(box[0] == i): 
                print(boxtext, end="")
                isBox = True
        if(not isBox): print(whitespace, end="")
           

    print(backround, end="")
    cursor.lineDown(height-(line-1))

    if existingBoxes == []:
        cursor.lineUp(height-(line-1))
        print(centerBorder, end="")
        cursor.lineDown(height-(line-1))

#moves a specific box (maybe change? idk)
def moveBox(boxIndex, howMuchY):
    oldPos = boxes[boxIndex][1]
    boxes[boxIndex][1] += howMuchY
    updateBoxesOnLine(oldPos)
    updateBoxesOnLine(boxes[boxIndex][1])





drawScreen(width, height)

    
while(True):
    
    x = ms.getch()
    x = ms.getch()

    if(renderMode == 0): os.system("cls")

    if(x == b'M'):  
        player[0] += 1#prawo
    elif (x == b'K'):
        player[0] -= 1 #lewo
    
    if(player[0] < 0): player[0] = 0
    elif(player[0] > width): player[0] = width
    
    if(renderMode == 1): updatePlayer()
    else: drawScreen(width, height)
    #moveBox(1, 1)

