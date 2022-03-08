# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:53:48 2022

@author: MS
"""


import numpy as np

POSSIBLE_MOVES = 4
MAX_CELL = 4
TOTAL_SQUARES = MAX_CELL * MAX_CELL

board = np.zeros((TOTAL_SQUARES), dtype="int")

def pushRight():
    new_board = np.zeros((MAX_CELL, MAX_CELL), dtype="int")
    done = False
    for r in MAX_CELL:
        NEW_CELL = MAX_CELL - 1
        for c in range(MAX_CELL-1, -1, -1):
            if board[r][c] != 0:
                new_board[r][c] = board[r][c]
                if c != NEW_CELL:
                    done = True
                NEW_CELL -= 1
                
    return(new_board, done)

def mergeSquares(board):
    score = 0
    done = False
    for r in range(MAX_CELL):
        for c in range(MAX_CELL- 1, 0, -1): 
            if (board[r][c] != 0) and (board[r][c] == board[r][c-1]):
                board[r][c] *= 2
                score += board[r][c]
                board[r][c-1] = 0
                done = True

    return (board, done, score)

'''def pushLeft():
    new_board = np.zeros((MAX_CELL, MAX_CELL), dtype="int")
    done = False
    for r in MAX_CELL:
        NEW_CELL = MAX_CELL - 1
        for c in range(MAX_CELL-1, 7, +1):
            if board[r][c] != 0:
                new_board[r][c] = board[r][c]
                if c != NEW_CELL:
                    done = True
                NEW_CELL -= 1
                
    return(new_board, done) '''


#RIGHT
def move_right(board):
    
    board, pushed = pushRight(board)
    board, merged, score = mergeSquares(board)
    
    board = pushRight(board)
    moveDone = (pushed or merged)
    
    return board, moveDone, score


#LEFT
def move_left(board):
    #reverse
    board = np.rot90(board, 2)
    board, pushed = pushRight(board)
    board, merged, score = mergeSquares(board)
    
    board = pushRight(board)
    #Un-reverse
    board = np.rot90(board, -2)
    
    moveDone = (pushed or merged)
    
    return board, moveDone, score


#UP
def move_up(board):
    #transpose ---  rot90 does anti-clock rotation
    #-1 takes it in the other direction
    board = np.rot90(board, -1) 
    board, pushed = pushRight(board)
    board, merged, score = mergeSquares(board)
    
    board = pushRight(board)
    #Un-Transpose
    board = np.rot90(board)
    
    moveDone = (pushed or merged)
    
    return board, moveDone, score


#DOWN
def move_down(board):
    #transpose ---  rot90 does anti-clock rotation
    board = np.rot90(board)
    board, pushed = pushRight(board)
    board, merged, score = mergeSquares(board)
    
    board = pushRight(board)
    #Un-Transpose
    board = np.rot90(board, -1)
    moveDone = (pushed or merged)
    
    return board, moveDone, score

print(board)

                

    
