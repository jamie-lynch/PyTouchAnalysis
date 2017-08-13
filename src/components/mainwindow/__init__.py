"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

# Import Modules
from PySide import QtGui, QtCore

# Import Components
from components import player


class MainWindow(QtGui.QMainWindow):
    """Custom QMainWindow element for the PyTouchAnalysis program"""

    def __init__(self):
        """Function to initialise the class"""
        super(MainWindow, self).__init__()

        # Create the user interface
        self.init_ui()

        # Set the window properties
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("PyTouchAnalyser")

    def init_ui(self):
        """Function to create the UI elements"""

        # Create central widget and layout
        central = QtGui.QWidget()
        grid = QtGui.QGridLayout()
        central.setLayout(grid)
        self.setCentralWidget(central)

        # Create a graphics view and scene
        # This is done to fool the video player into thinking its on the top
        self.view = QtGui.QGraphicsView()
        self.scene = QtGui.QGraphicsScene()

        # Create the player objects
        self.player = player.Player(main=self)

        # Create a proxy containing the video player
        video_proxy = QtGui.QGraphicsProxyWidget()
        video_proxy.setWidget(self.player)
        video_proxy.prepareGeometryChange()
        video_proxy.setGeometry(QtCore.QRectF(QtCore.QPointF(0, 0), QtCore.QSizeF(QtCore.QSize(640, 480))))
        video_proxy.setPos(0, 0)
        video_proxy.show()

        # Add the video proxy to the scene
        self.scene.addItem(video_proxy)
        self.view.setScene(self.scene)

        grid.addWidget(self.view, 0, 0)

        file_path = '/Users/jamielynch/Documents/Projects/PyTouchAnalysis/test/go1080p25.mp4'
        self.player.load(file_path)
        self.player.play()


