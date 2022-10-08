from tkinter import ttk, constants, Radiobutton, StringVar


class SelectFrame:
    """Frame for the selecting the underlying model.

    Attributes:
        root (object): The root window
        frame (object): The frame
        available_data (dict): The available data
        buttons (list): The buttons
        button_val (object): The value of the selected button
        handle_change_model (func): The function to handle the change model event
        intialize (func): Initializes the frame
    """

    def __init__(self, root: object, current_title: str, available_data: dict, handle_change_model) -> None:
        """Initializes the frame.

        Args:
            root (object): _description_
            current_title (str): the active title
            available_data (dict)): available titles
            handle_change_model (func): The function to handle the change model event
        """

        self.__root = root
        self.__frame = None
        self.__available_data = available_data
        self.__buttons = []
        self.__button_val = StringVar(value=current_title)
        self.__handle_change_model = handle_change_model
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __change_model(self, event=None) -> None:
        """Handles the change model event."""

        new_value = self.__button_val.get()
        self.__handle_change_model(new_value)
        self.__button_val.set(new_value)

    def __generate_buttons(self) -> None:
        """Creates the radiobuttons for each model.
        
        binds 'change_model' to each button.
        """

        label_frame = ttk.Labelframe(self.__frame)
        index = 0
        for value in self.__available_data.values():
            self.__buttons.append(Radiobutton(
                label_frame, text=value, variable=self.__button_val, value=value, command=self.__change_model))
            self.__buttons[-1].grid(sticky='WENS',
                                    row=index, column=0, padx=1, pady=1)
            index += 1
        label_frame.grid(row=1, column=0, columnspan=5, sticky=(constants.W))

    def __initialize(self) -> None:
        """Initializes the frame."""

        self.__frame = ttk.Frame(master=self.__root)
        self.__generate_buttons()
