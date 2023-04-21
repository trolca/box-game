import os
import msvcrt as ms
import time

height = 17
width = 12

backround = "▒▒"
boxtext = "▣"

player = [0, 5]
boxes = [[2, 30], [5, 30]]

def drawScreen(width, height):
    for y in range(0, height):
        for x in range(0, width):
            if y == 0 or y == height-1 or x == 0 or x == width-1: print(backround, end="")
            else: print("  ", end="")
        
        print()

drawScreen(width, height)
