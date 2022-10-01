from tkinter import ttk, constants, Radiobutton


class InputFrame:
    def __init__(self, root: object, handle_generate_text) -> None:
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
        self.__handle_generate_text()

    def __header(self) -> None:
        header = ttk.Label(
            self.__frame, text=f"Markov chain text generator", font=("Arial", 30))
        header.grid(row=0, column=7, columnspan=5,
                    sticky=(constants.S), padx=50)

    def __generate_button(self) -> None:
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
