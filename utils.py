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
    else:
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

   
def drawGrid(surface, x, y, states):
    
    for i in range(0,GRID_SIZE):
        y += OFFSET_Y
        #generates honeycomb pattern
        if i%2==1:
            x_t = x+HEX_RADIUS
        else: 
            x_t = x
            
        for j in range(0,GRID_SIZE):
            x_t += OFFSET_X
            drawHexagon(surface, x_t, y, states[modulomath(i,j)])
            

def gen():
    states = []
    for i in range(0,GRID_SIZE*GRID_SIZE):
        
        k = random.random()
        if k<=0.25:
            states.append(cellState.ALIVE)
        else:
            states.append(cellState.DEAD)
            
    return states


def get_neighbors(idx):
    
    E = idx + 1
    W = idx - 1    
    NW = (idx - GRID_SIZE) if (idx//GRID_SIZE)%2 == 1 else (idx-GRID_SIZE-1)
    NE = NW + 1
    SW = NW+GRID_SIZE*2
    SE = SW+1
    
    directions  = [E, W, NW, NE, SW, SE]
    unwanted = []
    
    if idx//GRID_SIZE == 0:
        unwanted.extend([NW, NE])
    
    if idx%GRID_SIZE == 0:
        unwanted.extend([W, SW, NW] if (idx//GRID_SIZE)%2 == 0 else [W])
        
    if idx%GRID_SIZE == GRID_SIZE-1:
        unwanted.extend([E, SE, NE] if (idx//GRID_SIZE)%2 == 1 else [E])
        
    if idx//GRID_SIZE == GRID_SIZE-1:
        unwanted.extend([SW,SE])
            
    for d in unwanted:
        if d in directions:
            directions.remove(d)
    
    return directions
 
       
def get_alive_count(directions: list, states: list):
    count = 0
    for idx in directions:
        if states[idx] == cellState.ALIVE:
            count = count + 1
            
    return count


def adjust_grid(states: list, causes:list, dead_count:dict, gen_count):
    new_states = states
    new_death_count = dead_count
    new_causes = causes
    
    for i in range(0,GRID_SIZE*GRID_SIZE):
        
        directions = get_neighbors(i)
        alive_count = get_alive_count(directions, states)

        if states[i] == cellState.ALIVE and alive_count < 2 and causes[i] != causeOfDeath.UNDER:
            new_states[i] = cellState.DEAD
            new_death_count[i] = 1
            new_causes[i] = causeOfDeath.UNDER
            
        elif states[i] == cellState.ALIVE and alive_count > 3 and causes[i]!= causeOfDeath.OVER:
            new_states[i] = cellState.DEAD
            new_death_count[i] = 1
            new_causes[i] = causeOfDeath.OVER
            
        elif states[i] == cellState.DEAD and alive_count == 3:
            new_states[i] = cellState.ALIVE
            new_death_count[i] = 1
            
        # if states[i] == cellState.DEAD and new_death_count[i] == 6:
        #     new_states[i] = cellState.ALIVE
        #     new_death_count[i] = 1         
            
        # if states[i] == cellState.DEAD:
        #     new_death_count[i] = new_death_count[i]+1
        
    return new_states, new_causes, new_death_count, gen_count
            
    
            