#!/usr/bin/python3
try:
    import os
    import threading
    import shiboken6
    from PySide6 import QtCore, QtGui, QtWidgets
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
        self.selectedServer = None
        
    # Launcher Tab Code
        self.refreshingServers(False)
        self.ui.serverRefreshButton.clicked.connect(lambda : self.refreshingServers())
        self.ui.searchBar.returnPressed.connect(lambda : self.refreshingServers())
        self.ui.startButton.clicked.connect(lambda : self.Startup())


    #Settings Tab Code
        self.refreshingDirs(False)
        self.refreshThemes(False)
        self.ui.addDirButton.clicked.connect(self.addDir)
        self.ui.themeRefresh.clicked.connect(lambda: self.refreshThemes())
        self.ui.saveSettings.clicked.connect(lambda : self.saveSettings())
        self.ui.defaultCheck.clicked.connect(lambda : self.forceful())

    #Help Tab Code
        readme = open("./Internals/help.html", "r",encoding="UTF-8")
        self.ui.textEdit.setText(readme.read())

    def forceful(self): # hopefully temporary code lol
        if self.selectedServer == None: #phenominal code, really
            self.ui.defaultCheck.setChecked(True)
            self.printl("You haven't selected a server!")

    def saveSettings(self):
        if self.ui.defaultCheck.isChecked():
            if self.ui.sJavaOver.text() != "":
                jdb.updateSettingValue("DefaultJava", self.ui.sJavaOver.text())
            if self.ui.jraEntry.text() != "":
                jdb.updateSettingValue("DefaultJRA", self.ui.jraEntry.text())
            self.printl("Saved settings as default!")
        else: #prm,graming at 2:30 AM like that's agood idea :) ) :)
            name = self.selectedServer
            if self.ui.sJavaOver.text() != "":
                jdb.updateServerValue(name,"JavaFilePath", self.ui.sJavaOver.text())
            if self.ui.jraEntry.text() != "":
                jdb.updateServerValue(name,"LaunchFlags", self.ui.jraEntry.text())
            if self.ui.jarFileEntry.text() != "":
                jdb.updateServerValue(name, "JARName",self.ui.jarFileEntry.text())
            self.printl("Saved settings to "+name)

    def addDir(self):
        direc = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select New Directory"))
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
        self.ui.startButton.setText(f"Start\n{name}")
        self.selectedServer = name
        self.selectedDir = dire
        self.ui.defaultCheck.setChecked(False)
        self.ui.serverSelectLabel.setText("Editing: " + name)

    def Startup(self):
        name = self.selectedServer
        ram = self.ui.ramEnter.text()[:-3]
        if name == None:  ## i'll figure out a better way of doing this later
            self.printl("You need to select a server! You can't just start nothing!")
            return
        if ram != jdb.readServerValue(name, "RAM"):
            self.printl("updating " + name + " RAM to " + ram + "GB")
            jdb.updateServerValue(name, "RAM", ram)
        self.ui.defaultCheck.setChecked(False)
        self.saveSettings() # need to uncheck it because my function is QUIRKY !
        self.printl(f"Starting {name}")
        self.ui.defaultCheck.setChecked(True)
        self.ui.serverSelectLabel.setText("No Server Selected!")
        self.ui.startButton.setText("Select a\nServer!")
        self.selectedServer = None

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
            for i in range (0, len(self.normal["buttons"])):
                self.SButtonFrames.removeWidget(self.normal["buttons"][i])
                self.SButtonFrames.removeWidget(self.normal["checks"][i])
                shiboken6.delete(self.normal["buttons"][i])
                shiboken6.delete(self.normal["checks"][i])
            for i in range (0, len(self.favorites["buttons"])):
                self.SButtonFrames.removeWidget(self.favorites["buttons"][i])
                self.SButtonFrames.removeWidget(self.favorites["checks"][i])
                shiboken6.delete(self.favorites["buttons"][i])
                shiboken6.delete(self.favorites["checks"][i])
            shiboken6.delete(self.SButtonFrames)
            del self.SButtonFrames
        
        self.SButtonFrames = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents)
        self.SButtonFrames.setContentsMargins(0,0,0,0) # probably a better way to do this!
        self.thisvarsucks = True
        self.normal = {"buttons":[], "checks":[] }
        self.favorites = { "buttons":[], "checks":[]}
        directories = list(jdb.readServerPaths())
        directories.append(".")
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

                self.serverButton = QtWidgets.QPushButton(str(server))
                self.serverButton.setFixedSize(500,45)
                self.serverButton.setContentsMargins(0,0,0,0)
                self.serverButton.clicked.connect(lambda _=False, e =server, d = dire: self.setServer(e, d))
                self.favorButton.clicked.connect(lambda _=False, e = server, d = self.favorButton : self.favoritism(e, d))
                favorite = bool(jdb.readServerValue(server, "IsFavorite"))
                if favorite:
                    self.favorButton.setChecked(True)
                    self.favorites["buttons"].append(self.serverButton)
                    self.favorites["checks"].append(self.favorButton)
                else:
                    self.normal["buttons"].append(self.serverButton)
                    self.normal["checks"].append(self.favorButton)
                if len(self.normal["buttons"]) + len(self.favorites["buttons"]) > 10:
                    self.ui.scrollAreaWidgetContents.setFixedHeight(self.ui.scrollAreaWidgetContents.height() +45)
            for i in range (0, len(self.favorites["buttons"])):
                self.SButtonFrames.addWidget(self.favorites["buttons"][i], i+1,1,1,1)
                self.SButtonFrames.addWidget(self.favorites["checks"][i],i+1,0,1,1)
            for i in range (0, len(self.normal["buttons"])): #this disgusts you as much as it does me
                self.SButtonFrames.addWidget(self.normal["buttons"][i], i+len(self.favorites["buttons"])+1,1,1,1)
                self.SButtonFrames.addWidget(self.normal["checks"][i],i+len(self.favorites["buttons"])+1,0,1,1)
            

            
        self.printl("Servers Refreshed successfully!")

    def favoritism(self, server, button):
        if jdb.readServer(server) == None:
            jdb.addServer(server)
        jdb.updateServerValue(server, "IsFavorite", int(button.isChecked()))


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
            if len(self.dirbuttlist) > 10:
                    self.ui.dirScrollerWidget.setFixedHeight(self.ui.dirScrollerWidget.height() +45)
        for i in range (0, len(self.dirbuttlist)):
            
            self.DButtonframes.addWidget(self.dirbuttlist[i], i,1,1,1)
            self.DButtonframes.addWidget(self.deldirlist[i],i,0,1,1)
        self.subsequentdirs = True
    def refreshThemes(self, subs = True): # i absolutely love reusing HUGE chunks of code 3 times because im incompetent!!! it *will* happen again.
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
        self.deftheme.clicked.connect(lambda _=False : self.updateTheme(None))
        self.themebutts.append(self.deftheme)
        self.TButtonframes.addWidget(self.deftheme)

        themelist = os.listdir("./Internals/themes")
        for theme in themelist:
            if theme[-4:] != ".qss":
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
style =jdb.readSettingValue("CurrentTheme") 
if style != None:
    sheet= open(style, "r")
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