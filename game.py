from const import *
from player import Player, RandomPlayer


class Game:
    def __init__(self) -> None:
        self.state = None
        pass

    def reward(self, state, action):
        return 0

    def update_board(self, state):
        '''
        update the board
        '''
        self.state = state
        return


class TikTacToe():
    def __init__(self, p1: Player, p2: Player) -> None:
        self.state = [B] * 9
        self.p1 = p1
        self.p2 = p2
        return

    def reset(self):
        self.state = [B] * 9
        return

    def run(self):
        while True:
            action_p1, new_state = self.p1.take_action(self.state.copy())
            self.state = new_state
            if MODE == DEBUG:
                self.visualize_board(
                    f"Player1({self.p1.label}) take actions: {action_p1}\ncurrent board is")
            if self.is_termination():
                if MODE == DEBUG:
                    self.visualize_board(
                        f"Player1({self.p1.label}) won the game!\nFinal board is")
                self.p1.informed_win(self.state)
                self.p2.informed_lose(self.state)
                break
            if self.no_winner():
                if MODE == DEBUG:
                    self.visualize_board(f'No winner! Final board is')
                self.p1.informed_draw(self.state)
                self.p2.informed_draw(self.state)
                break
            if MODE == TRAIN:
                self.visualize_board(f"Current board is")
            action_p2, new_state = self.p2.take_action(self.state.copy())
            if not MODE == MATCH:
                self.p1.update_value_function(self.state, new_state)
            self.state = new_state
            if MODE == DEBUG:
                self.visualize_board(
                    f"Player2({self.p2.label}) take actions: {action_p2}\ncurrent board is")
            if self.is_termination():
                if MODE == DEBUG:
                    self.visualize_board(
                        f"Player2({self.p2.label}) won the game!\nFinal board is")
                self.p2.informed_win(self.state)
                self.p1.informed_lose(self.state)
                break
            if MODE == DEBUG:
                print()
        return

    def is_termination(self,):
        terminal_patterns = [[0, 3, 6],
                             [1, 4, 7],
                             [2, 5, 8],
                             [0, 1, 2],
                             [3, 4, 5],
                             [6, 7, 8],
                             [0, 4, 8],
                             [2, 4, 6], ]
        for pattern in terminal_patterns:
            if self.state[pattern[0]] == self.state[pattern[1]] and self.state[pattern[1]] == self.state[pattern[2]] and self.state[pattern[0]] in [X, O]:
                return True
        return False

    def no_winner(self,):
        try:
            self.state.index(B)
        except:
            return True
        return False

    def visualize_board(self, message):
        print(message)
        print('----------------')
        print('| {} || {} || {} |'.format(
            self.state[0], self.state[1], self.state[2]))
        print('----------------')
        print('| {} || {} || {} |'.format(
            self.state[3], self.state[4], self.state[5]))
        print('----------------')
        print('| {} || {} || {} |'.format(
            self.state[6], self.state[7], self.state[8]))
        print('----------------')
        return


if __name__ == '__main__':
    # p1 = RandomPlayer(X)
    # p2 = RandomPlayer(O)
    # game = TikTacToe(p1, p2)
    # game.run()
    pass
