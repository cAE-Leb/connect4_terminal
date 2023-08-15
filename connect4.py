"""
This program will be a terminal based version of the popular two player board game, Connect Four. 
A standard 7 x 6 sized board will be used. https://en.wikipedia.org/wiki/Connect_Four
"""

# global variables
NUM_ROWS = 6
NUM_COLS = 7
EMPTY = ' '
PLAYER_1 = 'X'
PLAYER_2 = 'O'


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


def consecutive_cells_are_same(cell1, cell2, cell3, cell4):
    if cell1 == cell2 == cell3 == cell4 and cell1 != EMPTY:
        return True
    return False


def check_horizontal(board):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3): # -3 to stay within board boundary
            if consecutive_cells_are_same(board[col][row], board[col + 1][row], board[col + 2][row], board[col + 3][row]):
                return True
    return False
        

def check_vertical(board):
    for col in range(NUM_COLS):
        for row in range(NUM_ROWS - 3):  # -3 to stay within board limits
            if consecutive_cells_are_same(board[col][row], board[col][row + 1], board[col][row + 2], board[col][row + 3]):
                return True
    return False


def check_diagonal_left_to_right(board):
    for col in range(NUM_COLS - 3):
        for row in range(NUM_ROWS - 3):
            if consecutive_cells_are_same(board[col][row], board[col + 1][row + 1], board[col + 2][row + 2], board[col + 3][row + 3]):
                return True
    return False


def check_diagonal_right_to_left(board):
    for col in range(NUM_COLS - 3):
        for row in range(3, NUM_ROWS):  # Start from the 4th row
            if consecutive_cells_are_same(board[col][row], board[col + 1][row - 1], board[col + 2][row - 2], board[col + 3][row - 3]):
                return True
    return False


def check_win(board):
    if (check_horizontal(board) or
        check_vertical(board) or
        check_diagonal_left_to_right(board) or
        check_diagonal_right_to_left(board)):
        return True
    return False



if __name__ == "__main__":
    #initialize board
    board = [[EMPTY for _ in range(NUM_ROWS)] for _ in range(NUM_COLS)]
    current_player = PLAYER_1

    #flag to check if game is still ongoing
    game_over = False


    #main loop
    while not game_over:
        display_board(board)

        column = get_player_input(current_player)

        while not is_valid_move(board, column):
            print("Invalid move. Try again.")
            column = get_player_input(current_player)

        place_piece(board, column, current_player)
        if check_win(board):
            display_board(board) # show the final winning board
            print(f"Player {current_player} wins!")
            game_over = True
        else:
            current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1

        if all([cell != EMPTY for row in board for cell in row]):
            display_board(board)
            print("Its a tie!")
            game_over = True