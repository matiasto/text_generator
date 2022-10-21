from tkinter import ttk, constants, StringVar, messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox


class InputFrame:
    """Frame for the input field and generate button.

    When generating text, the sequence is retrieved from the entry field
    and passed to the handle_generate_text function. if the entry field is empty,
    the handle_generate_text function is called with an empty sequence and
    a random sequence is generated. Otherwise, the sequence is split on spaces
    to create the sequence and passed on to the handle_generate_text function.

    The input field uses the AutocompleteCombobox from the ttkwidgets package and 
    the autocomplete values are updated every time the user types a space. The
    autocomplete values are retrieved from the handle_retrieve_children function which
    in turn calls the retrieve_children function from the MarkovChain class. The
    children retrieved from the MarkovChain class are all the possible words that 
    follow the current sequence.

    Attributes:
        root (object): The root window
        frame (object): The frame
        current_sequence (StringVar): The current sequence
        complete_values (list): The values for the autocomplete
        entry (object): The entry field
        handle_retrieve_children (method): The function to retrieve the children for the autocomplete
        handle_generate_text (func): The function to handle the generate button
        options (dict): The options for the widgets
        initialize (func): Initializes the frame
    """

    def __init__(self, root: object, current_sequence, handle_retrieve_children, handle_generate_text) -> None:
        """Initializes the frame.

        Args:
            root (object): The root window
            current_sequence (StringVar): The current sequence for the entry field
            handle_retrieve_children (method): The function to retrieve the children for the autocomplete
            handle_generate_text (method): The function to handle the generate button
        """

        self.__root = root
        self.__frame = None
        self.__current_sequence = StringVar(value=current_sequence)
        self.__complete_values = []
        self.__entry = None
        self.__handle_retrieve_children = handle_retrieve_children
        self.__handle_generate_text = handle_generate_text
        self.__options = {'padx': 5, 'pady': 5}
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __callback(self, *args) -> None:
        """Callback function for the entry field.

        Updates the autocomplete values every time the user types a space.

        Args:
            *args: The arguments
        """

        content = self.__current_sequence.get()
        if not content:
            self.__complete_values = self.__handle_retrieve_children()
        elif content.endswith(" "):
            sequence = list(filter(None, content.split()))
            self.__complete_values = self.__handle_retrieve_children(sequence)
            self.__entry.configure(completevalues=self.__complete_values)

    def __handle_generate_event(self, event=None) -> None:
        """Handles the generate event.

        Retrieves the sequence from the entry field and calls the handle_generate_text function.

        Args:
            event (_, optional): Defaults to None.
        """
        sequence = None
        original = self.__current_sequence.get()
        if len(original) > 100:
            messagebox.showerror(
                "Error", "The sequence can't be longer than 100 characters.")
            self.__current_sequence.set("")
            return
        if original and len(original) < 100:
            sequence = list(filter(None, original.split()))
        self.__entry.destroy()
        self.__handle_generate_text(original, sequence)

    def __header(self) -> None:
        """Creates the header."""

        header = ttk.Label(
            self.__frame, text=f"Markov chain text generator", font=("Arial", 30))
        header.grid(row=0, column=7, columnspan=5,
                    sticky=(constants.S), padx=50)

    def __entry_field(self) -> None:
        """Creates the entry field.
        
        The entry field uses the AutocompleteCombobox from the ttkwidgets package.
        Every time the user types a space, the autocomplete values are updated.
        """

        label_frame = ttk.Labelframe(self.__frame)

        self.__entry = AutocompleteCombobox(
            label_frame, width=50, textvariable=self.__current_sequence, completevalues=self.__complete_values
        )
        self.__entry.grid(
            column=0, row=0, sticky=constants.W, **self.__options)

        label_frame.grid(row=0, column=0, columnspan=5, sticky=(constants.W))

    def __generate_button(self) -> None:
        """Creates the generate button.
        
        The button calls the handle_generate_event method.
        """

        label_frame = ttk.Labelframe(self.__frame)

        self.__root.bind("<Return>", self.__handle_generate_event)
        generate_button = ttk.Button(
            label_frame, text="Generate text", command=self.__handle_generate_event)

        generate_button.grid(
            column=0, row=0, sticky=constants.W, **self.__options)
        label_frame.grid(row=1, column=0, columnspan=5, sticky=(constants.W))

    def __initialize(self) -> None:
        """Initializes the frame."""

        self.__frame = ttk.Frame(master=self.__root)
        self.__header()
        self.__current_sequence.trace("w", self.__callback)
        self.__complete_values = self.__handle_retrieve_children()
        self.__entry_field()
        self.__generate_button()
