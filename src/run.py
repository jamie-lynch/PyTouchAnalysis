"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

import sys
from PySide import QtGui
from components import mainwindow


def main():
    """Function which launches the PyTouchAnalysis program"""

    app = QtGui.QApplication(sys.argv)
    main = mainwindow.MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
