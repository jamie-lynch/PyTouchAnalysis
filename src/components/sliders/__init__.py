"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

# Modules
from PySide import QtGui

# Components
from components.sliders.seekslider import TSeekSlider


class TSliders(QtGui.QWidget):
    """Customer widget which contains all of the sliders used"""

    def __init__(self, main, media_object):
        """Function to initialise the class"""
        super(TSliders, self).__init__()

        # reference to main window
        self.main = main
        self.media_object = media_object

        # create the UI
        self.create_ui()

    def create_ui(self):
        """Function which creates the UI"""

        # create the layout
        vbox = QtGui.QVBoxLayout()
        self.setLayout(vbox)

        # create the components required
        self.tseekslider = TSeekSlider(self.main, self.media_object)

        # add the components required
        vbox.addWidget(self.tseekslider)
