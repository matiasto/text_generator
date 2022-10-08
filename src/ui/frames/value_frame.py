from tkinter import StringVar, ttk, constants, messagebox


class ValueFrame:
    """Frame for the selecting the the degree of the model
    and the limit of the generated text.
    
    Attributes:
        root (object): The root window
        frame (object): The frame
        change_degree (func): The function to change the degree
        change_limit (func): The function to change the limit
        degree (int): The degree of the model
        limit (int): The limit of the generated text
        tmp_degree (object): The temporary degree to hold the entry value
        tmp_limit (object): The temporary limit to hold the entry value
        options (dict): The options for the frame
        initialize (func): Initializes the frame
        """

    def __init__(self, root: object, degree: int, limit: int, handle_change_degree, handle_change_limit) -> None:
        """Initializes the frame.

        Args:
            root (object): The root window
            degree (int): The degree of the model
            limit (int): The limit of the generated text
            handle_change_degree (func): The function to change the degree
            handle_change_limit (func): The function to change the limit
        """

        self.__root = root
        self.__frame = None
        self.__change_degree = handle_change_degree
        self.__change_limit = handle_change_limit
        self.__degree = degree
        self.__limit = limit
        self.__tmp_degree = StringVar(value=degree)
        self.__tmp_limit = StringVar(value=limit)
        self.__options = {'padx': 5, 'pady': 5}
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __event_change_degree(self, event=None) -> None:
        """Handles the change degree event.

        Args:
            event (_type_, optional): Defaults to None.
        """

        current = self.__tmp_degree.get()
        if not current or not current.isdigit() or int(current) < 1 or int(current) > 20:
            messagebox.showerror(
                "Error", "degree must be a number between 1 and 20")
            self.__tmp_degree.set(str(self.__degree))
        else:
            self.__degree = int(current)
            self.__change_degree(int(current))

    def __event_change_limit(self, event=None) -> None:
        """Handles the change limit event.

        Entered value must be a number between 1 and 100.

        Args:
            event (optional): Defaults to None.
        """

        current = self.__tmp_limit.get()
        if not current or not current.isdigit() or int(current) < 1 or int(current) > 100:
            messagebox.showerror(
                "Error", "limit must be a number between 1 and 100")
            self.__tmp_limit.set(str(self.__limit))
        else:
            self.__limit = int(current)
            self.__change_limit(int(current))

    def __fields(self) -> None:
        """Creates the fields."""
        
        entry_degree = ttk.Entry(self.__frame, textvariable=self.__tmp_degree)
        entry_limit = ttk.Entry(self.__frame, textvariable=self.__tmp_limit)
        button_degree = ttk.Button(
            self.__frame, text="Change Degree", command=lambda: self.__event_change_degree())
        button_limit = ttk.Button(
            self.__frame, text="Change Limit", command=lambda: self.__event_change_limit())

        entry_degree.grid(
            row=0, column=0, sticky=constants.W, **self.__options)
        entry_limit.grid(row=1, column=0, sticky=constants.W, **self.__options)
        button_degree.grid(
            row=0, column=1, sticky=constants.W, **self.__options)
        button_limit.grid(
            row=1, column=1, sticky=constants.W, **self.__options)

    def __initialize(self) -> None:
        """Initializes the frame."""

        self.__frame = ttk.Labelframe(master=self.__root)
        self.__fields()
