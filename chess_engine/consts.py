# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:43:27 2021

@author: Korean_Crimson
"""

EMPTY = '  '
PAWN = 'o'
KNIGHT = 'N'
BISHOP = 'L'
ROOK = 'R'
QUEEN = 'Q'
KING = 'K'

WHITE = '1'
BLACK = '2'

# BACKROW = [ROOK, ROOK, ROOK, ROOK, ROOK, ROOK, ROOK, ROOK]
BACKROW = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
FRONTROW = [PAWN] * 8

BOARD = [[piece + BLACK for piece in BACKROW],
         [piece + BLACK for piece in FRONTROW],
         [EMPTY] * 8,
         [EMPTY] * 8,
         [EMPTY] * 8,
         [EMPTY] * 8,
         [piece + WHITE for piece in FRONTROW],
         [piece + WHITE for piece in BACKROW]
         ]

DIRECTIONS = {WHITE: -1, BLACK: 1}
