from ttt.game import TTTGame
from ttt.view import TTTView
from ttt.player import TTTHumanPlayer, TTTComputerPlayer

player0 = TTTHumanPlayer("Chris")
player1 = TTTComputerPlayer("Bot")
game = TTTGame()
view = TTTView(player0, player1)

state = game.get_initial_state()
view.greet()
while not game.is_over(state):
    action = view.get_action(state)
    state = game.get_next_state(state, action)
view.conclude(state)
