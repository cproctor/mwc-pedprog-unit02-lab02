
# A state is a dictionary with two keys, "board" and "player." Here's an example:
# 
# {
#     "board": [None, None, "X", None, "O", None, "X", "O", None],
#     "player": "X",
# }

from itertools import count
counter = count()

def get_actions(state):
    """Given a board state, returns a dictionary whose keys are possible actions and whose 
    values are the resulting state from each action. If the game is over, returns an empty
    dictionary because no further moves are possible.
    """
    if is_over(state):
        return {}
    else:
        actions = {}
        for i in range(9):
            if state["board"][i] is None or state["board"][i] == ' ':
                actions[i] = get_next_state(state, i)
        return actions

def choose_best_action(state, depth=0, explain=False):
    """Given a state, returns the best action, its resulting state, and that state's value.
    For each possible action, we find the value of the resulting state. 
    Then, if the player is 'X', choose the action corresponding to the highest
    value. If the player is 'O', choose the action corresponding to the lowest
    value. 
    """
    if explain:
        question_number = next(counter)
        pose_question(state, question_number, depth)
    actions = get_actions(state)
    values_and_actions = []
    for action, result in actions.items():
        values_and_actions.append([get_value(result, depth=depth, explain=explain), action])
    if state["player"] == "X":
        value, action = max(values_and_actions)
    else:
        value, action = min(values_and_actions)
    if explain:
        answer_question(state, action, question_number, depth)
    return action, actions[action], value

def get_value(state, depth=0, explain=False):
    """Determines the value of the state.
    """
    if is_win(state, 'X'):
        return 1
    elif is_win(state, 'O'):
        return -1
    elif is_draw(state):
        return 0
    else:
        action, result, value = choose_best_action(state, depth=depth+1, explain=explain)
        return value
        
# =========================================================================================
# ================================== HELPERS ==============================================
# =========================================================================================

def pose_question(state, index, depth):
    "Logs a question asking about a player's best move at a state."
    board = format_board_inline(state['board'])
    log(f"What is the best action for {state['player']} at {board}?", index, depth)

def answer_question(state, action, index, depth):
    "Logs the answer to a question about a player's best move at a state."
    board = format_board_inline(state['board'])
    log(f"The best action for {state['player']} at {board} is {action}", index, depth)
        
def log(message, index, depth):
    "Prints a message at the appropriate depth, with each message numbered."
    indent = '  ' * depth
    print(f"{indent}{index}. {message}")
