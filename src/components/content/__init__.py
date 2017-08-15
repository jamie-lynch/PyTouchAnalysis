"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui


class TContent(QtGui.QWidget):
    """Custom widget which holds all of the available content"""

    def __init__(self, main):
        """Function to initialise the class"""
        super(TContent, self).__init__()

        # reference to main
        self.main = main

        # create the UI
        self.create_ui()

    def create_ui(self):
        """Function to create the UI elements"""

        # create the layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
