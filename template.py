from abc import ABC, abstractmethod


class Policy(ABC):

    @abstractmethod
    def select_action(self, state, action):
        pass





class DeterministicPolicy(Policy):
    def update(self, state, action):
        pass





class StochasticPolicy(Policy):
    def update(self, states, actions, rewards):
        pass

    def get_probability(self, state, action):
        pass