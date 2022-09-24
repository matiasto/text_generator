from random import choices


class GenerateService:
    """Generates text based on the model

    Given a start state and a model, generates text based on the model.

    Attributes:
        start_state (str): The starting state of the model
        limit (int): The number of words to be generated
        model (dict): The model to be used for generating text
        order (int): The order of the model
        generated_text (str): The generated text
        generate (function): The function that generates the text
    """

    def __init__(self, start_state: str, model: object, order: int, limit=10) -> None:
        """Inits GenerateService with the start state, model and limit

        Args:
            start_state (str): The starting state of the model
            model (dict): The model to be used for generating text
            order (int): The order of the model
            limit (int, optional): The limit of how many keys are
                                    picked from the model. Defaults to 10.
        """

        self.__start_state = start_state
        self.__limit = limit
        self.__model = model
        self.__order = order
        self.__generated_text = ""
        self.__generate()

    def __calculate_probability(self, children: dict) -> dict:
        """Calculates the probability of children

        Args:
            children (dict): The children of the current state

        Returns:
            dict: The probability of each word
        """

        total = sum([i.frequency for i in children.values()])
        return {word: value.frequency / total for word, value in children.items()}

    @property
    def generated_text(self) -> str:
        """Returns the generated text as string"""

        return self.__generated_text

    def __generate(self) -> None:
        """Generates text based on the model"""

        sequence = self.__start_state
        for _ in range(self.__limit):
            children = self.__model.get_children(sequence[-self.__order:])
            probability = self.__calculate_probability(children)
            word = choices(list(probability.keys()),
                           list(probability.values()))[0]
            sequence.append(word)
        self.__generated_text = " ".join(sequence)
