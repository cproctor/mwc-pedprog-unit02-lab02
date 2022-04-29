class TTTGame:
    "Models a tic-tac-toe game."

    def __init__(self, playerX, playerO):
        self.board = [None] * 9
        self.turn_index = 0
        self.players = {
            'X': playerX,
            'O': playerO,
        }

    def play_move(self, move):
        "Updates the game's state by recording a move"
        if not self.is_valid_move(move):
            raise ValueError(f"Illegal move {move} with board {self.board}.")
        self.board[move] = self.get_current_player_symbol()
        self.turn_index += 1

    def get_valid_moves(self):
        "Returns a list of the indices of empty spaces"
        return [index for index in range(9) if self.board[index] is None]

    def is_valid_move(self, move):
        "Checks whether a move is valid"
        return move in self.get_valid_moves()

    def get_current_player_symbol(self):
        "Returns the symbol of the current player"
        if self.turn_index % 2 == 0:
            return 'X'
        else:
            return 'O'

    def get_current_player(self):
        "Returns the symbol of the current player and the current player"
        return self.players[self.get_current_player_symbol()]
        
    def is_over(self):
        "Checks whether the game is over."
        return self.board_is_full() or self.check_winner('X') or self.check_winner('O')

    def board_is_full(self):
        "Checks whether all the spaces in the board are occupied."
        for space in self.board:
            if space == None:
                return False
        return True

    def check_winner(self, symbol):
        "Checks whether the player with `symbol` has won the game."
        return False
