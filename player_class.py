from settings import *
import pygame

vec = pygame.math.Vector2


class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = vec((self.grid_pos.x * self.app.cell_width) + TOP_BOTTOM_BUFFER,
                           (self.grid_pos.y * self.app.cell_height) + TOP_BOTTOM_BUFFER)
        print(self.grid_pos, self.pix_pos)
