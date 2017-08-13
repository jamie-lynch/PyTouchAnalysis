"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide.phonon import Phonon as Phonon


class Slider(Phonon.SeekSlider):
    """Custom Seek Slider used by the PyTouchAnalysis program"""

    def __init__(self, main, object):
        """Function to initialise the class"""
        super(Slider, self).__init__(object)

        # Create reference to the main window
        self.main = main
