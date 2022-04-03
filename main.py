import time
import random 
import os 
import numpy as np 
import pygame 
import grid 

#Center screen
os.environ["SDL_VIDEO_CENTERED"]='1'

#Color definitions
black = (0, 0, 0)
white = (255, 255, 255)

#Window parameters 
width, height = 1280,720
resolution = (width, height)
icon = pygame.image.load('icon.png')

#Drawing window & Engine parameters 
pygame.init()
pygame.display.set_caption("Unpredictable Machine - Conway Game of Life")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
fps = 15

#Field of view parameters 	
scaler = 10
offset = 2

#Drawing gameboard and spawning 
Grid = grid.Grid(width,height, scaler, offset)
Grid.random2d_array()

#Game start, pause, quit logic 
pause = False
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
    
    Grid.Conway(off_color=black, on_color=white, surface=screen, pause=pause)

    pygame.display.update()

pygame.quit()