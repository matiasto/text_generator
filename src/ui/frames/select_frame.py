from tkinter import ttk, constants, Radiobutton, StringVar


class SelectFrame:
    def __init__(self, root: object, current_title, available_data, handle_change_model) -> None:
        self.__root = root
        self.__frame = None
        self.__available_data = available_data
        self.__buttons = []
        self.__button_val = StringVar(value=current_title)
        self.__handle_change_model = handle_change_model
        self.__options = {'padx': 5, 'pady': 5}
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __change_model(self, event=None) -> None:
        new_value = self.__button_val.get()
        self.__handle_change_model(new_value)
        self.__button_val.set(new_value)

    def __generate_buttons(self):
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
