from http import server
from Internals import serverfinder, settingsconfig
from PySide6 import QtCore, QtWidgets, QtGui
import sys
class MainScreen(QtWidgets.QWidget):
    def __init__ (self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Start Server!")

        self.label = QtWidgets.QLabel("This doesn't work, and it won't for a long time.")


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        self.button.clicked.connect(self.findServers)


    @QtCore.Slot()
    def findServers(self):
        self.label.setText(str(serverfinder.folders()))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainScreen()
    widget.resize(500, 696) # double the size of the original!!! that's right!! go big or go home!!!!!!!!!!!!!!!!!!
    widget.show()
    sys.exit(app.exec())