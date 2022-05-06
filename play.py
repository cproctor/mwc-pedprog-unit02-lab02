from ttt_game import TTTGame
from ttt_view import TTTView
from ttt_player import TTTHumanPlayer, TTTComputerPlayer

player0 = TTTHumanPlayer("Player 1")
player1 = TTTComputerPlayer("Player 2")
game = TTTGame(player0, player1)
view = TTTView()

view.greet(game)
while not game.is_over(game.state):
    action = view.get_action(game)
    game.play_action(action)
view.conclude(game)
