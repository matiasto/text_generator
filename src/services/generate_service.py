from random import choices


class GenerateService:
    """Generates text based on the model

    Given a start state and a model, generates text based on the model.

    Attributes:
        start_state (str): The starting state of the model
        limit (int): The number of words to be generated
        model (dict): The model to be used for generating text
        generated_text (str): The generated text
        generate (function): The function that generates the text
    """

    def __init__(self, start_state: str, model: dict, limit=10) -> None:
        """Inits GenerateService with the start state, model and limit

        Args:
            start_state (str): The starting state of the model
            model (dict): The model to be used for generating text
            limit (int, optional): The limit of how many keys are
                                    picked from the model. Defaults to 10.
        """

        self.__start_state = start_state
        self.__limit = limit
        self.__model = model
        self.__generated_text = ""
        self.__generate()

    @property
    def generated_text(self) -> str:
        """Returns the generated text as string"""

        return self.__generated_text

    def __generate(self) -> None:
        """Generates text based on the model

        Given a start state and a model, the method generates text based on
        the model. The method loops through the model and picks a key based
        on the probability of the key (inside the model). The key is then
        added to the generated text and used as the new start state.
        The process is repeated until the limit is reached.
        """

        current_state = self.__start_state
        self.__generated_text += current_state
        for _ in range(self.__limit):
            next_state = choices(list(self.__model[current_state].keys()),
                                 list(self.__model[current_state].values()))[0]
            self.__generated_text += " " + next_state
            current_state = next_state
