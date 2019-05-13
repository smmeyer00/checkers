import pygame
import constants
import images


class Piece:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.type = 'checker'
        self.color = color
        self.selected = False

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def king(self):
        self.type = 'king'

    def possible_moves(self, player):
        moves = []
        final_moves = []
        if self.type == 'checker':
            if self.color == 'white':
                moves.append([self.x-1, self.y+1])
                moves.append([self.x+1, self.y+1])
            else:
                moves.append([self.x-1, self.y-1])
                moves.append([self.x+1, self.y-1])
        else:
            moves.append([self.x-1, self.y+1])
            moves.append([self.x+1, self.y+1])
            moves.append([self.x-1, self.y-1])
            moves.append([self.x+1, self.y-1])

        for move in moves:
            already = False
            for p in player.get_pieces():
                if move == [p.x, p.y]:
                    already = True

            if 0 > move[0] or move[0] > 7 or 0 > move[1] or move[1] > 7:
                already = True

            if already == False:
                final_moves.append(move)
        return final_moves



    def draw(self, screen, other_player):
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

        if self.selected:
            pygame.draw.rect(screen, constants.red, pygame.Rect(self.x*constants.tile_size+constants.tile_size, self.y*constants.tile_size+constants.tile_size, constants.tile_size, constants.tile_size), 3)
            for pos in self.possible_moves(other_player):
                pygame.draw.rect(screen, constants.red, pygame.Rect(pos[0]*constants.tile_size+constants.tile_size, pos[1]*constants.tile_size+constants.tile_size, constants.tile_size, constants.tile_size), 3)
