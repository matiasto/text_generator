from re import S
from tkinter import IntVar, ttk, constants, messagebox


class ValueFrame:
    def __init__(self, root: object, degree: int, limit: int, handle_change_degree, handle_change_limit) -> None:
        self.__root = root
        self.__frame = None
        self.__change_degree = handle_change_degree
        self.__change_limit = handle_change_limit
        self.__degree = IntVar(value=degree)
        self.__limit = IntVar(value=limit)
        self.__options = {'padx': 5, 'pady': 5}
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __event_change_degree(self, event=None) -> None:
        new_degree = self.__degree.get()
        if new_degree < 1 or new_degree > 10:
            messagebox.showerror("Error", "degree must be between 1 and 10")
        else:
            self.__degree = new_degree
            self.__change_degree(new_degree)

    def __event_change_limit(self, event=None) -> None:
        new_limit = self.__limit.get()
        if new_limit < 1 or new_limit > 100:
            messagebox.showerror("Error", "limit must be between 1 and 100")
        else:
            self.__limit = new_limit
            self.__change_limit(new_limit)

    def __fields(self) -> None:
        entry_degree = ttk.Entry(self.__frame, textvariable=self.__degree)
        entry_limit = ttk.Entry(self.__frame, textvariable=self.__limit, )
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
