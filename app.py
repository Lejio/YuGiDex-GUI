from PySide6.QtWidgets import QApplication
import sys
from window import App

if __name__ == "__main__":
    
    # Set event loop.
    app = QApplication(sys.argv)
    
    # Obtain sizes of user's desktop screen. Used to change the default window size.
    screens = app.screens()[0].size().toTuple()
    print(f"Creating App for display size of W:{screens[0]}, H:{screens[1]}.")
    
    app_width = int(round(screens[0] / 5) * 3)
    app_height = int(round(screens[1] / 7) * 5)
    
    app_x = int(round(screens[0] / 5))
    app_y = int(round(screens[1] / 7))
    
    # Starts the App.
    w = App(app_x, app_y, app_width, app_height)
    w.show()
    
    # Executes event loop.
    app.exec()

