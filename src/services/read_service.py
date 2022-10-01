import os


class ReadService:
    """Reads the text from the file and returns it as a list of lines

    Shares the names of the stories and reads the text from the file

    Attributes:
        files (dict): The names of the stories and the files they are in
        text (list): The text from the file
        path (str): The path to the data folder
    """

    def __init__(self) -> None:
        """Initializes the ReadService"""

        self.__files = {
            "Alice in Wonderland": "alice_in_wonderland.txt",
            "Frankenstein": "frankenstein.txt",
            "Moby Dick": "moby_dick.txt",
            "Sherlock Holmes": "sherlock_holmes.txt"
        }
        self.__title = None
        self.__text = None
        self.__path = os.path.join(
            os.path.dirname(__file__), "../data/")

    @property
    def available_stories(self) -> list:
        """Returns the names of the stories"""

        return {index: value for (index, value) in enumerate(self.__files.keys())}

    @property
    def title(self) -> str:
        """Returns the title of the story"""

        return self.__title

    @property
    def text(self) -> list:
        """Returns the text from the file"""

        return self.__text

    @text.setter
    def text(self, story) -> None:
        """Sets the text from the file

        Args:
            story (str): The name of the story
        """

        self.__title = story
        story_file = self.__files[story]
        with open(self.__path + story_file, "r", encoding="utf-8") as file:
            self.__text = file.readlines()
