"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui, QtCore


class TScrubSlider(QtGui.QSlider):
    """Custom slider used for scrubbing forwards and backwards through the video files"""

    def __init__(self, player):
        """Function to initialise the class"""
        super(TScrubSlider, self).__init__(QtCore.Qt.Horizontal)

        # set a reference to the video
        self.player = player
