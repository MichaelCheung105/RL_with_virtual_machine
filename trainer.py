import numpy as np
from model import NN
from socket_communicator import SocketCommunicator
from sql_database import SqlDB

host = 'enter host name'
port = 'enter host port'


class Trainer:
    def __init__(self):
        self.agent_interface = SocketCommunicator(socket_type='client', host=host, port=port)
        self.neural_network = NN()
        self.experience_pool = SqlDB()
        self.model_training_count = 0

    def init_weights(self):
        # TODO: Wait for weights from runner (set timer for stop waiting and kill itself)
        weights = self.neural_network.model.get_weights()
        self.neural_network.model.set_weights(weights)

    def start(self):
        self.init_weights()

        while True:
            print("Awaiting episode_remained from server")
            episode_remained = self.agent_interface.receive_message().decode("utf-8")
            episode_remained = int(episode_remained)
            print("Episode remained: {0}".format(episode_remained))

            if episode_remained % 3 == 0:
                self.train_model()

            if episode_remained == 0:
                break

        print("All training is completed. Killing this programme")

    def train_model(self):
        experiences = self.experience_pool.extract_experience_pool(table_name='exp_pool_1')
        print("Sample experience: {0}".format(experiences[0]))
        # use the experiences to train model
        self.model_training_count += 1
        # weights = self.neural_network.model.get_weights()
        # self.agent_interface.send_message(weights)
        print("Trained model for {0} time(s)".format(self.model_training_count))


if __name__ == "__main__":
    trainer = Trainer()
    trainer.start()
