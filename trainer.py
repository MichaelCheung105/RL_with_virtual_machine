import numpy as np
from model import NN
from sql_database import SqlDB


class Trainer:
    def __init__(self):
        self.neural_network = NN()
        self.experience_pool = SqlDB()

    def init_weights(self):
        # TODO: Wait for weights from runner (set timer for stop waiting and kill itself)
        weights = self.neural_network.model.get_weights()
        self.neural_network.model.set_weights(weights)

    def start(self):
        self.init_weights()
        is_training_complete = False
        while not is_training_complete:
            # wait for number of episodes and whether training is complete
            train_episode = np.random.randint(5)
            is_training_complete = False
            if not is_training_complete and train_episode % 3 == 0:
                self.train_model()

        print("All training is completed. Killing this programme")

    def train_model(self):
        experiences = self.experience_pool.extract_experience_pool(table_name='exp_pool_1')
        pass


if __name__ == "__main__":
    trainer = Trainer()
    trainer.start()
