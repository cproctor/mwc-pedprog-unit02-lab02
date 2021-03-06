class TTTGame:
    "Models a tic-tac-toe game."

    def get_initial_state(self):
        "Returns the game's initial state."
        return {
            "board": ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
            "player_x": True,
        }

    def get_next_state(self, state, action):
        """Given a state and an action, returns the resulting state.
        In the resulting state, the current player's symbol has been placed 
        in an empty board space, and it is the opposite player's turn.
        """
        new_board = state["board"].copy()
        new_board[action] = 'X' if state["player_x"] else 'O'
        return {
            "board": new_board,
            "player_x": not state["player_x"],
        }

    def get_actions(self, state):
        "Returns a list of the indices of empty spaces"
        return [index for index in range(9) if state["board"][index] == '-']

    def is_over(self, state):
        "Checks whether the game is over."
        return self.board_is_full(state) or self.check_winner(state, 'X') or self.check_winner(state, 'O')

    def get_reward(self, state):
        """Determines the reward associated with reaching this state.
        For tic-tac-toe, the two opponents each want a different game outcome. So 
        we set the reward for X winning to 1 and the reward for O winning to -1.
        All other states (unfinished games and games which ended in a draw) are worth 0.
        """
        if self.check_winner(state, 'X'):
            return 1
        elif self.check_winner(state, 'O'):
            return -1
        else:
            return 0

    def get_objective(self, state):
        """Returns a player's objective, or a function describing what a player wants. 
        This function should choose the best value from a list. In tic tac toe, the players
        want opposite things, so we set X's objective to the built-in function `max`
        (which chooses the largest number), and we set O's objective to the built-in function `min`.
        """
        return max if state["player_x"] else min

    def board_is_full(self, state):
        "Checks whether all the spaces in the board are occupied."
        for space in state["board"]:
            if space == '-':
                return False
        return True

    def check_winner(self, state, symbol):
        "Checks whether the player with `symbol` has won the game."
        return False
