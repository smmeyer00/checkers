import pygame
import constants
import images


class Piece:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.type = 'checker'
        self.color = color

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def king(self):
        self.type = 'king'

    def draw(self, screen):
        if self.type == 'checker':
            if self.color == 'white':
                screen.blit(images.white_checker, [self.x*constants.tile_size+constants.tile_size, self.y*constants.tile_size+constants.tile_size])
            else:
                screen.blit(images.black_checker, [self.x*constants.tile_size+constants.tile_size, self.y*constants.tile_size+constants.tile_size])
        else:
            if self.color == 'white':
                screen.blit(images.white_king, [self.x*constants.tile_size+constants.tile_size, self.y*constants.tile_size+constants.tile_size])
            else:
                screen.blit(images.black_king, [self.x*constants.tile_size+constants.tile_size, self.y*constants.tile_size+constants.tile_size])
