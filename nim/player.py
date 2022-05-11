from nim.game import NimGame
from strategy.lookahead_strategy import LookaheadStrategy

class HumanNimPlayer:
    def __init__(self, name):
        self.name = name
        self.game = NimGame()

    def choose_action(self, state):
        actions = self.game.get_actions(state)
        for i, action in enumerate(actions):
            row, lines_to_remove = action
            print(f"{i}. Remove {lines_to_remove} from row {row}.")
        choice = self.get_int(len(actions))
        return actions[choice]

    def get_int(self, maximum):
        while True:
            response = input("> ")
            if response.isdigit():
                value = int(response)
                if value < maximum:
                    return value
            print("Invalid input.")

class ComputerNimPlayer:
    def __init__(self, name):
        self.name = name
        self.strategy = LookaheadStrategy(NimGame(), max_depth=3, deterministic=False)

    def choose_action(self, state):
        action = self.strategy.choose_action(state)
        row, lines_to_remove = action
        print(f"{self.name} removes {lines_to_remove} from row {row}")
        return action
