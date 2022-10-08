from tkinter import ttk, constants


class InputFrame:
    """Frame for the generate button.

    Attributes:
        root (object): The root window
        frame (object): The frame
        handle_generate_text (func): The function to handle the generate button
        options (dict): The options for the widgets
        initialize (func): Initializes the frame
    """

    def __init__(self, root: object, handle_generate_text) -> None:
        """Initializes the frame.

        Args:
            root (object): The root window
            handle_generate_text (method): The function to handle the generate button
        """

        self.__root = root
        self.__frame = None
        self.__handle_generate_text = handle_generate_text
        self.__options = {'padx': 5, 'pady': 5}
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __handle_generate_event(self, event=None) -> None:
        """Handles the generate button event.

        Args:
            event (_, optional): Defaults to None.
        """

        self.__handle_generate_text()

    def __header(self) -> None:
        """Creates the header."""

        header = ttk.Label(
            self.__frame, text=f"Markov chain text generator", font=("Arial", 30))
        header.grid(row=0, column=7, columnspan=5,
                    sticky=(constants.S), padx=50)

    def __generate_button(self) -> None:
        """Creates the generate button."""

        label_frame = ttk.Labelframe(self.__frame)

        self.__root.bind("<Return>", self.__handle_generate_event)
        generate_button = ttk.Button(
            label_frame, text="Generate text", command=self.__handle_generate_event)

        generate_button.grid(
            column=1, row=0, sticky=constants.W, **self.__options)
        label_frame.grid(row=0, column=0, columnspan=5, sticky=(constants.W))

    def __initialize(self) -> None:
        """Initializes the frame."""

        self.__frame = ttk.Frame(master=self.__root)
        self.__header()
        self.__generate_button()
