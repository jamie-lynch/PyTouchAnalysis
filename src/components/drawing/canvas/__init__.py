"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui, QtCore
from components.drawing import painters


class TCanvas(QtGui.QWidget):
    """Custom widget on which all of the drawing activities are done"""

    def __init__(self, main):
        super(TCanvas, self).__init__()

        # set reference to main
        self.main = main

        # set the attributes
        self.items = []
        self.custom_painters = {
            'straight_arrow': painters.TStraightArrayPainter(self),
            'freehand_arrow': painters.TFreehandArrowPainter(self),
            'line': painters.TLinePainter(self),
            'multipoint_arc': painters.TMultipointArcPainter(self),
            'multipoint_square_outline': painters.TMultipointSquareOutlinePainter(self),
            'multipoint_square_filled': painters.TMultipointSquareFilledPainter(self),
            'free': painters.TFreePainter(self)
        }
        self.current_painter = None

        # set the initial point
        self.point = QtCore.QPoint(0, 0)

        # set the widget to be see through
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        for item in self.items:
            self.custom_painters[item['painter']].draw(qp, item)
        qp.end()

    def mousePressEvent(self, event):
        if self.current_painter:
            self.current_painter.add(event)
            self.repaint()

    def set_current_painter(self, painter):
        """Function which sets the current painter"""
        if self.current_painter and painter == self.current_painter.name:
            self.current_painter = None
        else:
            self.current_painter = self.custom_painters[painter]

    def undo(self):
        """Function which undoes the last item added"""
        self.items = self.items[:-1]
        self.repaint()

    def clear(self):
        """Function which clears all of the items"""
        self.items = []
        self.repaint()
