import numpy as np
from socket_communicator import SocketCommunicator
from model import NN

host = 'enter host name'
port = 'enter host port'


class Agent:
    def __init__(self):
        # Setup communication channel with trainer
        self.trainer_interface = SocketCommunicator(socket_type='server', host=host, port=port)

        # Initiate NN and ensure trainer share same weight
        self.neural_network = NN()
        weights = self.neural_network.model.get_weights()
        # TODO: send weights to trainer

    @staticmethod
    def get_action(state):
        action = np.random.randint(0, 2)
        return action

    def update_model(self, train_episode, total_episode):
        # Alert agent
        self.alert_agent(train_episode, total_episode)
        self.neural_network.model.set_weights(self.get_weights_from_trainer())

    def alert_agent(self, train_episode, total_episode):
        episode_remained = total_episode - train_episode
        try:
            self.trainer_interface.send_message(bytes(str(episode_remained), "utf-8 "))
            print("Sent episode_remained to trainer")
        except Exception as e:
            print("Failed to send episode_remained to trainer. See error message below")
            print(e)
            print("Continue the game")

    def get_weights_from_trainer(self):
        weights = self.neural_network.model.get_weights()  # TODO Extract weight from trainer
        return weights
