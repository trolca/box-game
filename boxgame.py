#Zrobione przez Szymona (trolca) i Norberta (norbertc)
import os
import msvcrt as ms
import time
import console_cursor as cursor
import _thread as thread
import random as rng

#0 - flicker mode (redraws the whole screen every move)
#1 - only cursor flicker mode (redraws only specific regions where there was movement)
renderMode = 1
running = True
canMove = True

score = 0
sleepTime = 1 #after how much secound is next tick
boxesPerTick = 1 #defines how many boxes spawn each tick

# border's size
height = 17
width = 12

boxtext = "⛋ "
playertext = '⬜'

# gfx
backround = "▒▒"
#boxtext = "■ "
#playertext = '# '
whitespace = '  '
centerBorder = "▒▒"+(whitespace*width)+"▒▒"
centerBorderPlayer = "▒▒"+(whitespace*width)+"▒▒▒"

# positioning
# 0 - x, 1 - y
player = [0, 13]
boxes = [[2, 0], [5, 0]]
boxesAmount = 5
boxesStartYPos = 0


os.system("cls")

#aaaaa
#bbbbb

# ---- FUNCTIONS -----
# make screen borders
def drawScreen(width, height):
    for y in range(-1, height+1):
        for x in range(-1, width+1):

            if (y == height or (x == -1 and y != -1) or (x == width and y != -1)): print(backround, end="")
            elif (y == -1 and x == -1): print(backround*5,"SCORE: "+str(score),backround*4, end="")
            elif (player[0] == x and player[1] == y): print(playertext, end="")
            elif(y != -1): 
                hasbox = False

                for box in boxes:
                    if(box[0] == x and box[1] == y):
                        print(boxtext, end="")
                        hasbox = True
                        
                if not hasbox: print(whitespace, end="")

        print()

#groups all the boxes in a specific line
def getBoxesByYInSpecificHeight(boxes, height):
    newBoxes = []
    for box in boxes:
        if(box[1] == height): newBoxes.append(box)
    return newBoxes

#it updates a specific line of boxes on the screen
def updateLine(line):
    existingBoxes = getBoxesByYInSpecificHeight(boxes, line)
    cursor.setCursorAt(line+2)
    print(backround, end="")
    isPlayer = False

    
    for i in range(width):
        isSomething = False

        if(line == player[1] and player[0] == i):
            print(playertext, end="")
            isSomething = True
            isPlayer = True

        for box in existingBoxes:
            if isSomething: break
            if(box[0] == i): 
                print(boxtext, end="")
                isSomething = True

        if(not isSomething): print(whitespace, end="")
    
#    print(backround, end="")
    if not isPlayer: print(backround, end="")
    else: print(backround+" ", end="")
    cursor.setCursorAt(height+3)

    if(existingBoxes == [] and line != player[1]):
        cursor.setCursorAt(line+2)
        if(line == height): print(backround*14, end="")
        else: print(centerBorder, end="")
        cursor.setCursorAt(height+3)

#moves a specific box (maybe change? idk)

#check if the player is inside of a box
def checkCollisions():
    global score
    global running
    global canMove
    global sleepTime
    global boxesPerTick
    global boxes
    for box in boxes:
        if box[0] == player[0] and box[1] == player[1]:
            canMove = False
            sleepTime = -1
            for i in range(2,height+2):
                cursor.setCursorAt(i)
                print(centerBorder, end="")

            cursor.setCursorAt(9)
            print(backround+whitespace*((width//3)-1),"GAME OVER")
            print(backround, "YOU SCORED ", score, " POINTS")
            print(backround, "HIT ANY KEY TO RESTART")

            time.sleep(2)
            
            x = ms.getch()
            if(x == b'\x00'): x = ms.getch()
            score = 1
            updateHeader()
            boxes.clear()

            for line in range(2, height+2):
                updateLine(line)

            cursor.setCursorAt(0)
            canMove = True
            sleepTime = 1
            boxesPerTick = 1
            return
        
#prints the score and upps the difficulty of the game
def updateHeader():
    global score
    global sleepTime
    global boxesPerTick
    score += 1
    if(renderMode == 1):
        cursor.setCursorAt(0)
        print(backround*4,"SCORE: "+str(score),backround*4)
        cursor.setCursorAt(height+3)
    
    if sleepTime == -1: return
    match score:
        case 15:
            sleepTime = 0.9
        case 30:
            sleepTime = 0.8
        case 40:
            sleepTime = 0.7
            boxesPerTick = 2
        case 80:
            sleepTime = 0.65
        case 100:
            boxesPerTick = 3
        case 140:
            sleepTime = 0.6
        case 165:
            sleepTime = 0.5
        case 200:
            sleepTime = 0.4
        case 225:
            sleepTime = 0.35
            boxesPerTick = 4
        case 300:
            sleepTime = 0.3
        case 400:
            sleepTime = 0.2




#bassicaly moves all of the boxes down
def boxLogic():
    global canMove
    global running
    global sleepTime
    global boxesPerTick
    while(running):
        

        time.sleep(sleepTime)

        while sleepTime == -1:
            time.sleep(0.1)

        if(renderMode == 0): os.system("cls")

        canMove = False
        removeBoxes = []
        updateLines = set({})
        line = 0

        for box in boxes:
            updateLines.add(box[1])
            box[1] += 1
            updateLines.add(box[1])

            if box[1] > height-1: 
                removeBoxes.append(box)

        for box in removeBoxes:
            line = box[1]
            if boxes == []: break
            boxes.remove(box)
            updateLines.add(line)

        if(renderMode == 1):
            for i in updateLines:
                updateLine(i)

        checkCollisions()
        updateHeader()


        for i in range(boxesPerTick):
            newBox = [rng.randint(0, width), 0]
            if not boxes.__contains__(newBox): boxes.append([rng.randint(0, width), 0])
        if(renderMode == 1): 
            updateLine(0)
        else: drawScreen(width, height)

        canMove = True




drawScreen(width, height)

#the boxLogic function is called in a different thread to make the boxes not dependent on players movement
thread.start_new_thread(boxLogic, ())

# everything in this loop is performed in each frame
while(running):

    

    x = ms.getch()

    if(renderMode == 0): os.system("cls")

    if(x == b'\x00'): x = ms.getch()
    if not running: break
    if(renderMode == 0): os.system("cls")
    # reading input from keyboard
    if(x == b'M'):  
        player[0] += 1  # right arrow pressed
    elif (x == b'K'):
        player[0] -= 1  # left arrow pressed
    elif(x == b'\x1b'):
         running = False
    
    
    # make player can't go beyond borders
    if(player[0] < 0):
        player[0] = 0
    elif(player[0] > width - 1): 
        player[0] = width - 1
    
    # update screen
    if(renderMode == 1):
        while not canMove:
            time.sleep(0.001)
        updateLine(player[1])
        checkCollisions()
    else:
        drawScreen(width, height)

    
