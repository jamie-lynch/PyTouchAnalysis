"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui


class TDrawingControlButton(QtGui.QPushButton):
    """Custom push button used to make the video controls"""

    def __init__(self, icon, label, action):
        """Function to initialise the class"""
        super(TDrawingControlButton, self).__init__(icon, label)
        self.clicked.connect(action)