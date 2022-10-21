from threading import Thread
from tkinter import messagebox
from services import ReadService, CleanService, MarkovModel, GenerateService
from ..frames import InputFrame, SelectFrame, ValueFrame, TextFrame, LoadingFrame


class MainView:
    """The view to control the application.

    Handles the user input and updates the view.

    On events that change the model, the view will show a loading screen
    while a new model is created on a separate thread. The view will
    monitor the thread and update the frames when the thread is finished.
    Updated values will be passed on to the new frames.

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
        self.__current_sequence = ""
        self.__frames = {}
        self.__data = ""
        self.__degree = 3
        self.__limit = 100
        self.__initialize()

    def __handle_retrieve_children(self, sequence=None) -> None:
        """Pass on function for the retrieve_children method.

        Args:
            sequence (list): The sequence of the generated text.
        """

        return self.__retrieve_children(sequence)

    def __handle_generate_text(self, original="", sequence=None) -> None:
        """Pass on function for the generate_text method."""

        self.__current_sequence = original
        self.__generate_text(sequence)

    def __handle_change_model(self, title: str) -> None:
        """Pass on function for the select frames title selection.

        Initializes a new model with the new title.

        Args:
            title (str): The title of the selected story.
        """

        self.__change_model(title)

    def __handle_change_degree(self, degree: int) -> None:
        """Pass on function for the value frames degree field.

        Initializes a new model with the new degree.

        Args:
            degree (int): New degree of the markov model.
        """

        self.__degree = degree
        self.__change_model(self.__read_service.title)

    def __handle_change_limit(self, limit: int) -> None:
        """Pass on function for the value frames limit field.

        Sets the limit of the generated text.
        Only affects the following text generations.

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
            self.__root, self.__current_sequence, self.__handle_retrieve_children, self.__handle_generate_text)
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
        """Shows the loading screen 

        Appears while the model is being created in a parallel thread.
        After the thread is finished, the loading screen will be destroyed
        and the new frames will be shown.
        """

        for frame in self.__frames.values():
            frame.destroy()
        self.__frames["loading"] = LoadingFrame(self.__root)
        self.__frames["loading"].pack()

    def __show_error_message(self, message: str) -> None:
        """Shows an error message.

        Args:
            message (str): The error message.
        """

        self.__root.withdraw()
        messagebox.showerror("Error", message)
        self.__root.deiconify()

    # method for monitoring the active threads
    def __monitor_thread(self, active_thread) -> None:
        """Monitors the active thread.

        Checks if the thread is still active every 100ms.
        If the thread is finished, the loading screen will be destroyed
        and the new frames will be shown.

        Addtionally, the current start state will be emptied.

        Args:
            active_thread (Thread): The active thread.
        """

        if active_thread.is_alive():
            self.__root.after(
                100, lambda: self.__monitor_thread(active_thread))
        else:
            self.__current_sequence = ""
            self.__update_frames()

    def __loading_screen(func):
        """Decorator to show the loading screen while creating the model.

        The decorator handles the creation of the model in a separate thread.
        The loading screen will be shown while the thread is active.
        After the thread is finished, the loading screen will be destroyed
        and the new frames will be shown.
        """

        def wrapper(self, *args, **kwargs):
            self.__show_loading_screen()
            thread = Thread(target=func, args=(self, *args), kwargs=kwargs)
            thread.start()
            self.__monitor_thread(thread)
        return wrapper

    def __retrieve_children(self, sequence) -> list:
        """Retrieves the children of the sequence.

        Used for the autocomplete feature in the input frame.

        Args:
            sequence (list): The sequence of the generated text.

        Returns:
            list: The updated autocomplete list.
        """

        if not sequence:
            return list(self.__markov_model.model.get_children(sequence).keys())

        children = None
        if len(sequence) > self.__degree:
            children = self.__markov_model.model.get_children(
                sequence[-self.__degree:])
        else:
            children = self.__markov_model.model.get_children(sequence)

        if children:
            sequence_str = " ".join(sequence)
            return [sequence_str + " " + i for i in list(children.keys())]
        return []

    @__loading_screen
    def __generate_text(self, sequence) -> None:
        """Generates the text.

        Given a starting sequence, the method will first complete the sequence
        to meet the degree of the model. Then, the existing model will be used
        to generate the text.

        Args:
            sequence (list): The possible starting sequence from the user input; a list of strings.
        """        

        if sequence is None:
            sequence = []
        sequence = self.__markov_model.form_the_starting_sequence(sequence)
        if not sequence:
            self.__show_error_message(
                "Could not generate sequence.\nGenerating a random sequence.")
            sequence = self.__markov_model.form_the_starting_sequence([])
        generate = GenerateService(
            sequence, self.__markov_model.model, self.__degree, self.__limit)
        self.__data = generate.generated_text
        if not self.__data:
            self.__show_error_message("Could not generate text.")

    @__loading_screen
    def __change_model(self, title: str) -> None:
        """Retrains the model with a new story.

        Given a title, the method will retrieve the story from the file.
        Then, after cleaning the text, the model will be retrained with the new story.

        Args:
            title (str): The title of the new story.
        """

        self.__read_service.text = title
        clean_service = CleanService(self.__read_service.text)
        self.__markov_model = MarkovModel(
            clean_service.clean_text, self.__degree)

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
        self.__read_service.text = self.__available_stories[0]
        clean_service = CleanService(self.__read_service.text)
        self.__markov_model = MarkovModel(clean_service.clean_text, 3)
        self.__update_frames()
