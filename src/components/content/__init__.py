"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

# Modules
from PySide import QtGui

# Components
from components.content.tcontentitem import TContentItem


class TContent(QtGui.QWidget):
    """Custom widget which holds all of the available content"""

    def __init__(self, main):
        """Function to initialise the class"""
        super(TContent, self).__init__()

        # reference to main
        self.main = main

        # reference to each of the elements included
        self.elements = []

        # create the UI
        self.create_ui()

        # call the test function
        self.add_test_items()

    def add_test_items(self):
        """Function used for testing which adds three items"""
        # add three items for now
        content = ['../test/composite.avi', '../test/cookie.avi', '../test/crocus.avi']
        image = ['../test/composite.png', '../test/cookie.png', '../test/crocus.png']
        for c, i in zip(content, image):
            self.add_item(c, i)

    def create_ui(self):
        """Function to create the UI elements"""

        # create the layout
        self.hbox = QtGui.QHBoxLayout()
        self.setLayout(self.hbox)

    def add_item(self, content_path, image_path, index=None):
        """Function which adds a new TContentItem"""

        # create the new TContentItem
        new_item = TContentItem(self.main, content_path, image_path)

        # either add or insert it to both the layout and the list
        # depending on what the function was told to do
        if index:
            self.hbox.insertWidget(index, new_item)
            self.elements.insert(index, new_item)
        else:
            self.hbox.addWidget(new_item)
            self.elements.append(new_item)
