"""
PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

# Import Modules
from PySide import QtGui, QtCore

# Import Components
from components import player, controls, sliders, drawing, content


class MainWindow(QtGui.QMainWindow):
    """Custom QMainWindow element for the PyTouchAnalysis program"""

    def __init__(self):
        """Function to initialise the class"""
        super(MainWindow, self).__init__()

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
        # This is done to fool the video player into thinking its on the top
        self.view = QtGui.QGraphicsView()
        self.scene = QtGui.QGraphicsScene()

        # Create the player objects
        self.player = player.TPlayer(self)
        self.controls = controls.TControls(self, self.player)
        self.slider = sliders.TSliders(self, self.player.media_object)

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

        # Create the logo
        logo_label = QtGui.QLabel()
        logo_pixmap = QtGui.QPixmap('resources/lsu_media_logo.png')
        logo_pixmap = logo_pixmap.scaledToWidth(0.1 * self.window_width, QtCore.Qt.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)

        # create and add the drawing buttons
        self.drawing_tools = drawing.TDrawingTools(self)

        # create and add the content widget
        self.content_box = content.TContent(self)

        # Add each of the components to the grid
        grid.addWidget(self.view, 0, 1, 3, 1)
        grid.addWidget(self.content_box, 0, 3)
        grid.addWidget(self.drawing_tools, 0, 0)
        grid.addWidget(self.slider, 1, 0)
        grid.addWidget(self.controls, 2, 0)
        grid.addWidget(logo_label, 3, 0)

        # Play a video for test
        file_path = '/Users/jamielynch/Documents/Projects/PyTouchAnalysis/test/MVI_0043.AVI'
        self.player.load(file_path)
        self.player.play()

    def get_screen_geometry(self):
        """Function which gets and sets the screen size"""
        desktop = QtGui.QDesktopWidget()
        available = desktop.availableGeometry()
        self.window_height = available.height()
        self.window_width = available.width()
