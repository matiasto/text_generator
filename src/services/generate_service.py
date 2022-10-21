from random import choices


class GenerateService:
    """Generates text based on the model

    Given a start state and a model, generates text based on the model.

    Attributes:
        sequence (list): The sequence to be used as the start state
        limit (int): The number of words to be generated
        model (object): The model to be used for generating text
        degree (int): The degree of the model
        generated_text (str): The generated text
        generate (function): The function that generates the text
    """

    def __init__(self, sequence: list, model: object, degree: int, limit=10) -> None:
        """Inits GenerateService with the start state, model and limit

        Args:
            sequence (list): The sequence to be used as the start state
            model (object): The model to be used for generating text
            degree (int): The degree of the model
            limit (int, optional): The limit of how many keys are
                                    picked from the model. Defaults to 10.
        """

        self.__sequence = sequence
        self.__limit = limit
        self.__model = model
        self.__degree = degree
        self.__generated_text = ""
        self.__generate()

    @property
    def generated_text(self) -> str:
        """Returns the generated text as string"""

        return self.__generated_text

    def __calculate_probability(self, children: dict) -> dict:
        """Calculates the probability of each children node.

        Args:
            children (dict): The children of the current state

        Returns:
            dict: The probability of each word
        """

        total = sum([i.frequency for i in children.values()])
        return {word: value.frequency / total for word, value in children.items()}

    def __generate(self) -> None:
        """Generates text based on the model, degree and limit"""

        sequence = self.__sequence
        while len(sequence) < self.__limit:
            children = self.__model.get_children(sequence[-self.__degree:])
            probability = self.__calculate_probability(children)
            word = choices(list(probability.keys()),
                           list(probability.values()))[0]
            sequence.append(word)
        self.__generated_text = " ".join(sequence)
