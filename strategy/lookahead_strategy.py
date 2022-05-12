from types import MethodType
from random import choice

class LookaheadStrategy:
    """A Strategy which considers the future consequences of an action.

    To initialize a LookaheadStrategy, pass in an instance of a game containing
    the following methods. These methods encode the rules of the game, 
    which a LookaheadStrategy needs to know in order to determine which move is best.

        - get_next_state: state, action -> state
        - get_actions: state -> [actions]
        - get_reward: state -> int
        - is_over: state -> bool
        - get_objective: str -> function

    Optionally, pass the following arguments to control the behavior of the LookaheadStrategy:

        - max_depth: int. A game may be too complex to search the full state tree.
          Setting max_depth will set a cutoff on how far ahead the LookaheadStrategy will look.
        - deterministic: bool. It's possible that there are multiple equally-good actions. 
          When deterministic is True, LookaheadStrategy will always choose the first of the 
          equally-good actions, so that LookaheadStrategy will always play out the same game. 
          When deterministic is False, LookaheadStrategy will choose randomly from all actions
          which are equally-good. 
        - Explain: When set to True, LookaheadStrategy will print out its reasoning. 
    """

    def __init__(self, game, max_depth=None, deterministic=True, explain=False):
        self.validate_game(game)
        self.game = game
        self.max_depth = max_depth
        self.deterministic = deterministic
        self.explain = explain

    def choose_action(self, state, depth=0):
        """Given a state, chooses an action.
        This is the most important method of a Strategy, corresponding to the situation where
        it's a player's turn to play a game and she needs to decide what to do. 

        Strategy chooses an action by considering all possible actions, and finding the 
        total current and future reward which would come from playing that action. 
        Then we use the game's objective to choose the "best" reward. Usually bigger is better, 
        but in zero-sum games like tic tac toe, the players want opposite outcomes. One player
        wants the reward to be high, while the other wants the reward to be low.

        Once we know which reward is best, we choose an action which will lead to that reward.
        """
        possible_actions = self.game.get_actions(state)
        rewards = {}
        for action in possible_actions:
            future_state = self.game.get_next_state(state, action)
            rewards[action] = self.get_current_and_future_reward(future_state, depth=depth)
        objective = self.game.get_objective(state)
        best_reward = objective(rewards.values())
        best_actions = [action for action in possible_actions if rewards[action] == best_reward]
        if self.deterministic:
            action = best_actions[0]
        else:
            action = choice(best_actions)
        if self.explain:
            self.print_explanation(state, action, rewards[action], depth)
        return action

    def get_current_and_future_reward(self, state, depth=0):
        """Calculates the reward from this state, and from all future states which would be 
        reached, assuming all players are using this Strategy.
        """
        reward = self.game.get_reward(state)
        if (self.max_depth is None or depth <= self.max_depth) and not self.game.is_over(state):
            action = self.choose_action(state, depth=depth+1)
            future_state = self.game.get_next_state(state, action)
            reward += self.get_current_and_future_reward(future_state, depth=depth+1)
        return reward

    def validate_game(self, game):
        "Checks that the game has all the required methods."
        required_methods = [
            "get_next_state",
            "get_actions",
            "get_reward",
            "is_over",
            "get_objective",
        ]
        for method in required_methods:
            if not (hasattr(game, method) and isinstance(getattr(game, method), MethodType)):
                message = f"Game {game} does not have method {method}."
                raise ValueError(message)

    def print_explanation(self, state, action, reward, depth):
        """Prints out the current state of exploration of the state tree"""
        indent = '│ ' * (max(0, depth-1)) + ('├ ' if depth > 0 else '')
        print(f"{indent}[{reward}] Best action: {action} {state}")



