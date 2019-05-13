import pygame
from board import Board
import images
import constants
from player import *


class Game:

    # player1 always white, player 2 black

    def __init__(self):
        pygame.init()
        self.board = Board(constants.tile_size, constants.tile_size)
        self.player1 = Player('white')
        self.player1.get_pieces()[1].selected = True
        self.player2 = Player('black')
        self.screen = pygame.display.set_mode((constants.tile_size*10, constants.tile_size*10))
        self.run()

    def event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos

    def run(self):
        turn = 1
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    print('X pos: '+str(x))
                    print('Y pos: '+str(y))


            self.screen.fill(constants.white)
            self.board.draw_board(self.screen)
            self.player1.draw(self.screen, self.player2)
            self.player2.draw(self.screen, self.player1)
            pygame.display.flip()
