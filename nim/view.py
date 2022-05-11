from nim.game import NimGame

class NimView:
    def __init__(self, player0, player1):
        self.players = [player0, player1]
        self.game = NimGame()

    def greet(self):
        print(f"{self.players[0].name} and {self.players[1].name}, welcome to Nim.")
    
    def show_board(self, state):
        for lines_in_row in state["board"]:
            print("| " * lines_in_row)

    def get_action(self, state):
        self.show_board(state)
        player = self.get_current_player(state)
        return player.choose_action(state)

    def get_current_player(self, state):
        if state["first_player"]:
            return self.players[0]
        else:
            return self.players[1]

    def conclude(self, state):
        self.show_board(state)
        if self.game.get_reward(state) > 0:
            winner = self.players[0]
        else:
            winner = self.players[1]
        print(f"Congratulations, {winner.name}!")
