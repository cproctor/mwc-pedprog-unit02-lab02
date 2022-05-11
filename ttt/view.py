from ttt.game import TTTGame
import click

class TTTView:
    "Handles user interaction with a tic-tac-toe game."
    greeting = "Welcome to tic-tac-toe"
    goodbye = "Well, that's a wrap."
    divider = "---+---+---"
    x_color = "red"
    o_color = "blue"
    option_color = "bright_black"

    def __init__(self, playerX, playerO):
        self.game = TTTGame()
        self.players = {
            "X": playerX, 
            "O": playerO,
        }

    def greet(self):
        "Starts a new game by greeting the players."
        x_name = self.players['X'].name
        o_name = self.players['O'].name
        print(self.greeting)
        print(f"{x_name} will play as X.")
        print(f"{o_name} will play as O.")

    def get_action(self, state):
        "Shows the board and asks the current player for their choice of action."
        self.print_board(state)
        current_player_symbol = 'X' if state["player_x"] else 'O'
        player = self.players[current_player_symbol]
        print(f"{player.name}, it's your move.")
        return player.choose_action(state)

    def print_board(self, state):
        "Prints the current board, showing indices of available spaces"
        print(self.format_row(state, [0, 1, 2]))
        print(self.divider)
        print(self.format_row(state, [3, 4, 5]))
        print(self.divider)
        print(self.format_row(state, [6, 7, 8]))

    def format_row(self, state, indices):
        "Returns a string for one row in the board, like ' X | O | X '"
        spaces = [self.format_value(state, i) for i in indices]
        return f" {spaces[0]} | {spaces[1]} | {spaces[2]} "

    def format_value(self, state, index):
        """Formats the value for a single space on the board. 
        If the game board already has a symbol in that space, formats that value for the Terminal.
        If the space is empty, instead formats the index of the space. 
        """
        if state["board"][index] == 'X':
            return click.style('X', fg=self.x_color)
        elif state["board"][index] == 'O':
            return click.style('O', fg=self.o_color)
        else:
            return click.style(index, fg=self.option_color)

    def conclude(self, state):
        """Says goodbye.
        """
        self.print_board(state)
        if self.game.check_winner(state, 'X'):
            winner = self.players['X']
        elif self.game.check_winner(state, 'O'):
            winner = self.players['O']
        else:
            winner = None
        print(self.goodbye)
        if winner:        
            print(f"Congratulations to {winner.name}.")
        else:
            print("Nobody won this game.")
