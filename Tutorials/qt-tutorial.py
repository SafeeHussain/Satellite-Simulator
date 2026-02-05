# This section will just go over how I can use Qt as a way to make a quick GUI application

# Only needed to access command line arguments (whatever that means)
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt

# QApplication gets the application started
# QPushButton creates a button instance
# QWidget creates a widget for the user
# QMainWindow creates a main window

# Subclass QMainWindow to customise application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Sets the title of the window
        self.setWindowTitle("My App")

        # Creates a button instance
        button = QPushButton("Press me")

        # Set the central widget of the window
        #   In this case, putting the button in the centre of the screen
        #   By default, it is set to take up the whole screen
        self.setCentralWidget(button)

        # Setting a fixed sized to prevent resizing a window
        self.setFixedSize(QSize(400, 300))
        # Additionally, you can also do .setMinimumSize() and .setMaximumSize()
        self.setMaximumSize(QSize(800, 700))
        self.setMinimumSize(QSize(100, 200))



# Only need 1 QApplication instance per application
# Passing in sys.argv allows to use command line arguments for you app
app = QApplication(sys.argv)

# Creating a Qt Widget
window = MainWindow()
window.show()   # Windows are hidden by default

# Starting event loop
app.exec()

# The code will not continue until you exit the app
print("Hello World")
