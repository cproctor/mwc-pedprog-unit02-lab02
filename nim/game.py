class NimGame:
    def get_initial_state(self):
        return {
            "board": [1, 3, 5, 7],
            "first_player": True
        }

    def get_next_state(self, state, action):
        new_state = {
            "board": state["board"].copy(),
            "first_player": not state["first_player"],
        }
        row, lines_removed = action
        new_state["board"][row] -= lines_removed
        return new_state
    
    def get_actions(self, state):
        actions = []
        for row_num, lines_in_row in enumerate(state["board"]):
            for lines_to_remove in [1,2,3]:
                if lines_to_remove <= lines_in_row:
                    actions.append((row_num, lines_to_remove))
        return actions

    def get_reward(self, state):
        if self.is_over(state):
            return 1 if state["first_player"] else -1    
        else:
            return 0

    def is_over(self, state):
        return sum(state["board"]) == 0

    def get_objective(self, state):
        return max if state["first_player"] else min
