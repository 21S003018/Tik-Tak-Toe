from typing import List

import random as rd
from const import *


class Player:
    def __init__(self) -> None:
        pass

    def take_action(self, state):
        return

    def informed_win(self, final_state):
        return

    def informed_lose(self, final_state):
        return

    def informed_draw(self, final_state):
        return


class RandomPlayer(Player):
    def __init__(self, label=X) -> None:
        self.label = label
        return

    def take_action(self, state):
        '''
        take action randomly
        return current action and the next state
        '''
        pos = rd.randint(0, 8)
        while state[pos] in [X, O]:
            pos = rd.randint(0, 8)
        state[pos] = self.label
        return pos, state.copy()


class HumanPlayer(Player):
    def __init__(self, label) -> None:
        self.label = label
        return

    def take_action(self, state: List[int]):
        pos = int(input('Please input a position: '))
        while state[pos] in [X, O]:
            pos = int(input('Occupied! Input again: '))
        state[pos] = self.label
        return pos, state


if __name__ == '__main__':
    p1 = RandomPlayer()
    game_state = [0, 0, 0,
                  0, 0, 0,
                  0, 0, 0]
    print(p1.take_action(game_state))
    print(p1.take_action(game_state))
    print(p1.take_action(game_state))
    print(p1.take_action(game_state))
    print(p1.take_action(game_state))
