# Example file showing a circle moving on screen
import time
import pygame
import math
from constants import *
import utils
import random


# pygame setup
pygame.init()

screen = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()

running = True
playing = False

states = [cellState.DEAD]*(GRID_SIZE*GRID_SIZE)
causes = [None]*(GRID_SIZE*GRID_SIZE)

death_count = {i:1 for i in range(0,GRID_SIZE*GRID_SIZE)}
gen_count = 1

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            # pauses the game
            if event.key == pygame.K_SPACE:
                playing = not playing
                
            # clears the grid 
            if event.key == pygame.K_c:
                states = [cellState.DEAD]*(GRID_SIZE*GRID_SIZE)
                playing = False
                
            # generates random elements
            if event.key == pygame.K_g:
                states = utils.gen()
                playing = False
            
    
    screen.fill("black")

    utils.drawGrid(screen, INITIAL_X, INITIAL_Y, states)
    
    if playing:
        states, causes, death_count, gen_count= utils.adjust_grid(states, causes, death_count, gen_count)
    
    time.sleep(0.5)
    pygame.display.update()

pygame.quit()
