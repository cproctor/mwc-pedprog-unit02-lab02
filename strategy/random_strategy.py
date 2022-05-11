from random import choice

class RandomStrategy:
    """A Strategy which randomly chooses a move. Not a great choice.
    """
    def __init__(self, game):
        self.game = game

    def choose_action(self, state):
        possible_actions = self.game.get_actions(state)
        return choice(possible_actions)
