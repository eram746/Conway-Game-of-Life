import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = height // scale
        self.rows = width // scale
        self.size = (self.rows, self.columns)
        self.grid_array = np.random.randint(2, size=self.size)
        self.offset = offset

    def Conway(self, off_color, on_color, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos, x_pos = y * self.scale, x * self.scale
                color = on_color if self.grid_array[x][y] == 1 else off_color
                pygame.draw.rect(surface, color, [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])

        if not pause:
            next = np.copy(self.grid_array)
            for x in range(self.rows):
                for y in range(self.columns):
                    state, neighbors = self.grid_array[x][y], self.get_neighbors(x, y)
                    next[x][y] = 1 if (state == 0 and neighbors == 3) or (state == 1 and 2 <= neighbors <= 3) else 0
            self.grid_array = next

    def get_neighbors(self, x, y):
        total = sum(self.grid_array[(x + n) % self.rows][(y + m) % self.columns] for n in range(-1, 2) for m in range(-1, 2))
        return total - self.grid_array[x][y]
