from random import choice
from entities import Trie


class MarkovModel:
    """Creates the Markov chain from the cleaned text

    Attributes:
        cleaned_text (str): The cleaned text
        order (int): The order of the Markov chain
        model (dict): The Markov chain
        train (func): Trains the Markov chain
    """

    def __init__(self, cleaned_text: list, order: int) -> None:
        """Initializes the Markov chain

        Args:
            cleaned_text (list): The cleaned text
            order (int, optional): The order/degree of Markov chain.
        """

        self.__cleaned_text = cleaned_text
        self.__order = order
        self.__model = Trie()
        self.__train()

    @property
    def model(self) -> dict:
        """Returns the Markov chain in dictionary format"""

        return self.__model

    def get_random_starting_sequence(self) -> str:
        """Returns a random starting sequence from the Trie data structure"""

        sequence = []
        for _ in range(self.__order):
            children = self.__model.get_children(sequence)
            sequence.append(choice(list(children.keys())))
        return sequence

    def __build_model(self) -> None:
        """Builds the Markov chain"""

        order = self.__order + 1
        for i in range(len(self.__cleaned_text) - order):
            state = tuple(self.__cleaned_text[i:i + order])
            self.__model.insert(state)

    def __train(self) -> None:
        """Trains the Markov chain

        Builds the Markov chain and adds the frequencies of each state
        """

        self.__build_model()
