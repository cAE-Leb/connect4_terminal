import numpy as np

class Connect4Env:
    NUM_COLS = 7
    NUM_ROWS = 6


    def __init__(self):
        #Initial board state
        self.board = np.zeros((Connect4Env.NUM_COLS, Connect4Env.NUM_ROWS), dtype=int)
        self.current_player = 1 #player one starts off
        self.done = False #indicates when the game is over
        self.winner = None #stores winner (if there is one)

        #rewards for model
        self.reward_win = 10
        self.reward_lose = -10
        self.reward_draw = 0
        self.reward_invalid_move = -15


    def action_space(self):
        #number of columns as the size of action space
        return Connect4Env.NUM_COLS
    
        
    def state_space(self):
        #returns board config
        return self.board.copy()
    
    
    def reset(self):
        #resets env to initial state
        self.board = np.zeros((Connect4Env.NUM_COLS, Connect4Env.NUM_ROWS), dtype=int)
        self.current_player = 1
        self.done = False
        self.winner = None
        return self.board
    
    
    def step(self, action):
        # Check if the selected column is valid
        if not self.is_valid_move(action):
            return self.board, self.reward_invalid_move, True, {"winner": None}
        
        # Place the piece
        self.place_piece(action, self.current_player)

        # Check if the current player has won
        if self.check_win():
            self.done = True
            self.winner = self.current_player
            # If current player is the agent, return winning reward. Otherwise, return losing reward.
            reward = self.reward_win if self.current_player == 1 else self.reward_lose
            return self.board, reward, True, {"winner": self.winner}

        # If it's a tie
        if self.is_draw():
            self.done = True
            return self.board, self.reward_draw, True, {"winner": None}

        # If game is still ongoing, switch to the other player
        self.current_player = 3 - self.current_player  # Switches between 1 and 2
        return self.board, 0, False, {}
    
    
    def is_valid_move(self, column):
        # Check if the selected column is in range and the top-most row of the column is empty
        return 0 <= column < self.action_space and self.board[column][0] == 0
    
    
    def place_piece(self, column, player):
        for row in reversed(range(Connect4Env.NUM_ROWS)):
            if self.board[column][row] == 0:
                self.board[column][row] = player
                break

                
    def check_win(self):
        return (self.check_horizontal() or self.check_vertical() or
                self.check_diagonal_left_to_right() or self.check_diagonal_right_to_left())

    
    def check_horizontal(self):
        for row in range(Connect4Env.NUM_ROWS):
            for col in range(Connect4Env.NUM_COLS - 3):  # -3 to stay within board boundary
                if self.consecutive_cells_are_same(self.board[col][row], self.board[col + 1][row], 
                                                   self.board[col + 2][row], self.board[col + 3][row]):
                    return True
        return False

    # Similarly, adapt `check_vertical`, `check_diagonal_left_to_right`, and `check_diagonal_right_to_left`...
    

    def is_draw(self):
        return all(cell != 0 for column in self.board for cell in column)
    

    def consecutive_cells_are_same(self, cell1, cell2, cell3, cell4):
        return cell1 == cell2 == cell3 == cell4 and cell1 != 0