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


current_player = PLAYER_1

def get_player_input(player):
    return int(input(f"Player {player}, choose a column (0 - {NUM_COLS-1}): "))


def is_valid_move(board, column):
    if 0 <= column < NUM_COLS and board[column][0] == EMPTY: #validate range and if spot is empty
        return True
    return False


def place_piece(board, column, player):
    for row in reversed(range(NUM_ROWS)):
        if board[column][row] == EMPTY:
            board[column][row] = player
            break


if __name__ == "__main__":
    board = [[EMPTY for _ in range(NUM_ROWS)] for _ in range(NUM_COLS)]
    current_player = PLAYER_1
    
    for _ in range(NUM_ROWS * NUM_COLS):  # This will allow for the maximum number of moves in a game
        display_board(board)
        column = get_player_input(current_player)
        
        while not is_valid_move(board, column):
            print("Invalid move. Try again.")
            column = get_player_input(current_player)
        
        place_piece(board, column, current_player)
        current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1  # Switch player for next turn

