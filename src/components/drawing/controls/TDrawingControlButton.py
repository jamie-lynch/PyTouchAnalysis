"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui


class TDrawingControlButton(QtGui.QPushButton):
    """Custom push button used to make the video controls"""

    def __init__(self, icon, label, action, parent_frame, checkable=False):
        """Function to initialise the class"""
        super(TDrawingControlButton, self).__init__(icon, label)

        # store the parent and action
        self.parent_frame = parent_frame
        self.action = action

        # set the button to be checkable
        self.setCheckable(checkable)

        # setup function for when button is clicked
        self.clicked.connect(self.on_click)

    def on_click(self):
        """Function which is called when the button is clicked"""
        if self.isCheckable() and self.isChecked():
            self.parent_frame.set_current_button(self)

        self.action()
