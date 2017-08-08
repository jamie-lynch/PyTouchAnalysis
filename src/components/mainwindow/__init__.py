"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui


class MainWindow(QtGui.QMainWindow):
    """Custom QMainWindow element for the PyTouchAnalysis program"""

    def __init__(self):
        """Function to initialise the class"""
        super(MainWindow, self).__init__()

        self.setWindowTitle("PyTouchAnalyser")
