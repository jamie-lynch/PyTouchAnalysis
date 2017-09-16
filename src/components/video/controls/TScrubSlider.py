"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui, QtCore


class TScrubSlider(QtGui.QWidget):
    """Custom slider used for scrubbing forwards and backwards through the video files"""

    def __init__(self, player):
        """Function to initialise the class"""
        super(TScrubSlider, self).__init__()

        # create attributes
        self.slider = None

        # set a reference to the video
        self.player = player

        # create the ui elements
        self.init_ui()

        # setup the slider logic
        self.slider_setup()

    def init_ui(self):
        """Function which creates the UI elements"""

        # Create a grid
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        # Create a slider
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal)

        # Create the symbols
        minus = QtGui.QLabel()
        minus.setPixmap(QtGui.QPixmap('resources/icons/rewind.png'))
        plus = QtGui.QLabel()
        plus.setPixmap(QtGui.QPixmap('resources/icons/fast_forward.png'))

        # Add it all to the grid
        grid.addWidget(minus, 0, 0)
        grid.addWidget(self.slider, 0, 1)
        grid.addWidget(plus, 0, 2)

    def slider_setup(self):
        """Function which sets the slider logic"""
        # set the range and starting value
        self.slider.setRange(-10, 10)
        self.slider.setValue(0)

        # enable tracking so that the value can be tracked while the slider is dragged
        self.slider.setTracking(True)

        # when the slider is released then return to central
        self.slider.sliderReleased.connect(lambda: self.slider.setValue(0))

        # set the steps to zero (this stops people clicking on the bar to move the slider)
        self.slider.setSingleStep(0)
        self.slider.setPageStep(0)
