from nim_game import NimGame
from nim_view import NimView
from nim_player import HumanNimPlayer, ComputerNimPlayer

player0 = HumanNimPlayer(input("What's your name? "))
player1 = ComputerNimPlayer("BOT")
view = NimView(player0, player1)
game = NimGame()

view.greet()
state = game.get_initial_state()
while not game.is_over(state):
    action = view.get_action(state)
    state = game.get_next_state(state, action)
view.conclude(state)
