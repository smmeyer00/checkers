import pygame
from pieces import *

class Player:

    def __init__(self, color):
        self.pieces = []
        if color == 'white':
            for x in range(8):
                if x % 2 == 0:
                    self.pieces.append(Piece(x, 0, color))
                    self.pieces.append(Piece(x, 2, color))
                else:
                    self.pieces.append(Piece(x, 1, color))
        else:
            for x in range(8):
                if x % 2 == 0:
                    self.pieces.append(Piece(x, 6, color))
                else:
                    self.pieces.append(Piece(x, 5, color))
                    self.pieces.append(Piece(x, 7, color))

    def get_pieces(self):
        return list(self.pieces)

    def draw(self, screen, other_player, this_player):
        for p in self.pieces:
            p.draw(screen, other_player, this_player)
