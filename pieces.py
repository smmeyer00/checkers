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

    def move_to(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.selected = False

    def king(self):
        self.type = 'king'

    def get_pos(self):
        return list([self.x, self.y])

    def possible_moves(self, other_player, this_player):
        moves = []
        final_moves = []
        if self.type == 'checker':
            if self.color == 'white':
                moves.append([self.x-1, self.y+1])
                moves.append([self.x+1, self.y+1])
                for p in other_player.get_pieces():
                    if p.x == self.x-1 and p.y == self.y+1:
                        moves.append([self.x-2, self.y+2])
                    if p.x == self.x+1 and p.y == self.y+1:
                        moves.append([self.x+2, self.y+2])
            else:
                moves.append([self.x-1, self.y-1])
                moves.append([self.x+1, self.y-1])
                for p in other_player.get_pieces():
                    if p.x == self.x-1 and p.y == self.y-1:
                        moves.append([self.x-2, self.y-2])
                    if p.x == self.x+1 and p.y == self.y-1:
                        moves.append([self.x+2, self.y-2])
        else:
            moves.append([self.x-1, self.y+1])
            moves.append([self.x+1, self.y+1])
            moves.append([self.x-1, self.y-1])
            moves.append([self.x+1, self.y-1])

            for p in other_player.get_pieces():
                if p.x == self.x-1 and p.y == self.y+1:
                    moves.append([self.x-2, self.y+2])
                if p.x == self.x+1 and p.y == self.y+1:
                    moves.append([self.x+2, self.y+2])
                if p.x == self.x-1 and p.y == self.y-1:
                    moves.append([self.x-2, self.y-2])
                if p.x == self.x+1 and p.y == self.y-1:
                    moves.append([self.x+2, self.y-2])


        for move in moves:
            already = False
            for p in other_player.get_pieces():
                if move == [p.x, p.y]:
                    already = True
            for p in this_player.get_pieces():
                if move == [p.x, p.y]:
                    already = True

            if 0 > move[0] or move[0] > 7 or 0 > move[1] or move[1] > 7:
                already = True

            if already == False:
                final_moves.append(move)
        return final_moves


    def update(self):
        if self.color == 'white' and self.y == 7:
            self.type = 'king'
        elif self.color == 'black' and self.y == 0:
            self.type = 'king'


    def jump_possible(self, other_player, this_player):
        moves = self.possible_moves(other_player, this_player)
        final_moves = []
        for move in moves:
            if abs(self.y-move[1]) > 1:
                final_moves.append(move)

        if len(final_moves) > 0:
            return True

        return False



    def draw(self, screen, other_player, this_player):
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
            for pos in self.possible_moves(other_player, this_player):
                pygame.draw.rect(screen, constants.green, pygame.Rect(pos[0]*constants.tile_size+constants.tile_size, pos[1]*constants.tile_size+constants.tile_size, constants.tile_size, constants.tile_size), 3)
