from tkinter import constants, messagebox
from services import ReadService, CleanService, MarkovModel, GenerateService
from ..frames import InputFrame, SelectFrame, ValueFrame, TextFrame

# Todo caching


class MainView:
    """The applications main view.

    Combines multiple frames into one view.
    Handles new requests to WeatherService.
    Updates frames with new data.

    Managed by the UI.

    Attributes:
        root: The root window.
        frame: The Frame instance.
        weather: Instance of WeatherService.
        frames: Collection of all frames in key: Frame format.
        data: The Weather entity that holds the weather data.
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

    def pack(self) -> None:
        """Pack widgets."""

        self._frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self._frame.destroy()

    def __handle_generate_text(self) -> None:
        self.__generate_text()

    def __handle_change_model(self, title: str):
        self.__change_model(title)

    def __handle_change_degree(self, degree: int) -> None:
        self.__degree = degree
        self.__change_model(self.__read_service.title)

    def __handle_change_limit(self, limit: int) -> None:
        self.__limit = limit

    def __show_input_frame(self) -> None:
        if "input" in self.__frames:
            frame = self.__frames["input"]
            frame.destroy()
        self.__frames["input"] = InputFrame(
            self.__root, self.__handle_generate_text)
        self.__frames["input"].pack()

    def __show_select_frame(self) -> None:
        if "select" in self.__frames:
            frame = self.__frames["select"]
            frame.destroy()
        self.__frames["select"] = SelectFrame(
            self.__root, self.__read_service.title, self.__available_stories, self.__handle_change_model)
        self.__frames["select"].pack()

    def __show_value_frame(self) -> None:
        if "value" in self.__frames:
            frame = self.__frames["value"]
            frame.destroy()
        self.__frames["value"] = ValueFrame(
            self.__root, self.__degree, self.__limit, self.__handle_change_degree, self.__handle_change_limit)
        self.__frames["value"].pack()

    def __show_text_frame(self) -> None:
        if "text" in self.__frames:
            frame = self.__frames["text"]
            frame.destroy()
        self.__frames["text"] = TextFrame(
            self.__root, self.__data)
        self.__frames["text"].pack()

    def __show_error_message(self) -> None:
        """Error message for failed request."""

        messagebox.showerror("Error", "Request Failed")

    def __generate_text(self) -> None:
        starting_word = self.__markov_model.get_random_starting_sequence()
        generate = GenerateService(
            starting_word, self.__markov_model.model, self.__degree, self.__limit)
        self.__data = generate.generated_text
        if not self.__data:
            self.__show_error_message()
        else:
            self.__update_frames()

    def __change_model(self, title: str) -> None:
        self.__read_service.text = title
        clean_service = CleanService(self.__read_service.text)
        self.__markov_model = MarkovModel(
            clean_service.clean_text, self.__degree)
        self.__update_frames()

    def __update_frames(self) -> None:
        """Sets of frame updates."""

        self.__show_input_frame()
        self.__show_select_frame()
        self.__show_value_frame()
        self.__show_text_frame()

    def __initialize(self) -> None:
        self.__available_stories = self.__read_service.available_stories
        story = self.__available_stories[0]
        self.__read_service.text = story
        clean_service = CleanService(self.__read_service.text)
        self.__markov_model = MarkovModel(clean_service.clean_text, 3)
        starting_word = self.__markov_model.get_random_starting_sequence()
        generate = GenerateService(
            starting_word, self.__markov_model.model, 3, 100)
        self.__data = generate.generated_text
        self.__frames["input"] = InputFrame(
            self.__root, self.__handle_generate_text)
        self.__frames["select"] = SelectFrame(
            self.__root, self.__read_service.title, self.__available_stories, self.__handle_change_model)
        self.__frames["value"] = ValueFrame(
            self.__root, self.__degree, self.__limit, self.__handle_change_degree, self.__handle_change_limit)
        self.__frames["text"] = TextFrame(self.__root, self.__data)

        self.__frames["input"].pack()
        self.__frames["select"].pack()
        self.__frames["value"].pack()
        self.__frames["text"].pack()
