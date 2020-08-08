import numpy as np
from model import NN


class Agent:
    def __init__(self):
        self.neural_network = NN()

        # Ensure trainer share same weight
        weights = self.neural_network.model.get_weights()
        # TODO: send weights to trainer

    @staticmethod
    def get_action(state):
        action = np.random.randint(0, 2)
        return action

    def update_model(self, train_episode, total_episode):
        # Alert agent
        self.alert_agent(train_episode, total_episode)
        self.neural_network.model.set_weights(self.get_weights())

    def alert_agent(self, train_episode, total_episode):
        train_episode = train_episode
        is_training_completed = train_episode == total_episode - 1
        # TODO: Send the # of training episode to agent
        pass

    def get_weights(self):
        weights = self.neural_network.model.get_weights()  # Extract weight from trainer
        return weights
