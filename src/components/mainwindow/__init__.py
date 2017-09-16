"""
PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

# Import Modules
from PySide import QtGui, QtCore

from components import video, drawing


class MainWindow(QtGui.QMainWindow):
    """Custom QMainWindow element for the PyTouchAnalysis program"""

    def __init__(self):
        """Function to initialise the class"""
        super(MainWindow, self).__init__()

        # Set attributes
        self.player = None
        self.canvas = None
        self.window_width = None
        self.window_height = None

        # Check the screen size
        self.get_screen_geometry()

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
        # This is done to fool the video video into thinking its on the top
        view = QtGui.QGraphicsView()
        scene = QtGui.QGraphicsScene()

        # Create the video objects
        self.player = video.TPlayer(self)
        controls = video.TVideoControlsFrame(self, self.player)

        # Create a proxy containing the video video
        video_proxy = QtGui.QGraphicsProxyWidget()
        video_proxy.setWidget(self.player)
        video_proxy.prepareGeometryChange()
        video_proxy.setGeometry(QtCore.QRectF(QtCore.QPointF(0, 0), QtCore.QSizeF(QtCore.QSize(640, 480))))
        video_proxy.setPos(0, 0)
        video_proxy.show()

        # Create a canvas
        self.canvas = drawing.TCanvas(self)

        # self.view.fitInView(self.proxy, QtCore.Qt.KeepAspectRatio)

        # Add the video proxy and the canvas to the scene
        scene.addItem(video_proxy)
        scene.addWidget(self.canvas)
        view.setScene(scene)

        # Create the logo
        logo_label = QtGui.QLabel()
        logo_pixmap = QtGui.QPixmap('resources/lsu_media_logo.png')
        logo_pixmap = logo_pixmap.scaledToWidth(0.08 * self.window_width, QtCore.Qt.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)

        # create and add the drawing buttons
        drawing_tools = drawing.TDrawingControlsFrame(self)

        # create and add the content widget
        content_box = video.TContentFrame(self)

        # Add each of the components to the grid
        grid.addWidget(drawing_tools, 0, 0)
        grid.addWidget(controls, 1, 0)
        grid.addWidget(logo_label, 2, 0)
        grid.addWidget(view, 0, 1, 2, 1)
        grid.addWidget(content_box, 2, 1)

        # centre the logo
        grid.setAlignment(logo_label, QtCore.Qt.AlignCenter)

        # set the row stretches so that the button row stays smaller
        grid.setRowStretch(0, 2)
        grid.setRowStretch(1, 2)
        grid.setRowStretch(2, 1)

        # Play a video for test
        file_path = '/Users/jamielynch/Documents/Projects/PyTouchAnalysis/test/composite.avi'
        self.player.load(file_path)
        self.player.play()

    def get_screen_geometry(self):
        """Function which gets and sets the screen size"""
        desktop = QtGui.QDesktopWidget()
        available = desktop.availableGeometry()
        self.window_height = available.height()
        self.window_width = available.width()
