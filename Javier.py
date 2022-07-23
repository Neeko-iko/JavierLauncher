import PySide6
from PySide6 import QtWidgets
from Internals import ui


class MainJavier(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Main()
        self.ui.setupUi(self)




if __name__ == "__main__":
    app = QtWidgets.QApplication()
    widget = MainJavier()

    #widget.resize(500, 696) # double the size of the original!!! that's right!! go big or go home!!!!!!!!!!!!!!!!!!
    #widget.setWindowTitle("Javier | MC Server Launcher")
    widget.show()
    app.exec()