from threading import Thread
from services import ReadService, CleanService, MarkovModel, GenerateService
from ..frames import InputFrame, SelectFrame, ValueFrame, TextFrame, LoadingFrame

# Todo caching


class MainView:
    """The view to control the application.

    Handles the user input and updates the view.

    Attributes:
        root (object): The root window, Tk() instance.
        markov_model (MarkovModel): The markov model instance.
        read_service (ReadService): The read service instance.
        available_stories (dict): The list of available stories.
        frames (dict): The dictionary of frames.
        data (str): The generated text.
        degree (int): The degree of the markov model.
        limit (int): The limit of the generated text.
        initialize (method): The method to initialize the view.
    """

    def __init__(self, root: object) -> None:
        """Class constructor.

        Args:
            root (object): The root window, Tk() instance.
        """

        self.__root = root
        self.__markov_model = None
        self.__read_service = ReadService()
        self.__available_stories = None
        self.__frames = {}
        self.__data = ""
        self.__degree = 3
        self.__limit = 100
        self.__initialize()

    def __handle_generate_text(self) -> None:
        """Pass on function for the generate button."""

        self.__generate_text()

    def __handle_change_model(self, title: str) -> None:
        """Pass on function for the select frame.

        Args:
            title (str): The title of the selected story.
        """

        self.__change_model(title)

    def __handle_change_degree(self, degree: int) -> None:
        """Pass on function for the value frame.

        Args:
            degree (int): New degree of the markov model.
        """

        self.__degree = degree
        self.__change_model(self.__read_service.title)

    def __handle_change_limit(self, limit: int) -> None:
        """Pass on function for the value frame.

        Args:
            limit (int): New limit of the generated text.
        """

        self.__limit = limit
        self.__update_frames()

    def __show_input_frame(self) -> None:
        """Shows the input frame."""

        if "input" in self.__frames:
            frame = self.__frames["input"]
            frame.destroy()
        self.__frames["input"] = InputFrame(
            self.__root, self.__handle_generate_text)
        self.__frames["input"].pack()

    def __show_select_frame(self) -> None:
        """Shows the select frame."""

        if "select" in self.__frames:
            frame = self.__frames["select"]
            frame.destroy()
        self.__frames["select"] = SelectFrame(
            self.__root, self.__read_service.title, self.__available_stories, self.__handle_change_model)
        self.__frames["select"].pack()

    def __show_value_frame(self) -> None:
        """Shows the value frame."""

        if "value" in self.__frames:
            frame = self.__frames["value"]
            frame.destroy()
        self.__frames["value"] = ValueFrame(
            self.__root, self.__degree, self.__limit, self.__handle_change_degree, self.__handle_change_limit)
        self.__frames["value"].pack()

    def __show_text_frame(self) -> None:
        """Shows the text frame."""

        if "text" in self.__frames:
            frame = self.__frames["text"]
            frame.destroy()
        self.__frames["text"] = TextFrame(
            self.__root, self.__data)
        self.__frames["text"].pack()

    def __show_loading_screen(self) -> None:
        """Shows the loading screen while creating the model."""

        for frame in self.__frames.values():
            frame.destroy()
        self.__frames["loading"] = LoadingFrame(self.__root)
        self.__frames["loading"].pack()

    def __monitor(self, running_thread) -> None:
        """Monitors the running thread."""

        if running_thread.is_alive():
            self.__root.after(100, lambda: self.__monitor(running_thread))

    def __loading_screen(func):
        """Decorator to show the loading screen while creating the model."""

        def wrapper(self, *args, **kwargs):
            self.__show_loading_screen()
            thread = Thread(target=func, args=(self, *args), kwargs=kwargs)
            thread.start()
            self.__monitor(thread)
        return wrapper

    @__loading_screen
    def __generate_text(self) -> None:
        """Generates the text based on current model and values."""

        starting_word = self.__markov_model.get_random_starting_sequence()
        generate = GenerateService(
            starting_word, self.__markov_model.model, self.__degree, self.__limit)
        self.__data = generate.generated_text
        if not self.__data:
            self.__show_error_message()
        else:
            self.__update_frames()

    @__loading_screen
    def __change_model(self, title: str) -> None:
        """Changes the model based on the selected story.

        Args:
            title (str): The title of the selected story.
        """

        self.__read_service.text = title
        clean_service = CleanService(self.__read_service.text)
        self.__markov_model = MarkovModel(
            clean_service.clean_text, self.__degree)
        self.__update_frames()

    def __update_frames(self) -> None:
        """Updates the frames."""

        if "loading" in self.__frames:
            self.__frames["loading"].destroy()
        self.__show_input_frame()
        self.__show_select_frame()
        self.__show_value_frame()
        self.__show_text_frame()

    def __initialize(self) -> None:
        """Initializes the view."""
        
        self.__available_stories = self.__read_service.available_stories
        story = self.__available_stories[0]
        self.__read_service.text = story
        clean_service = CleanService(self.__read_service.text)
        self.__markov_model = MarkovModel(clean_service.clean_text, 3)
        self.__update_frames()
