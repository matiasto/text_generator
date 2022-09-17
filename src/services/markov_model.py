from random import choice


class MarkovModel:
    """Creates the Markov chain from the cleaned text

    Attributes:
        cleaned_text (str): The cleaned text
        order (int): The order of the Markov chain
        model (dict): The Markov chain
        train (func): Trains the Markov chain
    """

    def __init__(self, cleaned_text: list, order=2) -> None:
        """Initializes the Markov chain

        Args:
            cleaned_text (list): The cleaned text
            order (int, optional): The order/degree of Markov chain.
                                    Defaults to 2.
        """

        self.__cleaned_text = cleaned_text
        self.__order = order
        self.__model = {}
        self.__train()

    @property
    def model(self) -> dict:
        """Returns the Markov chain in dictionary format"""

        return self.__model

    def get_random_starting_word(self) -> str:
        """Returns a random starting word from the Markov chain"""

        return choice(list(self.__model.keys()))

    def __build_model(self) -> None:
        """Builds the Markov chain

        Loops through the cleaned text and adds the current word and the next
        word to the Markov chain. If the current word is not in the Markov
        chain, it is added to the Markov chain with the next word as the value.
        The value is a dictionary with the next word as the key and the number
        of times the next word has appeared after the current word as the value.
        """

        for i in range(len(self.__cleaned_text) - self.__order - 1):
            current_state = ""
            next_state = ""
            for j in range(self.__order):
                current_state += self.__cleaned_text[i+j] + " "
                next_state += self.__cleaned_text[i+j+self.__order] + " "
            current_state = current_state[:-1]
            next_state = next_state[:-1]
            if current_state not in self.__model:
                self.__model[current_state] = {}
                self.__model[current_state][next_state] = 1
            else:
                if next_state in self.__model[current_state]:
                    self.__model[current_state][next_state] += 1
                else:
                    self.__model[current_state][next_state] = 1

    def __calculate_probability(self) -> None:
        """Calculates the probability of each word in the Markov chain

        Loops through the Markov chain and calculates the probability of each
        word by dividing the number of times the word has appeared after the
        current word by the total number of words that have appeared after the
        current word.
        """

        for current_state, transition in self.__model.items():
            total = sum(transition.values())
            for state, count in transition.items():
                self.__model[current_state][state] = count / total

    def __train(self) -> None:
        """Trains the Markov chain

        Builds the Markov chain and calculates the probability of each word
        """

        self.__build_model()
        self.__calculate_probability()
