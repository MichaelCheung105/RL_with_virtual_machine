import numpy as np


class Environment:
    def __init__(self):
        pass

    @staticmethod
    def init_state():
        state = np.random.rand(3)
        return state

    @staticmethod
    def step(action):
        reward = np.random.randint(low=-1, high=2)
        next_state = np.random.rand(3)
        done = False
        return reward, next_state, done
