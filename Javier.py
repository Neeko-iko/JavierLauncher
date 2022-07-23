from PySide6 import QtWidgets
from Internals import ui


class MainJavier(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Main()
        self.ui.setupUi(self)


app = QtWidgets.QApplication()
widget = MainJavier()

widget.show()
app.exec()