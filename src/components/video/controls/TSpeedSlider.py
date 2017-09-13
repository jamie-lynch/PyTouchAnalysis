"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui, QtCore


class TSpeedSlider(QtGui.QSlider):
    """Custom slider used for controlling the speed of playback"""

    def __init__(self, player):
        """Function to initialise the class"""
        super(TSpeedSlider, self).__init__(QtCore.Qt.Horizontal)

        # set a reference to the video
        self.player = player
