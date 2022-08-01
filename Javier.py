#!/usr/local/bin/python3
from re import T


try:
    import os
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
        self.selectedDir = None

    # Nontabbed buttosn/other code
        self.ui.logClearButton.clicked.connect(lambda : self.ui.miniSole.setPlainText(""))
        
        
    # Launcher Tab Code
        self.refreshingServers(False)
        self.ui.serverRefreshButton.clicked.connect(lambda : self.refreshingServers())
        self.ui.searchBar.returnPressed.connect(lambda : self.refreshingServers())
        
        self.ui.startButton.clicked.connect(lambda : self.Startup())


    # Settings Tab Code
        self.subsequentdirs = False
        self.refreshingDirs(False)
        self.refreshThemes(False)
        self.ui.addDirbutton.clicked.connect(self.addDir)
        self.ui.themeRefresh.clicked.connect(lambda: self.refreshThemes())

        





    def addDir(self):
        direc = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select ur cur"))
        if direc != "":
            if direc not in jdb.readServerPaths():
                jdb.addServerPath(str(direc))
                self.printl(f"Successfully added {direc}!")
                self.refreshingDirs()
                self.refreshingServers()
            else:
                self.printl(f"{direc} is already saved! can't save it again!")
        else: # im sure there's probably a better way for this
            self.printl("Adding new directory was aborted.......")

    @QtCore.Slot()  # ngl i have no idea what this does, is it necessary?????
    def printl(self, string):
        self.ui.miniSole.appendPlainText(string)

    


    def setServer(self, name, dire):
        self.printl(f"Selected: {name}")
        self.ui.startButton.setText(f"Start {name}")
        self.selectedDir = dire

    def Startup(self):
        name = self.ui.startButton.text()[6:]
        ram = self.ui.ramEnter.text()
        self.printl(ram)
        if self.selectedDir == None:  ## i'll figure out a better way of doing this later
            self.printl("You need to select a server! You can't just start nothing!")
            return
        
        self.printl(f"Starting {name}")

        a = threading.Thread(target= serverRelated.runServer, args=(name, self.selectedDir, ram))
        a.start()
    def delDirs(self, dire):
        jdb.delServerPath(dire)
        self.refreshingDirs()
        self.refreshingServers()

    def updateTheme(self, theme):
        jdb.updateSettingValue("CurrentTheme", theme)
        self.printl("Javier will apply this theme upon reboot!")
        
    
    


    def refreshingServers(self, subs = True):
        self.ui.scrollAreaWidgetContents.setFixedHeight(450)
        if subs:
            for button in self.buttonlist:
                self.SButtonFrames.removeWidget(button)
                shiboken6.delete(button)
            for favorite in self.favorlist:
                self.SButtonFrames.removeWidget(favorite)
                shiboken6.delete(favorite)
            shiboken6.delete(self.SButtonFrames)
            del self.SButtonFrames
        
        self.SButtonFrames = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents)
        self.SButtonFrames.setContentsMargins(0,0,0,0) # probably a better way to do this!
        self.thisvarsucks = True
        self.buttonlist = []
        self.favorlist = []
        directories = list(jdb.readServerPaths())
        directories.append(".")
        print(directories)
        for i in range(0, len(directories)):
            dire = str(directories[i])
            if dire.isdigit():
                continue

            servers = serverRelated.folders(dire) 
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
                self.serverButton.clicked.connect(lambda _=False, e =server, d = dire: self.setServer(e, d))
                self.buttonlist.append(self.serverButton)
                if len(self.buttonlist) > 10:
                    self.ui.scrollAreaWidgetContents.setFixedHeight(self.ui.scrollAreaWidgetContents.height() +45)

        for i in range (0, len(self.buttonlist)):

            self.SButtonFrames.addWidget(self.buttonlist[i], i+1,1,1,1)
            self.SButtonFrames.addWidget(self.favorlist[i],i+1,0,1,1)
        self.printl("Servers Refreshed successfully!")

    def refreshingDirs(self, subs = True):
        if subs:
            for button in self.dirbuttlist:
                self.DButtonframes.removeWidget(button)
                shiboken6.delete(button)
            for delbutton in self.deldirlist:
                self.DButtonframes.removeWidget(delbutton)
                shiboken6.delete(delbutton)
            shiboken6.delete(self.DButtonframes)
            del self.DButtonframes
        self.DButtonframes = QtWidgets.QGridLayout(self.ui.dirScrollerWidget)
        self.DButtonframes.setContentsMargins(0,0,0,0)
        directs = jdb.readServerPaths()
        self.dirbuttlist = []
        self.deldirlist = []
        for i in range (0, len(directs)):
            dire = str(directs[i])
            print(dire)
            if dire.isdigit():
                continue
            
            self.deldirbutton = QtWidgets.QToolButton(text='DEL')
            self.deldirbutton.setFixedSize(30,30)
            self.deldirbutton.clicked.connect(lambda _=False, d = dire: self.delDirs(d))
            self.deldirlist.append(self.deldirbutton)


            self.directButton = QtWidgets.QPushButton(str(dire))
            self.directButton.setFixedSize(500,30)
            self.directButton.setContentsMargins(0,0,0,0)
            self.directButton.clicked.connect(lambda _=False, e = dire: self.printl(e))
            self.dirbuttlist.append(self.directButton)
            if len(self.buttonlist) > 10:
                    self.ui.dirScrollerWidget.setFixedHeight(self.ui.dirScrollerWidget.height() +45)
        for i in range (0, len(self.dirbuttlist)):
            
            self.DButtonframes.addWidget(self.dirbuttlist[i], i,1,1,1)
            self.DButtonframes.addWidget(self.deldirlist[i],i,0,1,1)
        self.subsequentdirs = True
    def refreshThemes(self, subs = True): # i absolutely love reusing HUGE chunks of code 3 times because im incompetent!!! it *will* happen again.
        self.printl("Themes are currently not working- should be soon!") # remove this later.
        if subs:
            for button in self.themebutts:
                self.TButtonframes.removeWidget(button)
                shiboken6.delete(button)
            shiboken6.delete(self.TButtonframes)
            del self.TButtonframes
        self.TButtonframes = QtWidgets.QVBoxLayout(self.ui.themeArea)
        self.TButtonframes.setContentsMargins(0,0,0,0)
        self.themebutts = []

        self.deftheme = QtWidgets.QToolButton(text= "System")
        self.deftheme.setFixedSize(215,45)
        self.deftheme.setStyleSheet("") # this makes it ignore the current theme
        self.deftheme.clicked.connect(lambda _=False : self.updateTheme("NULL"))
        self.themebutts.append(self.deftheme)
        self.TButtonframes.addWidget(self.deftheme)

        themelist = os.listdir("./Internals/themes")
        for theme in themelist:
            if theme[-4:] != ".jss":
                continue
            th = open("./Internals/themes/"+theme, "r")
            the = th.readline().strip()[2:]
            th.close()
            del th

            self.themebutton = QtWidgets.QToolButton(text=theme[:-4])
            self.themebutton.setFixedSize(215,45)
            self.themebutton.setStyleSheet(the)
            self.themebutton.clicked.connect(lambda _=False, d = theme: self.updateTheme("./Internals/themes/"+d))
            self.themebutts.append(self.themebutton)
            self.TButtonframes.addWidget(self.themebutton)
        


app = QtWidgets.QApplication()
widget =MainJavier()
if jdb.readSettingValue("CurrentTheme") != ():
    sheet= open("./Internals/themes/Dark.jss", "r")
    style = sheet.readlines()
    sheet.close()
    sheet = "" # don't act like im unaware of the malpractice done here.
    for item in style:
        if item[:2] == "//":
            continue
        sheet = sheet + item
    widget.setStyleSheet(sheet)
    widget.printl("Loaded Theme succesfully!")
widget.setWindowIcon(QtGui.QIcon("./Internals/resources/icon.png"))

widget.show()
app.exec()