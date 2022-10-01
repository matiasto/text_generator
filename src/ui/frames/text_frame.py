from tkinter import ttk, constants, Text


class TextFrame:
    def __init__(self, root: object, data) -> None:
        """Class constructor.

        Args:
            frame (object): Frame instance from ForecastFrame.
        """

        self.__root = root
        self.__frame = None
        self.__data = data
        self.__options = {'padx': 5, 'pady': 5}
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Clears the current details frame."""

        self.__frame.destroy()

    def __set_text(self) -> None:
        """Generates the general widgets.

        These widgets display general information about the day.
        """

        text = Text(self.__frame, height=10, width=100)
        text.pack(expand=True)
        text.insert('insert', self.__data)
        text.config(state='disabled')

    def update(self, text: object) -> None:
        self.__data = text
        self.__frame = ttk.Labelframe(self.__root, text="Generated text")
        self.__set_text()
        self.__frame.grid(row=4, column=0, rowspan=4,
                          columnspan=15, sticky=constants.W, **self.__options)

    def __initialize(self) -> None:
        """Initializes the frame."""

        self.__frame = ttk.Labelframe(self.__root, text="Generated text")
        self.__set_text()
