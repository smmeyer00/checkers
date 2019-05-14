import pygame
from board import Board
import images
import constants
from player import *


class Game:

    # player1 always white, player 2 black
    # font = pygame.font.SysFont('comicsansms', 30)

    def __init__(self):
        pygame.init()
        self.board = Board(constants.tile_size, constants.tile_size)
        self.player1 = Player('white')
        # self.player1.get_pieces()[0].selected = True
        self.player2 = Player('black')
        self.screen = pygame.display.set_mode((constants.tile_size*10, constants.tile_size*10))
        self.font = pygame.font.SysFont('comicsansms', 30)
        self.run()


    def run(self):
        turn = 1
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = [event.pos[0], event.pos[1]]
                    print(pos)
                    # print('X pos: '+str(x))
                    # print('Y pos: '+str(y))
                    if turn == 1:
                        for p in self.player1.get_pieces():
                            # print(p.get_pos())
                            # [0, 50] < [100, 0] <- True/
                            top_left = [p.get_pos()[0]*constants.tile_size+constants.tile_size, p.get_pos()[1]*constants.tile_size+constants.tile_size]
                            print(top_left)
                            bottom_right = [p.get_pos()[0]*constants.tile_size+2*constants.tile_size, p.get_pos()[1]*constants.tile_size+2*constants.tile_size]
                            print(bottom_right)
                            if top_left[0] < pos[0] and top_left[1] < pos[1] and pos[0] < bottom_right[0] and pos[1] < bottom_right[1]:
                                for piece in self.player1.get_pieces():
                                    piece.selected = False
                                p.selected = True
                                print(str(p.get_pos())+' selected')
                    elif turn == 2:
                        for p in self.player2.get_pieces():
                            # print(p.get_pos())
                            # [0, 50] < [100, 0]
                            top_left = [p.get_pos()[0]*constants.tile_size+constants.tile_size, p.get_pos()[1]*constants.tile_size+constants.tile_size]
                            print(top_left)
                            bottom_right = [p.get_pos()[0]*constants.tile_size+2*constants.tile_size, p.get_pos()[1]*constants.tile_size+2*constants.tile_size]
                            print(bottom_right)
                            if top_left[0] < pos[0] and top_left[1] < pos[1] and pos[0] < bottom_right[0] and pos[1] < bottom_right[1]:
                                for piece in self.player2.get_pieces():
                                    piece.selected = False
                                p.selected = True
                                print(str(p.get_pos())+' selected')


            if turn == 1:
                turn_text = self.font.render("White's Turn", True, constants.black)
            else:
                turn_text = self.font.render("Black's Turn", True, constants.black)


            self.screen.fill(constants.white)
            self.board.draw_board(self.screen)
            self.screen.blit(turn_text, (0, 0))
            self.player1.draw(self.screen, self.player2, self.player1)
            self.player2.draw(self.screen, self.player1, self.player2)
            pygame.display.flip()
