from ttt.game import TTTGame
from ttt.view import TTTView
from ttt.player import TTTHumanPlayer

player0 = TTTHumanPlayer("Player 1")
player1 = TTTHumanPlayer("Player 2")
game = TTTGame()
view = TTTView(player0, player1)

state = game.get_initial_state()
view.greet()
while not game.is_over(state):
    action = view.get_action(state)
    state = game.get_next_state(state, action)
view.conclude(state)
