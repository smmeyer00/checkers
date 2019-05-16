import pygame
from board import Board
import images
import constants
from player import *
import time


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
        self.winner_font = pygame.font.SysFont('comicsansms', 70)
        self.turn = 1
        self.run()

    def check_win(self):
        if len(self.player1.get_pieces()) < 1:
            return 2
        elif len(self.player2.get_pieces()) < 1:
            return 1

        return 0


    def reset(self):
        self.player1 = Player('white')
        self.player2 = Player('black')
        self.turn = 1


    def draw_buttons(self):
        pygame.draw.rect(self.screen, constants.red, pygame.Rect(0, constants.tile_size*9, constants.tile_size*2, constants.tile_size))
        text = self.font.render("Reset", True, constants.black)
        self.screen.blit(text, [0, constants.tile_size*9])

        # finish later, draw reset button bottom left corner


    def run(self):
        # turn = 1
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

                    if 0 < pos[0] < constants.tile_size*2 and constants.tile_size*9 < pos[1] < constants.tile_size*10:
                        self.reset()

                    if self.turn == 1:
                        for p in self.player2.get_pieces():
                            p.selected = False

                        for p in self.player1.get_pieces():
                            if p.selected:
                                possible_moves = p.possible_moves(self.player2, self.player1)
                                for move in possible_moves:
                                    if move[0]*constants.tile_size+constants.tile_size < pos[0] and move[1]*constants.tile_size+constants.tile_size < pos[1] and move[0]*constants.tile_size+2*constants.tile_size > pos[0] and move[1]*constants.tile_size+2*constants.tile_size > pos[1]:
                                        self.turn = 2
                                        jump = False
                                        if abs(p.y-move[1]) > 1:
                                            x = (p.x+move[0])/2
                                            y = (p.y+move[1])/2
                                            jump = True
                                            for p2 in self.player2.pieces:
                                                if p2.x == x and p2.y == y:
                                                    self.player2.pieces.remove(p2)

                                        p.move_to(move)
                                        if jump and p.jump_possible(self.player2, self.player1):
                                            self.turn = 1

                            top_left = [p.get_pos()[0]*constants.tile_size+constants.tile_size, p.get_pos()[1]*constants.tile_size+constants.tile_size]
                            print(top_left)
                            bottom_right = [p.get_pos()[0]*constants.tile_size+2*constants.tile_size, p.get_pos()[1]*constants.tile_size+2*constants.tile_size]
                            print(bottom_right)
                            if top_left[0] < pos[0] and top_left[1] < pos[1] and pos[0] < bottom_right[0] and pos[1] < bottom_right[1]:
                                for piece in self.player1.get_pieces():
                                    piece.selected = False
                                p.selected = True
                                print(str(p.get_pos())+' selected')
                    elif self.turn == 2:
                        for p in self.player1.get_pieces():
                            p.selected = False

                        for p in self.player2.get_pieces():
                            if p.selected:
                                possible_moves = p.possible_moves(self.player1, self.player2)
                                for move in possible_moves:
                                    if move[0]*constants.tile_size+constants.tile_size < pos[0] and move[1]*constants.tile_size+constants.tile_size < pos[1] and move[0]*constants.tile_size+2*constants.tile_size > pos[0] and move[1]*constants.tile_size+2*constants.tile_size > pos[1]:
                                        self.turn = 1
                                        jump = False
                                        if abs(p.y-move[1]) > 1:
                                            x = (p.x+move[0])/2
                                            y = (p.y+move[1])/2
                                            jump = True
                                            for p2 in self.player1.pieces:
                                                if p2.x == x and p2.y == y:
                                                    self.player1.pieces.remove(p2)

                                        p.move_to(move)
                                        if jump and p.jump_possible(self.player1, self.player2):
                                            self.turn = 2

                            top_left = [p.get_pos()[0]*constants.tile_size+constants.tile_size, p.get_pos()[1]*constants.tile_size+constants.tile_size]
                            print(top_left)
                            bottom_right = [p.get_pos()[0]*constants.tile_size+2*constants.tile_size, p.get_pos()[1]*constants.tile_size+2*constants.tile_size]
                            print(bottom_right)
                            if top_left[0] < pos[0] and top_left[1] < pos[1] and pos[0] < bottom_right[0] and pos[1] < bottom_right[1]:
                                for piece in self.player2.get_pieces():
                                    piece.selected = False
                                p.selected = True
                                print(str(p.get_pos())+' selected')


            if self.turn == 1:
                turn_text = self.font.render("White's Turn", True, constants.black)
                for p in self.player2.get_pieces():
                    p.selected = False
            else:
                turn_text = self.font.render("Black's Turn", True, constants.black)
                for p in self.player1.get_pieces():
                    p.selected = False

            if self.check_win() == 1:
                text = self.winner_font.render('White wins!', True, constants.blue)
                self.screen.blit(text, [0, constants.tile_size*5-35])
                pygame.display.flip()
                time.sleep(3)
                self.reset()
            elif self.check_win() == 2:
                text = self.winner_font.render('Black wins!', True, constants.blue)
                self.screen.blit(text, [0, constants.tile_size*5-35])
                pygame.display.flip()
                time.sleep(3)
                self.reset()

            self.player1.update()
            self.player2.update()

            self.screen.fill(constants.white)
            self.board.draw_board(self.screen)
            self.draw_buttons()
            self.screen.blit(turn_text, (0, 0))
            self.player1.draw(self.screen, self.player2, self.player1)
            self.player2.draw(self.screen, self.player1, self.player2)
            pygame.display.flip()
