"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui
from components.video.controls.TScrubSlider import TScrubSlider
from components.video.controls.TVideoControlButton import TVideoControlButton
from components.video.controls.TSpeedSlider import TSpeedSlider


class TVideoControlsFrame(QtGui.QFrame):
    """Custom frame which contains all of the video controls UI components"""

    def __init__(self, main, player):
        """Function to initialise the class"""
        super(TVideoControlsFrame, self).__init__()

        # Set reference to main window and video
        self.main = main
        self.player = player

        # set the frame style
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameShadow(QtGui.QFrame.Plain)

        # Create the UI
        self.init_ui()

    def init_ui(self):
        """Function which creates the UI"""

        # Create and set the grid as layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        # Create the sliders
        seek_slider = TSpeedSlider(self.player)
        scrub_slider = TScrubSlider(self.player)

        # Create the buttons
        play = TVideoControlButton(QtGui.QIcon('resources/icons/play.png'), '', self.player.play)
        pause = TVideoControlButton(QtGui.QIcon('resources/icons/pause.png'), '', self.player.pause)

        # add buttons to the grid
        grid.addWidget(scrub_slider, 0, 0, 1, 2)
        grid.addWidget(play, 1, 0)
        grid.addWidget(pause, 1, 1)
        grid.addWidget(seek_slider, 2, 0, 1, 2)
