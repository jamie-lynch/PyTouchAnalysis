"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide.phonon import Phonon as Phonon
import os


class Player(Phonon.VideoPlayer):
    """Customer video player used by the PyTouchAnalysis program"""

    def __init__(self, main):
        """Function to initialise the class"""
        super(Player, self).__init__(Phonon.VideoCategory)

        self.main = main


