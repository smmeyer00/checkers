import pygame
from board import Board
import images
import constants
from player import *


class Game:

    def __init__(self):
        pygame.init()
        self.board = Board(constants.tile_size, constants.tile_size)
        self.player1 = Player('white')
        self.player2 = Player('black')
        self.screen = pygame.display.set_mode((constants.tile_size*10, constants.tile_size*10))
        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(constants.white)
            self.board.draw_board(self.screen)
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            pygame.display.flip()
