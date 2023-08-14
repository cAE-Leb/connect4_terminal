"""
This program will be a terminal based version of the popular two player board game, Connect Four. 
A standard 7 x 6 sized board will be used. https://en.wikipedia.org/wiki/Connect_Four
"""

# Initialize the Board
NUM_ROWS = 6
NUM_COLS = 7
EMPTY = ' '
PLAYER_1 = 'X'
PLAYER_2 = 'O'

board = [[EMPTY for _ in range(NUM_ROWS)] for _ in range(NUM_COLS)]
#print(board)

def print_column_numbers():
    for col in range(NUM_COLS):
        print(col, end='   ')
    print() # To move to the next line after printing all column numbers


def print_board(board):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            print(board[col][row], end=' | ')
        print() # Move to the next line after printing a row
        print('-' * (NUM_COLS * 4)) # Print horizontal separators


def display_board(board):
    print_column_numbers()
    print_board(board)


display_board(board)