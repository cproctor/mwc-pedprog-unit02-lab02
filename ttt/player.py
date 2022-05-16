from click import Choice, prompt
from strategy.random_strategy import RandomStrategy
from strategy.lookahead_strategy import LookaheadStrategy
from ttt.game import TTTGame
import random

class TTTHumanPlayer:
    "A human tic tac toe player."

    def __init__(self, name):
        "Sets up the player."
        self.name = name
        self.game = TTTGame()

    def choose_action(self, state):
        "Chooses an action by prompting the player for a choice."
        actions = self.game.get_actions(state)
        choices = Choice([str(action) for action in actions])
        action = int(prompt("> ", type=choices, show_choices=False))
        return action

class TTTComputerPlayer:
    "A computer tic tac toe player"

    def __init__(self, name):
        "Sets up the player."
        self.name = name
        self.strategy = LookaheadStrategy(TTTGame())

    def choose_action(self, state):
        "Chooses a random move from the moves available."
        action = self.strategy.choose_action(state)
        print(f"{self.name} chooses {action}.")
        return action
