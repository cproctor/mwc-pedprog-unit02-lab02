import click

class TTTView:
    "Handles user interaction with a tic-tac-toe game."
    greeting = "Welcome to tic-tac-toe"
    goodbye = "Well, that's a wrap."
    divider = "---+---+---"
    x_color = "red"
    o_color = "blue"
    option_color = "bright_black"

    def greet(self, game):
        "Starts a new game by greeting the players."
        x_name = game.players['X'].name
        o_name = game.players['O'].name
        print(self.greeting)
        print(f"{x_name} will play as X.")
        print(f"{o_name} will play as O.")

    def get_move(self, game):
        "Shows the board and asks the current player for their choice of move."
        self.print_board_with_options(game)
        player = game.get_current_player()
        print(f"{player.name}, it's your move.")
        return player.choose_move(game)

    def print_board_with_options(self, game):
        "Prints the current board, showing indices of available spaces"
        print(self.format_row(game, [0, 1, 2]))
        print(self.divider)
        print(self.format_row(game, [3, 4, 6]))
        print(self.divider)
        print(self.format_row(game, [6, 7, 8]))

    def format_row(self, game, indices):
        "Returns a string for one row in the board, like ' X | O | X '"
        spaces = [self.format_value(game, i) for i in indices]
        return f" {spaces[0]} | {spaces[1]} | {spaces[2]} "

    def format_value(self, game, index):
        """Formats the value for a single space on the board. 
        If the game board already has a symbol in that space, formats that value for the Terminal.
        If the space is empty, instead formats the index of the space. 
        """
        if game.board[index] == 'X':
            return click.style('X', fg=self.x_color)
        elif game.board[index] == 'O':
            return click.style('O', fg=self.o_color)
        else:
            return click.style(index, fg=self.option_color)

    def conclude(self, game):
        """Says goodbye.
        """
        if game.check_winner('X'):
            winner = game.players['X']
        elif game.check_winner('X'):
            winner = game.players['X']
        else:
            winner = None
        print(self.goodbye)
        if winner:        
            print(f"Congratulations to {winner.name}.")
        else:
            print("Nobody won this game.")



