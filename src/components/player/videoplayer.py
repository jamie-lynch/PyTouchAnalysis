"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide.phonon import Phonon as Phonon


class Player(Phonon.VideoWidget):
    """Customer video player used by the PyTouchAnalysis program"""

    def __init__(self, main):
        """Function to initialise the class"""
        super(Player, self).__init__()

        # Reference to the main window
        self.main = main

        # Create a media object to be used by the player
        self.media_object = Phonon.MediaObject()

        # Create a path for the media object to the video player
        Phonon.createPath(self.media_object, self)

    def play(self):
        """Function which plays or resumes current source"""
        self.media_object.play()

    def pause(self):
        """Function which pauses current source"""
        self.media_object.pause()

    def load(self, filepath):
        """Function which loads in a new video from a provided filepath"""
        self.media_object.setCurrentSource(filepath)

    def seek(self, time):
        """Function which seeks to a current time based on the provided value in ms"""
        self.media_object.seek(time)

