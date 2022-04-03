#Credit for the logic and idea: https://www.youtube.com/watch?v=FWSR_7kZuYg
import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        #A scaler factor that is deciding size of grids per columns and row s// defined in main.py
        self.scale = scale  
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        #Off set to visually distinguish each block 
        self.offset = offset

    #Iterate through all the possible positions and give a dead or alive value 
    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)

    #Use Conway's properties             
    def Conway(self, off_color, on_color, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

        next = np.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbors = self.get_neighbors( x, y)
                    if state == 0 and neighbors == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbors < 2 or neighbors > 3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.grid_array = next
            
    #Check to see surrounding alive/ dead memebers to update accordingly        
    def get_neighbors(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total