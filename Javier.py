#!/usr/local/bin/python3
try:
    import shiboken6
    from PySide6 import QtWidgets, QtCore, QtGui
    from Internals import ui, serverRelated
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
        servers = serverRelated.folders()  # testing cuz it doesn't have proper functionality yet anyways. will remove in future update
        self.buttonlist = []
        self.favorlist = []
        for i in range(0, len(servers)):
            server = servers[i]

            self.favorButton = QtWidgets.QCheckBox(text='')
            self.favorButton.setFixedSize(20,20)
            self.favorlist.append(self.favorButton)
            self.serverButton = QtWidgets.QPushButton(str(server))
            self.serverButton.setFixedSize(500,45)
            self.serverButton.clicked.connect(lambda _=False, e =server: self.setServer(e))
            self.buttonlist.append(self.serverButton)
            if len(self.buttonlist) > 10:
                self.ui.scrollAreaWidgetContents.setFixedHeight(self.ui.scrollAreaWidgetContents.height() +45)
        for i in range (0, len(self.buttonlist)):
            #TODO: make sure to sort these for favorites fisrt using the TO BE JSON/MONGOvvv
            self.SButtonFrames.addWidget(self.buttonlist[i], i+1,1,1,1)
            self.SButtonFrames.addWidget(self.favorlist[i],i+1,0,1,1)

        


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
        for favorite in self.favorlist:
            self.SButtonFrames.removeWidget(favorite)
            shiboken6.delete(favorite)
        shiboken6.delete(self.SButtonFrames)
        del self.SButtonFrames
        #TODO: grab stuff from eventual mongo/json data
        self.SButtonFrames = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents)
        self.SButtonFrames.setContentsMargins(0,0,0,0)
        servers = serverRelated.folders()  # testing cuz it doesn't have proper functionality yet anyways. will remove in future update
        self.buttonlist = []
        self.favorlist = []
        for i in range(0, len(servers)):
            server = servers[i]
            if self.ui.searchBar.text() != '':
                if self.ui.searchBar.text() not in str(server):
                    continue
            
            self.favorButton = QtWidgets.QCheckBox(text='')
            self.favorButton.setFixedSize(20,20)
            self.favorlist.append(self.favorButton)

            self.serverButton = QtWidgets.QPushButton(str(server))
            self.serverButton.setFixedSize(500,45)
            self.serverButton.setContentsMargins(0,0,0,0)
            self.serverButton.clicked.connect(lambda _=False, e =server: self.setServer(e))
            self.buttonlist.append(self.serverButton)
            if len(self.buttonlist) > 10:
                self.ui.scrollAreaWidgetContents.setFixedHeight(self.ui.scrollAreaWidgetContents.height() +45)

        for i in range (0, len(self.buttonlist)):
            #TODO: make sure to sort these for favorites fisrt using the TO BE JSON/MONGO
            self.SButtonFrames.addWidget(self.buttonlist[i], i+1,1,1,1)
            self.SButtonFrames.addWidget(self.favorlist[i],i+1,0,1,1)


app = QtWidgets.QApplication()
widget = MainJavier()
widget.setWindowIcon(QtGui.QIcon("./Internals/resources/icon.png"))

widget.show()
app.exec()