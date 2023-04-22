import sys
import time

LINE_UP = '\033[2A'
LINE_DOWN = '\033[1B'
LINE_CLEAR = '\x1b[2K'
CURSOR_INVISIBLE = '\033[?25l'
CURSOR_VISIBLE = '\033[?25h'

cursorVisible = True
cursorPosition = 0

def lineUp(howManyTimes):
    for i in range(howManyTimes):
        print(LINE_UP, sep="", end="")
        print("")
        time.sleep(0.01)
    sys.stdout.flush()

def lineDown(howManyTimes):
     for i in range(howManyTimes): 
        print(LINE_DOWN, sep="", end="")
     sys.stdout.flush()

def setCursorAt(line):
    line = str(line)
    cursorPosition = line
    LINE_AT = '\033['+line+';0H'
    print(LINE_AT, end="")
    sys.stdout.flush()

def setCursorVisible(isVisible):
    cursorVisible = isVisible
    if(isVisible):
        print(CURSOR_VISIBLE, end="")
    else:
        print(CURSOR_INVISIBLE, end="")

def cursorVisible():
    return cursorVisible

def cursorPosition():
    return cursorPosition