from .views import MainView


class UI:
    """The main UI.

    Manages the MainView.

    Attributes:
        root: The root window.
        current_view: Active view.
        set_up_geometry: Sets up window geometry.
    """

    def __init__(self, root: object) -> None:
        """Class constructor.

        Args:
            root (object): The root window, Tk() instance.
        """

        self.__root = root
        self.__current_view = None
        self.__set_up_geometry()

    def __set_up_geometry(self) -> None:
        """Sets up window geometry."""

        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        center_x = int(screen_width/2)
        center_y = int(screen_height/2)
        self.__root.geometry("+%d+%d" % (center_x, center_y))

    def __hide_current_view(self) -> None:
        """Destroys the current view."""

        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def __handle_main_view(self) -> None:
        """Handles redirect to MainView."""

        self.__show_main_view()

    def __show_main_view(self) -> None:
        """Activates MainView."""

        self.__hide_current_view()
        self.__current_view = MainView(self.__root)

    def start(self) -> None:
        """Start the UI."""

        self.__handle_main_view()
