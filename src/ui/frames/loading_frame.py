from tkinter import ttk, constants


class LoadingFrame:
    """Frame for the loading screen.

    Attributes:
        root (object): The root window
        frame (object): The frame
        configure (func): Configures the frame
        run (func): Runs the frame
    """

    def __init__(self, root) -> None:
        """Initializes the frame.

        Args:
            root (object): The root window
        """

        self.root = root
        self.__frame = ttk.Frame(self.root)
        self.__configure()
        self.__run()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __configure(self) -> None:
        """Configures the frame."""

        self.__frame.columnconfigure(0, weight=1)
        self.__frame.rowconfigure(0, weight=1)

    def __run(self) -> None:
        """Creates the progressbar."""

        pl = ttk.Label(
            self.__frame, text="Loading...", font=("Helvetica", 16))
        pb = ttk.Progressbar(
            self.__frame, orient=constants.HORIZONTAL, mode='indeterminate', length=400)
        pl.grid(row=0, column=0, columnspan=7, sticky=constants.NSEW)
        pb.grid(row=1, column=0, columnspan=7,
                sticky=constants.EW, padx=10, pady=10)
        pb.start(10)
