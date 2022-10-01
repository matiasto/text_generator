from tkinter import Tk
from ui import UI


def main():
    """Start app.

    Intializes the Tk instance, starts the UI, and
    handles the mainloop.
    """

    window = Tk()
    window.title('WeatherApp')

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    main()
