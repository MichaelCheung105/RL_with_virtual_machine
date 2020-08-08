from keras.models import Sequential
from keras.layers import Dense


class NN:
    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_shape=(3,)))
        self.model.add(Dense(2, activation='linear'))
        self.model.compile(optimizer='adam', loss='mse')