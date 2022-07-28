#!/usr/local/bin/python3
try:
    import threading
    import shiboken6
    from PySide6 import QtWidgets, QtCore, QtGui
    from Internals import ui, serverRelated, jdb
except ModuleNotFoundError as e:
    print("imports failed, see error")
    print(e)
    exit()

# honestly this is all way over my head- i don't work with classes generally haha
class MainJavier(QtWidgets.QWidget): # whoops sorry for the bad code down below!
    def __init__(self): # my bad guys i promise my code is ususally better than this
        super().__init__() # swear on it! i do! it's true!
        jdb.deploy() # the database initiizlaition! YAY! DB!!!! YAY
        self.ui = ui.Ui_Main()
        self.ui.setupUi(self)
        self.ui.refreshButton.clicked.connect(lambda : self.refreshingServers())
        self.ui.searchBar.returnPressed.connect(lambda : self.refreshingServers())
        self.ui.LogClearer.clicked.connect(lambda : self.ui.miniSole.setPlainText(""))
        
    # Launcher Tab Code
        self.thisvarsucks = False
        self.refreshingServers() # i love making long ass lines of code for no reason its gotta be my favorite thing lol
        self.ui.startButton.clicked.connect(lambda : self.Startup(self.ui.startButton.text()[6:] , self.dire, self.ui.ramEnter.text()))


    # Settings Tab Code
        self.ui.addDirbutton.clicked.connect(self.addDir)

        





    def addDir(self):
        direc = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select ur cur"))
        if direc != "":
            if direc not in jdb.readServerPaths():
                jdb.addServerPath(str(direc))
                self.printl(f"Successfully added {direc}!")
            else:
                self.printl(f"{direc} is already saved! can't save it again!")
        else: # im sure there's probably a better way for this
            self.printl("Adding new directory was aborted.......")

    @QtCore.Slot()  # ngl i have no idea what this does, is it necessary?????
    def printl(self, string):
        self.ui.miniSole.appendPlainText(string)

    


    def setServer(self, name, dire=None):
        self.printl(f"Selected: {name}")
        self.ui.startButton.setText(f"Start {name}")
        self.dire = dire
    def Startup(self, name, dire, RAM):
        if name == " a Server":  ## i'll figure out a better way of doing this later
            self.printl("You need to select a server! You can't just start nothing!")
            return
        self.printl(f"'Starting {name}'")

        a = threading.Thread(target= serverRelated.runServer, args=(name, dire, RAM))
        a.start()

    def refreshing():

        return

    def refreshingServers(self):
        self.ui.scrollAreaWidgetContents.setFixedHeight(450)
        if self.thisvarsucks:
            for button in self.buttonlist:
                self.SButtonFrames.removeWidget(button)
                shiboken6.delete(button)
            for favorite in self.favorlist:
                self.SButtonFrames.removeWidget(favorite)
                shiboken6.delete(favorite)
            shiboken6.delete(self.SButtonFrames)
            del self.SButtonFrames
        self.thisvarsucks = True
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

            self.SButtonFrames.addWidget(self.buttonlist[i], i+1,1,1,1)
            self.SButtonFrames.addWidget(self.favorlist[i],i+1,0,1,1)
        self.printl("Servers Refreshed successfully!")


app = QtWidgets.QApplication()
widget =MainJavier()
widget.setWindowIcon(QtGui.QIcon("./Internals/resources/icon.png"))

widget.show()
app.exec()