from click import confirm
from strategy import LookaheadStrategy

class PegSolitaire:
    """Models a one-player peg solitaire game.
    On each turn, the player jumps a peg over another peg to an empty space, 
    and removes the jumped peg. The goal is to end the game with a single peg
    in the original empty space.

    This game serves as an example of how to implement a game which plays nicely with
    LookaheadStrategy by implementing the required methods.
    """

    def __init__(self):
        self.state = self.get_initial_state()

    def get_initial_state(self):
        """All we need to know for peg solitaire is what's on the board, 
        so the state can simply be a list of lists representing the contents
        of the rectangular board. 1 represents a peg, 
        0 represents an empty space, and 2 represents a solid block 
        not available for play (this allows us to create a non-rectangular board).
        """
        return [
            [2,2,2,1,1,1,2,2,2],
            [2,2,2,1,1,1,2,2,2],
            [2,2,2,1,1,1,2,2,2],
            [1,1,1,1,1,1,1,1,1],
            [1,1,1,1,0,1,1,1,1],
            [1,1,1,1,1,1,1,1,1],
            [2,2,2,1,1,1,2,2,2],
            [2,2,2,1,1,1,2,2,2],
            [2,2,2,1,1,1,2,2,2],
        ]

    def get_next_state(self, state, action):
        """An action consists of two integers and a string: The row index (j), 
        the column index (i), and the direction, represented by "UP", "DOWN", "LEFT",
        or "RIGHT".
        """
        new_state = self.copy_state(state)
        row, col, direction = action
        jumped_row, jumped_col = self.get_jumped_peg(state, action)
        dest_row, dest_col = self.get_jump_destination(state, action)
        new_state[row][col] = 0
        new_state[jumped_row][jumped_col] = 0
        new_state[dest_row][dest_col] = 1
        return new_state

    def play_action(self, action):
        self.state = self.get_next_state(self.state, action)

    def get_actions(self, state):
        """Finds all possible actions by testing each direction at each 
        possible space on the board.
        """
        num_rows, num_cols = self.get_board_dimensions(state)
        actions = []
        for col in range(num_cols):
            for row in range(num_rows):
                for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
                    action = (row, col, direction)
                    jumped_row, jumped_col = self.get_jumped_peg(state, action)
                    dest_row, dest_col = self.get_jump_destination(state, action)
                    if (
                        self.is_on_board(state, row, col) and 
                        self.is_on_board(state, dest_row, dest_col) and 
                        self.has_peg(state, row, col) and 
                        self.has_peg(state, jumped_row, jumped_col) and 
                        self.is_empty(state, dest_row, dest_col)
                    ):
                        actions.append(action)
        return actions

    def is_over(self, state):
        actions = self.get_actions(state)
        #print(actions)
        return len(self.get_actions(state)) == 0

    def get_reward(self, state):
        """A game ending with a single peg is worth 1, a win. 
        A game ending with more than one peg is worth -1, a loss.
        An unfinished game is worth 0.
        """
        if self.is_over(state):
            if self.count_pegs(state) == 1:
                return 1
            else:
                return -1
        else:
            return 0

    def get_objective(self, state):
        "The objective is always to get the highest reward."
        return max
            
    def copy_state(self, state):
        return [row.copy() for row in state]

    def get_jump_destination(self, state, action):
        """An action encodes the starting place of a jump and the direction.
        Returns the coordinates of the ending place of the jump.
        """
        row, col, direction = action
        if direction == "UP":
            return row - 2, col
        elif direction == "DOWN":
            return row + 2, col
        elif direction == "LEFT":
            return row, col - 2
        elif direction == "RIGHT":
            return row, col + 2

    def get_jumped_peg(self, state, action):
        """An action encodes the starting place of a jump and the direction.
        Returns the coordinates of the jumped peg.
        """
        row, col, direction = action
        if direction == "UP":
            return row - 1, col
        elif direction == "DOWN":
            return row + 1, col
        elif direction == "LEFT":
            return row, col - 1
        elif direction == "RIGHT":
            return row, col + 1

    def get_board_dimensions(self, state):
        """Calculates the dimensions of the board"""
        num_rows = len(state)
        num_cols = len(state[0])
        return num_rows, num_cols

    def is_on_board(self, state, row, col):
        row_max, col_max = self.get_board_dimensions(state)
        in_rect = (0 <= row and row < row_max and 0 <= col and col < col_max)
        if in_rect:
            return state[row][col] != 2
        else:
            return False

    def is_empty(self, state, row, col):
        "Calculates whether a space is empty"
        #print("CHECKING IF EMPTY:", row, col)
        return state[row][col] == 0

    def has_peg(self, state, row, col):
        "Calculates whether a space has a peg"
        return state[row][col] == 1

    def count_pegs(self, state):
        "Counts how many pegs are on the board"
        num_pegs = 0
        for row in state:
            for space in row:
                if space == 1:
                    num_pegs += 1
        return num_pegs

class PegSolitareView:
    """A simple--but terrible--user interface."""
    symbols = [' ', '*', 'X']

    def greet(self, game, player):
        print(f"Hello, {player.name}")

    def show_board(self, state):
        for row in state:
            row_symbols = [self.symbols[num] for num in row]
            print(' '.join(row_symbols))

    def get_action(self, game, player):
        self.show_board(game.state)
        return player.choose_action(game)

    def conclude(self, game):
        self.show_board(game.state)
        if game.get_reward(game.state) == 1:
            print("Congratulations!")
        else:
            print("Better luck next time")

class PegSolitaireHumanPlayer:
    def __init__(self, name):
        self.name = name

    def choose_action(self, game):
        print("PLEASE CHOOSE AN ACTION")
        actions = game.get_actions(game.state)
        self.show_actions(actions)
        choice = self.get_int(len(actions))
        return actions[choice]

    def show_actions(self, actions):
        for i, action in enumerate(actions): 
            row, col, direction = action
            print(f"{i}. ({row}, {col}) -> {direction}")

    def get_int(self, maximum):
        while True:
            response = input("> ")
            if response.isdigit():
                value = int(response)
                if value < maximum:
                    return value
            print("Invalid input.")

class PegSolitaireComputerPlayer:
    def __init__(self):
        self.name = "BOT"
        self.strategy = LookaheadStrategy(PegSolitaire(), max_depth=2)

    def choose_action(self, game):
        action = self.strategy.choose_action(game.state)
        print(f"{self.name} chooses {action}.")
        return action

if __name__ == '__main__':
    if confirm("Use computer player?"):
        player = PegSolitaireComputerPlayer()
    else:
        name = input("What's your name? ")
        player = PegSolitaireHumanPlayer(name)
    game = PegSolitaire()
    view = PegSolitareView()
    view.greet(game, player)
    while not game.is_over(game.state):
        action = view.get_action(game, player)
        game.play_action(action)
    view.conclude(game)
