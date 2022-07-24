#!/bin/
import shiboken6


try:
    from PySide6 import QtWidgets, QtCore, QtGui
    from Internals import ui, serverfinder
except ModuleNotFoundError as e:
    print("imports failed, see error")
    print(e)
    exit()


class MainJavier(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Main()
        self.ui.setupUi(self)

        self.ui.refreshButton.clicked.connect(lambda : self.Refreshing())
        self.ui.searchBar.returnPressed.connect(lambda : self.Refreshing())

        self.SButtonFrames = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents)
        self.SButtonFrames.setContentsMargins(0,0,0,0)
        servers = serverfinder.folders("test")  # testing cuz it doesn't have proper functionality yet anyways. will remove in future update
        self.buttonlist = []
        for i in range(0, len(servers)):
            server = servers[i]
            
            
            self.serverButton = QtWidgets.QPushButton(str(server))
            self.serverButton.setFixedSize(500,45)
            self.serverButton.clicked.connect(lambda _="garb", e =server: self.setServer(e))
            self.buttonlist.append(self.serverButton)
            if len(self.buttonlist) > 8:
                self.ui.scrollAreaWidgetContents.setFixedHeight(self.ui.scrollAreaWidgetContents.height() +45)
        for i in range (0, len(self.buttonlist)):
            self.SButtonFrames.addWidget(self.buttonlist[i], i+1,0,1,1)

        


        self.ui.startButton.clicked.connect(lambda : self.Startup(self.ui.startButton.text()[6:] ))


    def printl(self, string):
        self.ui.miniSole.appendPlainText(string)

    @QtCore.Slot()
    def setServer(self, name):
        self.printl(f"Selected: {name}")
        self.ui.startButton.setText(f"Start {name}")

    def Startup(self, name):
        self.printl(f"This doesn't work yet, but if it did, it'd say something like: 'Starting {name}'")

    def Refreshing(self):
        self.ui.scrollAreaWidgetContents.setFixedHeight(450)
        for button in self.buttonlist:
            self.SButtonFrames.removeWidget(button)
            shiboken6.delete(button)
        shiboken6.delete(self.SButtonFrames)
        del self.SButtonFrames
        #TODO: grab stuff from eventual mongo/json data
        self.SButtonFrames = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents)
        self.SButtonFrames.setContentsMargins(0,0,0,0)
        servers = serverfinder.folders("test")  # testing cuz it doesn't have proper functionality yet anyways. will remove in future update
        self.buttonlist = []
        for i in range(0, len(servers)):
            server = servers[i]
            if self.ui.searchBar.text() != '':
                if str(server) not in self.ui.searchBar.text():
                    continue
            
            
            self.serverButton = QtWidgets.QPushButton(str(server))
            self.serverButton.setFixedSize(500,45)
            self.serverButton.setContentsMargins(0,0,0,0)
            self.serverButton.clicked.connect(lambda _="garb", e =server: self.setServer(e))
            self.buttonlist.append(self.serverButton)
            if len(self.buttonlist) > 8:
                self.ui.scrollAreaWidgetContents.setFixedHeight(self.ui.scrollAreaWidgetContents.height() +45)

        for i in range (0, len(self.buttonlist)):
            self.SButtonFrames.addWidget(self.buttonlist[i], i+1,0,1,1)


app = QtWidgets.QApplication()
widget = MainJavier()
widget.setWindowIcon(QtGui.QIcon("./Internals/resources/icon.png"))

widget.show()
app.exec()