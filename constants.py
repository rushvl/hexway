from enum import Enum


WIDTH, HEIGHT = 800, 800
HEX_RADIUS = 20
INITIAL_X = 0
INITIAL_Y = 0
GRID_SIZE = 15

OFFSET_Y = 1.7*HEX_RADIUS
OFFSET_X = 2*HEX_RADIUS

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
YELLOW = ( 255, 255, 0)

class cellState(Enum):
    ALIVE = 0
    DEAD = 1
    SELECTED = 2
        
class causeOfDeath(Enum):
    OVER = 0
    UNDER = 1
    
    