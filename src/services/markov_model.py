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

    def __init__(self, cleaned_text: list, degree: int) -> None:
        """Initializes the Markov chain

        Args:
            cleaned_text (list): The cleaned text
            order (int, optional): The order/degree of Markov chain.
        """

        self.__cleaned_text = cleaned_text
        self.__degree = degree
        self.__model = Trie()
        self.__train()

    @property
    def degree(self) -> int:
        """Returns the degree of the Markov chain"""

        return self.__degree

    @property
    def model(self) -> dict:
        """Returns the Markov chain in dictionary format"""

        return self.__model

    def get_random_starting_sequence(self) -> str:
        """Returns a random starting sequence from the Trie data structure"""

        sequence = []
        for _ in range(self.__degree):
            children = self.__model.get_children(sequence)
            sequence.append(choice(list(children.keys())))
        return sequence

    def __build_model(self) -> None:
        """Builds the Markov chain"""

        order = self.__degree + 1
        for i in range(len(self.__cleaned_text) - order):
            state = tuple(self.__cleaned_text[i:i + order])
            self.__model.insert(state)

    def __train(self) -> None:
        """Trains the Markov chain

        Builds the Markov chain and adds the frequencies of each state
        """

        self.__build_model()
