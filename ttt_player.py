from click import Choice, prompt
import random

class TTTPlayer:
    "A tic tac toe player."

    def __init__(self, name):
        "Sets up the player."
        self.name = name

    def get_symbol(self, game):
        "Returns this player's symbol in the game."
        if game.players['X'] == self:
            return 'X'
        elif game.players['O'] == self:
            return 'O'
        else:
            raise ValueError(f"Player {self.name} isn't in this game!")

class TTTHumanPlayer(TTTPlayer):
    "A human tic tac toe player."

    def choose_move(self, game):
        "Chooses a move by prompting the player for a choice."
        choices = Choice([str(i) for i in game.get_valid_moves()])
        move = prompt("> ", type=choices, show_choices=False)
        return int(move)

class TTTComputerPlayer(TTTPlayer):
    "A computer tic tac toe player"

    def choose_move(self, game):
        "Chooses a random move from the moves available."
        return random.choice(game.get_valid_moves())

