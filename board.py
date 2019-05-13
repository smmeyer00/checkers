import pygame
import constants

class Board:

    # github test comment

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw_board(self, surface):
        for x in range(0, 8*constants.tile_size, constants.tile_size):
            for y in range(0, 8*constants.tile_size, constants.tile_size):
                if (x/constants.tile_size) % 2 == (y/constants.tile_size) % 2:
                    pygame.draw.rect(surface, constants.grey, (self.xpos + x, self.ypos+y, constants.tile_size, constants.tile_size))
                else:
                    pygame.draw.rect(surface, constants.black, (self.xpos+x, self.ypos+y, constants.tile_size, constants.tile_size))
