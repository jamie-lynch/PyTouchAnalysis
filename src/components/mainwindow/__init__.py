"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

# Import Modules
from PySide import QtGui, QtCore
from PySide.phonon import Phonon
import os

# Import Components
from components import player


class MainWindow(QtGui.QMainWindow):
    """Custom QMainWindow element for the PyTouchAnalysis program"""

    def __init__(self):
        """Function to initialise the class"""
        super(MainWindow, self).__init__()

        self.init_ui()

        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("PyTouchAnalyser")

    def init_ui(self):
        """Function to create the UI elements"""

        central = QtGui.QWidget()
        hbox = QtGui.QHBoxLayout()
        central.setLayout(hbox)
        self.setCentralWidget(central)

        self.view = QtGui.QGraphicsView()
        self.scene = QtGui.QGraphicsScene()

        self.media_object = Phonon.MediaObject()
        self.video_widget = Phonon.VideoWidget()
        self.audio_output = Phonon.AudioOutput()

        Phonon.createPath(self.media_object, self.video_widget)
        Phonon.createPath(self.media_object, self.audio_output)
        file_path = '/Users/jamielynch/Documents/Projects/PyTouchAnalysis/test/MVI_0043.AVI'

        media_source = Phonon.MediaSource(file_path)
        self.media_object.setCurrentSource(media_source)

        self.proxy = QtGui.QGraphicsProxyWidget()
        self.proxy.setWidget(self.video_widget)
        self.proxy.prepareGeometryChange()
        self.proxy.setGeometry(QtCore.QRectF(QtCore.QPointF(0, 0), QtCore.QSizeF(QtCore.QSize(640, 480))))
        self.proxy.setPos(0, 0)
        self.proxy.show()

        self.scene.addItem(self.proxy)
        self.view.setScene(self.scene)

        hbox.addWidget(self.view)
        self.media_object.play()


