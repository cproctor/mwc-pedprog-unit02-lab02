from ttt_game import TTTGame
from ttt_view import TTTView
from ttt_player import TTTHumanPlayer

player0 = TTTHumanPlayer("Player 1")
player1 = TTTHumanPlayer("Player 2")
game = TTTGame(player0, player1)
view = TTTView()

view.greet(game)
while not game.is_over():
    move = view.get_move(game)
    game.play_move(move)
view.conclude(game)
