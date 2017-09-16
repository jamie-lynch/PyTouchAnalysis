"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui


class TDrawingControlButton(QtGui.QPushButton):
    """Custom push button used to make the video controls"""

    def __init__(self, icon, label, action, checkable=False):
        """Function to initialise the class"""
        super(TDrawingControlButton, self).__init__(icon, label)

        # set the button to be checkable
        self.setCheckable(checkable)

        # setup function for when button is clicked
        self.clicked.connect(action)
