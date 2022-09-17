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

    def __clean(self) -> None:
        """Cleans the text and tokenizes it into a list of words

        Loops trough the text and ignores copyright information and other
        non-textual information from the text. Then converts all characters
        to lowercase and removes punctuation and other disallowed characters.
        Finally, tokenizes the text into a list of words.
        """

        cleaned_txt = []
        book_text = False
        for line in self.__text:
            if re.match(r"\*\*\* END OF THE PROJECT GUTENBERG EBOOK .+ \*\*\*", line):
                book_text = False
                continue
            if re.match(r"\*\*\* START OF THE PROJECT GUTENBERG EBOOK .+ \*\*\*", line):
                book_text = True
                continue
            if book_text:
                line = line.lower()
                disallowed_characters = ",.\"\'_@#$%^&*(){}/;~:<>+=\\"
                line = line.translate(
                    {ord(c): None for c in disallowed_characters})
                tokens = line.split()
                cleaned_txt += tokens
        self.__clean_text = cleaned_txt

    def __intialize(self) -> None:
        """Initializes the CleanService"""

        self.__clean()
