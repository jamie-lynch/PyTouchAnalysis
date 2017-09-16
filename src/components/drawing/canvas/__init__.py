"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui, QtCore


class TCanvas(QtGui.QWidget):
    """Custom widget on which all of the drawing activities are done"""

    def __init__(self, main):
        super(TCanvas, self).__init__()

        # set reference to main
        self.main = main

        # set the attributes
        self.items = []

        # set the initial point
        self.point = QtCore.QPoint(0, 0)

        # set the widget to be see through
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        for item in self.items:
            self.drawText(qp, item)
        qp.end()

    def drawText(self, qp, item):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.drawText(item, 'TADA!')

    def mousePressEvent(self, event):
        self.items.append(QtCore.QPoint(event.x(), event.y()))
        self.repaint()

    def undo(self):
        """Function which undoes the last item added"""
        self.items = self.items[:-1]
        self.repaint()

    def clear(self):
        """Function which clears all of the items"""
        self.items = []
        self.repaint()
