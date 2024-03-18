# Example file showing a circle moving on screen
import time
import pygame
import math
from constants import *
import utils
import random


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

states = []

for i in range(0,GRID_SIZE*GRID_SIZE):
    
    k = random.random()
    print(k)
    if k<=0.25:
        states.append(cellState.ALIVE)
    else:
        states.append(cellState.DEAD)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    utils.drawGrid(screen, INITIAL_X, INITIAL_Y, GRID_SIZE, states)
    # flip() the display to put your work on screen
    pygame.display.flip()

    time.sleep(1)
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
