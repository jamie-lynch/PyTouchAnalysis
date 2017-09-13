"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui, QtCore


class TContentItem(QtGui.QLabel):
    """Custom widget which holds and displays a single content item"""

    clicked = QtCore.Signal()

    def __init__(self, main, content_path, image_path):
        """Function to initialise the class"""
        super(TContentItem, self).__init__('')

        # reference to main
        self.main = main

        # required variables
        self.content_path = content_path
        self.image_path = image_path

        # configure UI
        self.init_ui()

        # connect to the clicked signal
        self.clicked.connect(self.load_self)

    def init_ui(self):
        """Function to initialise the UI elements"""
        pixmap = QtGui.QPixmap(self.image_path)
        pixmap = pixmap.scaledToWidth(self.main.window_width*0.1)
        self.setPixmap(pixmap)

    def mouseReleaseEvent(self, event):
        """Reimplemented function called when mouse release occurs"""
        self.clicked.emit()

    def load_self(self):
        """Function which is called when the button is clicked to load self into the video"""
        self.main.player.load(self.content_path)