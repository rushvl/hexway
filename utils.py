import math
import random
import pygame
from constants import *

def drawHexagon(surface, x, y, status):
    pts = []
    if status == cellState.ALIVE:
        width = 0
        color = WHITE
    elif status == cellState.DEAD:
        color = WHITE
        width = 1
    elif status == cellState.SELECTED:
        color = RED
        width = 1
        
    for i in range(6):
        x = x + HEX_RADIUS * math.cos(math.pi/6+math.pi * 2 * i / 6)
        y = y + HEX_RADIUS * math.sin(math.pi/6+math.pi * 2 * i / 6)
        pts.append([int(x), int(y)])

    pygame.draw.polygon(surface, color, pts, width)
    
    
def modulomath(i, j):
    # y = idx/GRID_SIZE
    # x = idx%GRID_SIZE
    
    return i*GRID_SIZE+j

   
def drawGrid(surface, x, y, n, state):
    
    for i in range(0,n):
        y += OFFSET_Y
        #generates honeycomb pattern
        if i%2==1:
            x_t = x+HEX_RADIUS
        else: 
            x_t = x
            
        for j in range(0,n):
            x_t += OFFSET_X
            drawHexagon(surface, x_t, y, state[modulomath(i,j)])