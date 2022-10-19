import re


class CleanService:
    """Cleans the text and returns a list of  tokenized words

    Firstly removes copyright information and other non-textual information
    from the text. Then converts all characters to lowercase and removes
    punctuation and other disallowed characters. Finally, tokenizes the text
    into a list of words.

    Attributes:
        text (str): The text to be cleaned
    """

    def __init__(self, text: str) -> None:
        """Inits CleanService with the text to be cleaned

        Args:
            text (str): The text to be cleaned
        """

        self.__text = text
        self.__clean_text = None
        self.__intialize()

    @property
    def clean_text(self) -> list:
        """Returns the cleaned text as tokenized words"""

        return self.__clean_text

    def __remove_meta_info(self) -> None:
        """Removes meta information from the text"""

        text = None
        is_book_text = False
        for line in self.__text:
            if re.match(r"\*\*\* END OF THE PROJECT GUTENBERG EBOOK .+ \*\*\*", line):
                is_book_text = False
                continue
            if re.match(r"\*\*\* START OF THE PROJECT GUTENBERG EBOOK .+ \*\*\*", line):
                is_book_text = True
                continue
            if is_book_text:
                if text is None:
                    text = line
                else:
                    text += line
        self.__text = text

    def __clean(self) -> None:
        """Cleans the text"""

        self.__text = re.sub(r"[^A-Za-z\.\!\?\'\,]", " ", self.__text)
        self.__text = self.__text.lower()
        self.__text = ' '.join(self.__text.split())

    def __tokenize(self) -> None:
        """Tokenizes the text into a list of words"""

        self.__clean_text = self.__text.split()

    def __intialize(self) -> None:
        """Initializes the CleanService"""

        self.__remove_meta_info()
        self.__clean()
        self.__tokenize()
