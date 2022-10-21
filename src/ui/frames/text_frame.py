from tkinter import ttk, constants, Text


class TextFrame:
    """Frame for the generated text.

    This Frame displays the generated text. Updates when
    the generate button is pressed.

    Attributes:
        root (object): The root window
        frame (object): The frame
        data (str): The generated text
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
        """Sets the generated text to 'disabled' text widget."""

        label_frame = ttk.LabelFrame(self.__frame, text="Generated text")

        text = Text(label_frame, height=10, width=100)
        text.pack(expand=True)
        text.insert('insert', self.__data)
        text.config(state='disabled')

        label_frame.grid(row=4, column=0, columnspan=5, sticky=(constants.W))

    def __initialize(self) -> None:
        """Initializes the frame."""

        self.__frame = ttk.Frame(self.__root)
        self.__set_text()
