from tkinter import ttk, constants, Text


class TextFrame:
    """Frame for the generated text.

    Attributes:
        root (object): The root window
        frame (object): The frame
        data (str): The generated text
        options (dict): The options for the frame
        initialize (func): Initializes the frame
    """

    def __init__(self, root: object, data) -> None:
        """Class constructor.

        Args:
            root (object): The root window
            data (str): The generated text
        """

        self.__root = root
        self.__frame = None
        self.__data = data
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __set_text(self) -> None:
        """Sets the text to disabled text widget."""

        text = Text(self.__frame, height=10, width=100)
        text.pack(expand=True)
        text.insert('insert', self.__data)
        text.config(state='disabled')

    def __initialize(self) -> None:
        """Initializes the frame."""

        self.__frame = ttk.Labelframe(self.__root, text="Generated text")
        self.__set_text()
