"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui


class Controls(QtGui.QWidget):
    """Customer video player used by the PyTouchAnalysis program"""

    def __init__(self, main, player):
        """Function to initialise the class"""
        super(Controls, self).__init__()

        # Set reference to main window and player
        self.main = main
        self.player = player

        # Create the UI
        self.init_ui()

    def init_ui(self):
        """Function which creates the UI"""

        # Create and set the grid as layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        # Create the buttons
        play = QtGui.QPushButton('play')
        pause = QtGui.QPushButton('pause')