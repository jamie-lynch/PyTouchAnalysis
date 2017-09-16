"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui, QtCore


class TSpeedSlider(QtGui.QWidget):
    """Custom slider used for controlling the speed of playback"""

    def __init__(self, player):
        """Function to initialise the class"""
        super(TSpeedSlider, self).__init__()

        # create attributes
        self.slider = None

        # set a reference to the video
        self.player = player

        # create the ui elements
        self.init_ui()

        # setup the slider
        self.setup_slider()

    def init_ui(self):
        """Function which creates the UI elements"""

        # Create a grid
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        # Create a slider
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal)

        # Create the symbols
        minus = QtGui.QLabel()
        minus.setPixmap(QtGui.QPixmap('resources/icons/minus.png'))
        plus = QtGui.QLabel()
        plus.setPixmap(QtGui.QPixmap('resources/icons/plus.png'))

        # Add it all to the grid
        grid.addWidget(minus, 0, 0)
        grid.addWidget(self.slider, 0, 1)
        grid.addWidget(plus, 0, 2)

    def setup_slider(self):
        """Function which sets up the logic of the slider"""

        # set the range and start value
        self.slider.setRange(0, 10)
        self.slider.setValue(10)
