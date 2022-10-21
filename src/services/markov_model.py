from random import choice
from entities import Trie


class MarkovModel:
    """Creates the Markov chain from the cleaned text

    Attributes:
        cleaned_text (str): The cleaned text
        degree (int): The order/degree of Markov chain.
        model (dict): The Markov chain
        build_model (func): Builds the Markov chain
    """

    def __init__(self, cleaned_text: list, degree: int) -> None:
        """Initializes the Markov chain

        Args:
            cleaned_text (list): The cleaned text
            degree (int): The order/degree of Markov chain.
        """

        self.__cleaned_text = cleaned_text
        self.__degree = degree
        self.__model = Trie()
        self.__build_model()

    @property
    def degree(self) -> int:
        """Returns the degree of the Markov chain"""

        return self.__degree

    @property
    def model(self) -> dict:
        """Returns the trained Markov model"""

        return self.__model

    def form_the_starting_sequence(self, sequence):
        """Adds the missing words in a sequence

        generates missing words in a sequence based 
        on the degree of the model.

        Args:
            sequence (list): The sequence to check
        """

        while len(sequence) < self.__degree:
            children = self.__model.get_children(sequence)
            if not children:
                return []
            sequence.append(choice(list(children.keys())))
        return sequence

    def __build_model(self) -> None:
        """Builds the Markov chain"""

        order = self.__degree + 1
        for i in range(len(self.__cleaned_text) - order):
            state = tuple(self.__cleaned_text[i:i + order])
            self.__model.insert(state)
