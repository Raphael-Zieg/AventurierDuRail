import gym
import numpy as np
import random
import tensorflow as tf
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation="relu"))
        model.add(Dense(24, activation="relu"))
        model.add(Dense(self.action_size, activation="linear"))
        model.compile(loss="mse", optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # returns action

    # ... autres méthodes incluant train, replay ...


if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    agent = DQNAgent(state_size, action_size)

    # Boucle d'entraînement
    for e in range(EPISODES):
        # Réinitialiser l'état pour chaque épisode
        state = env.reset()
        state = np.reshape(state, [1, state_size])

        for time in range(500):
            # Choisir l'action
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            reward = reward if not done else -10
            # Reshape next_state for the model
            next_state = np.reshape(next_state, [1, state_size])

            # Remember the previous state, action, reward, and next state
            agent.remember(state, action, reward, next_state, done)

            # Make next_state the new current state for the next frame.
            state = next_state

            if done:
                print(f"Episode: {e}/{EPISODES}, score: {time}, e: {agent.epsilon:.2}")
                break

            # Train the agent with the experience of the episode
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)

        # Reduce epsilon (because we need less and less exploration)
        if agent.epsilon > agent.epsilon_min:
            agent.epsilon *= agent.epsilon_decay
