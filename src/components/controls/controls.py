"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui


class TControls(QtGui.QWidget):
    """Customer video player used by the PyTouchAnalysis program"""

    def __init__(self, main, player):
        """Function to initialise the class"""
        super(TControls, self).__init__()

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
        play = QtGui.QPushButton(QtGui.QIcon('resources/play.png'), '')
        pause = QtGui.QPushButton(QtGui.QIcon('resources/pause.png'), '')

        # connect to the correct functions
        play.clicked.connect(self.player.play)
        pause.clicked.connect(self.player.pause)

        # add buttons to the grid
        grid.addWidget(play, 0, 0)
        grid.addWidget(pause, 0, 1)
