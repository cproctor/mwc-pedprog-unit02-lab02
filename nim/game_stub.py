class NimGameStub:
    """A stub is a minimal version of a class which stands in for the 
    real class, which hasn't yet been written. The stub has all the correct 
    methods, and their inputs and outputs are the right kind of thing, 
    but it doesn't really do anything. 
    """
    def get_initial_state(self):
        return {
            "board": [1, 3, 5, 7],
            "first_player": True
        }

    def get_next_state(self, state, action):
        next_state = {
            "board": state["board"].copy(),
            "first_player": not state["first_player"],
        }
        return next_state

    def get_actions(self, state):
        return [
            (0, 0), 
            (1, 0), (1, 1),
            (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3),
        ]

    def get_reward(self, state):
        return 0

    def is_over(self, state):
        return False

    def get_objective(self, state):
        return max if state["first_player"] else min
