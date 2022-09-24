from services import ReadService, CleanService, MarkovModel, GenerateService


class UI:
    """The user interface of the program

    Attributes:
        read_service (ReadService): The service that manages reading files
        available_stories (list): The names of the stories
        text (list): generated text
        run (function): The function that runs the program
    """

    def __init__(self) -> None:
        """Initializes the UI"""

        self.__read_service = ReadService()
        self.__available_stories = self.__read_service.available_stories
        self.__text = None
        self.__run()

    def __welcome(self) -> None:
        """Prints the welcome message"""

        print("Welcome to the Markov Chain Text Generator!")

    def __create(self, choice, order, word_count) -> None:
        """Creates the Markov chain and generates text

        Args:
            choice (str): The name of the story
            order (int): The order of the Markov chain
            word_count (int): The number of words to generate
        """

        story = self.__available_stories[choice - 1]
        self.__read_service.text = story
        clean_service = CleanService(self.__read_service.text)
        markov_model = MarkovModel(clean_service.clean_text, order)
        starting_word = markov_model.get_random_starting_sequence()
        generate = GenerateService(
            starting_word, markov_model.model, order, word_count)
        self.__text = generate.generated_text

    def __run(self) -> None:
        """Runs the program"""

        self.__welcome()
        while True:
            print("Available stories:")
            for i, story in enumerate(self.__available_stories):
                print(f"{i + 1}. {story}")
            print("0. Exit\n")
            choice = input("Choose a story: ")
            if choice == "0":
                break
            try:
                choice = int(choice)
                if choice < 0 or choice > len(self.__available_stories):
                    raise ValueError
            except ValueError:
                print("Invalid choice")
                continue
            order = input("Enter the degree of the Markov chain: ")
            if order.isnumeric():
                order = int(order)
            else:
                print("Invalid order, order set to 2")
                order = 2
            word_count = input(
                "Enter the number of words to generate (0 - 100): ")
            if word_count.isnumeric() and int(word_count) > 0 and int(word_count) < 100:
                word_count = int(word_count)
            else:
                print("Invalid word count, word count set to 10")
                word_count = 10
            self.__create(choice, order, word_count)
            print("\nGenerated text:")
            print(self.__text)
            print("\n")
