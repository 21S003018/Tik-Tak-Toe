from player import HumanPlayer, RandomPlayer
from models import ReinfrocementLearningPlayer
from const import *
from game import TikTacToe
p1 = ReinfrocementLearningPlayer(X)
# p2 = RandomPlayer(O)
p2 = HumanPlayer(O)
game = TikTacToe(p1, p2)
p1.set_env(game)
W = "win"
D = "draw"
L = "lose"
ROUNDS = 1
rates = {W: 0, D: 0, L: 0}
for i in range(ROUNDS):
    if i % 100 == 0:
        print(f'iter{i}')
    game.run()
    if game.no_winner():
        rates[D] += 1
    elif game.state.count(X) > game.state.count(O):
        rates[W] += 1
    else:
        rates[L] += 1
    game.reset()

print(rates)
