import json
from typing import List
import random as rd

from torch import randint
from player import RandomPlayer, Player
from const import *
from game import TikTacToe
import pickle


class ReinfrocementLearningPlayer(Player):
    def __init__(self, label=X, value_function_path='q_table.pkl') -> None:
        self.label = label
        self.value_function_path = value_function_path
        try:
            with open(value_function_path, 'rb') as f:
                self.value_function = pickle.load(f)
        except:
            self.value_function = {}
        return

    def set_env(self, game_env: TikTacToe):
        self.env = game_env
        self.value_function[self._hash(self.env.state)] = 0
        return

    def take_action(self, state):
        # get successors
        candidates = self._get_successors(state)
        candidates_value_function = [
            self.value_function[self._hash(a_s[1])] for a_s in candidates]
        # policy
        if MODE == DEBUG:
            print(candidates)
            print(candidates_value_function)
        if not MODE == TRAIN:
            exploit_rate = 1
        else:
            exploit_rate = 0.8

        if rd.random() < exploit_rate:
            action, next_state = candidates[candidates_value_function.index(
                max(candidates_value_function))]
        else:
            action, next_state = candidates[rd.randint(0, len(candidates)-1)]
        # update value function
        if not MODE == MATCH:
            self.update_value_function(state, next_state)
        return action, next_state

    def update_value_function(self, state, next_state):
        if not self.value_function.__contains__(self._hash(state)):
            self.value_function[self._hash(state)] = 0
        if not self.value_function.__contains__(self._hash(next_state)):
            self.value_function[self._hash(next_state)] = 0
        gamma = 0.2
        self.value_function[self._hash(
            state)] = self.value_function[self._hash(state)] + gamma * (self.value_function[self._hash(next_state)] - self.value_function[self._hash(state)])
        return

    def informed_win(self, final_state):
        self.value_function[self._hash(final_state)] = 1
        self.ending()
        return

    def informed_lose(self, final_state):
        self.value_function[self._hash(final_state)] = -1
        self.ending()
        return

    def informed_draw(self, final_state):
        self.value_function[self._hash(final_state)] = 0.5
        self.ending()
        return

    def ending(self):
        with open(self.value_function_path, 'wb') as f:
            pickle.dump(self.value_function, f)
        with open('q_table.json', 'w') as f:
            json.dump(self.value_function, f)
        return

    def _get_successors(self, state: List):
        if not self.value_function.__contains__(self._hash(state)):
            self.value_function[self._hash(state)] = 0
        ret = []
        for i in range(9):
            if state[i] == B:
                tmp = state.copy()
                tmp[i] = self.label
                ret.append((i, tmp))
                if not self.value_function.__contains__(self._hash(tmp)):
                    self.value_function[self._hash(tmp)] = 0
        return ret

    def _hash(self, state: List):
        return ','.join(state)


if __name__ == '__main__':
    # model = ReinfrocementLearningPlayer()
    # print(model.take_action([B]*9))
    with open('q_table.pkl', 'rb') as f:
        value_function = pickle.load(f)
    print(value_function['X,X,O,X,X,O,O,O,X'])
    pass
