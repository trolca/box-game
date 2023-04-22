import sys
import time

LINE_UP = '\033[2A'
LINE_DOWN = '\033[1B'
LINE_CLEAR = '\x1b[2K'


def lineUp(howManyTimes):
    for i in range(howManyTimes):
        print(LINE_UP, sep="", end="")
        print("")
    sys.stdout.flush()

def lineDown(howManyTimes):
     for i in range(howManyTimes): 
        print(LINE_DOWN, sep="", end="")
     sys.stdout.flush()