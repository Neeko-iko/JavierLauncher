#!/usr/bin/python3


try:
    import os
    import shiboken6
    from PySide6 import QtWidgets, QtGui, QtGui
    from PySide6.QtCore import Slot, QThread
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
        class JavaDLThread(QThread):
          def __init__(self):
            super().__init__()
            self.ver = 8
          def setVer(self, ver):
            self.ver = ver
          def run(self):
            serverRelated.dlJava(self.ver)
        self.jthread = JavaDLThread()
        self.serverManager = serverRelated.ServerThread()
    # Nontabbed buttosn/other code
        self.ui.logClearButton.clicked.connect(lambda : self.ui.miniSole.setPlainText(""))
        self.selectedServer = None
        self.ui.updateCheckerButton.setText("v"+jdb.version)
        self.ui.updateCheckerButton.clicked.connect(self.update)
    # Launcher Tab Code
        self.refreshingServers(False)
        self.ui.serverRefreshButton.clicked.connect(lambda : self.refreshingServers())
        self.ui.searchBar.returnPressed.connect(lambda : self.refreshingServers())
        self.ui.startButton.clicked.connect(lambda : self.Startup())
        


    #Settings Tab Code
        self.refreshingDirs(False)
        self.refreshingThemes(False)
        self.refreshingJavas(False)
        self.ui.addDirButton.clicked.connect(self.addDir)
        self.ui.javaRefresh.clicked.connect(lambda: self.refreshingJavas())
        self.ui.themeRefresh.clicked.connect(lambda: self.refreshingThemes())
        self.ui.saveSettings.clicked.connect(lambda : self.saveSettings())
        self.ui.defaultCheck.clicked.connect(lambda : self.forceful())
        self.ui.downJavaButton.clicked.connect(lambda : self.funkyJava())

    #Help Tab Code
        try:
            readme = open("./Internals/help.html", "r",encoding="UTF-8")
            self.ui.textEdit.setText(readme.read())
        except:
            self.printl("no help.html! this is ok...")
            self.ui.textEdit.setText("Javier is a work in progress.\nyou can find some information at https://github.com/neeko-iko/javierlauncher \nif you need assistance please contact @Neeko_iko on Twitter, or Neeko#7373 on Discord")

    @Slot(int)
    def on_progUpdate(self, p):
      #print("We proggin': ", p) #This is for debugging, p is equal to the number of bytes downloaded
      self.ui.javaDownBar.setValue(p)

    @Slot(bool)
    def on_javaDownloadFinish(self, flag):
        self.ui.javaDownBar.setMaximum(0)
        self.ui.javaDownBar.setValue(0)
        self.ui.javaDownBar.setMaximum(1)
        self.ui.javaDownBar.setEnabled(False)
        self.ui.downJavaButton.setEnabled(True)
        self.printl("Download complete!")


    def update(self):
        ### one day this will do something 
        self.ui.updateCheckerButton.setText("v"+jdb.version)
    #Not so funky anymore, Neeko
    def funkyJava(self):
      ver = self.ui.javaIntBox.text()
      self.jthread.setVer(ver)
      if not os.path.exists("./Internals/javas/java"+ver):
        jdb.progInit()
        self.ui.javaDownBar.setEnabled(True)
        self.ui.javaDownBar.setMaximum(0)
        self.ui.javaDownBar.setValue(0)
        self.ui.downJavaButton.setDisabled(True)
        self.printl("Attempting to download OpenJDK Java JRE "+ ver)
        #Java download
        self.jthread.start()
        while jdb.jfin == 0:
          if jdb.jready == 1:
            print("Size in Main Thread:", jdb.jsize)
            self.ui.javaDownBar.setMaximum(int(jdb.jsize))
            break
      else:
        self.printl("You already have Java "+ver+" installed!")
        self.ui.javaDownBar.setMaximum(1)
        self.ui.javaDownBar.setValue(0)
        self.ui.javaDownBar.setEnabled(False)
        self.ui.downJavaButton.setEnabled(True)
        return
        

    def forceful(self): # hopefully temporary code lol
        if self.selectedServer == None: #phenominal code, really
            self.ui.defaultCheck.setChecked(True)
            self.printl("You haven't selected a server!")
        else:
            self.refreshSettings()

    def refreshSettings(self):
        if self.ui.defaultCheck.isChecked():
                self.ui.jraEntry.setText(jdb.readSettingValue("DefaultJRA"))
                self.ui.sJavaOver.setText(jdb.readSettingValue("DefaultJava"))
                self.ui.jarFileEntry.setText("")
        else:
            self.ui.jraEntry.setText(jdb.readServerValue(self.selectedServer, "LaunchFlags"))
            self.ui.sJavaOver.setText(jdb.readServerValue(self.selectedServer, "JavaFilePath"))
            self.ui.jarFileEntry.setText(jdb.readServerValue(self.selectedServer, "JARName"))
            val = jdb.readServerValue(self.selectedServer, "RAM")
            if val != None and val != '':
                self.ui.ramEnter.setValue(val)
            else:
                self.ui.ramEnter.setValue(1)

    def saveSettings(self):
        if self.ui.defaultCheck.isChecked():
            jdb.updateSettingValue("DefaultJava", self.ui.sJavaOver.text())
            jdb.updateSettingValue("DefaultJRA", self.ui.jraEntry.text())
            self.printl("Saved settings as default!")
        else: #prm,graming at 2:30 AM like that's agood idea :) ) :)
            name = self.selectedServer 
            if jdb.readServer(name) == False:
                jdb.addServer(name)#it wasn't how could i forget these lines!!!????
            jdb.updateServerValue(name,"JavaFilePath", self.ui.sJavaOver.text())
            jdb.updateServerValue(name,"LaunchFlags", self.ui.jraEntry.text())
            jdb.updateServerValue(name, "JARName",self.ui.jarFileEntry.text())
            self.printl("Saved settings to "+name)
    def openDir(self, dire):
        if os.name == "nt":
            os.system("explorer " + dire)
        else:
            os.system("xdg-open " + dire)

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

    #@QtCore.Slot()  # ngl i have no idea what this does, is it necessary????? answer: yes! very necessary! it's useful to read up on what you're using before just slamming into it at full force.
    def printl(self, string):
        self.ui.miniSole.appendPlainText(string)

    def setServer(self, name, dire):
        self.printl(f"Selected: {name}")
        self.ui.startButton.setText(f"Start\n{name}")
        self.selectedServer = name
        self.selectedDir = dire
        self.ui.defaultCheck.setChecked(False)
        self.ui.serverSelectLabel.setText("Editing: " + name)
        self.refreshSettings()

    

    def Startup(self):
        name = self.selectedServer
        ram = self.ui.ramEnter.text()[:-3]
        if name == None:  ## i'll figure out a better way of doing this later
            self.printl("You need to select a server! You can't just start nothing!")
            return
        self.saveSettings() 
        print(jdb.readServerValue(name, "RAM"))
        print(ram != jdb.readServerValue(name, "RAM"))
        if ram != jdb.readServerValue(name, "RAM"):
            self.printl("updating " + name + " RAM to " + ram + "GB")
            jdb.updateServerValue(name, "RAM", ram)
        self.ui.defaultCheck.setChecked(False)
        dire = self.selectedDir if self.selectedDir != "." else os.getcwd()
        pathers = dire + "/"+name 
        if not os.path.isfile(pathers+"/eula.txt"):
            self.printl("By starting this server using Javier you accept Minecraft's EULA defined at \nhttps://www.minecraft.net/en-us/eula\n")
            eula = open(pathers+"/eula.txt", "w")
            eula.writelines("eula=true\n##READ UP ON THE EULA HERE: https://www.minecraft.net/en-us/eula\n\n#this was automagically signed by Qter Javier")
            eula.close
            del eula #TRASH!
        # need to uncheck it because my function is QUIRKY !
        self.printl(f"Starting {name}")
        self.ui.defaultCheck.setChecked(True)
        self.ui.serverSelectLabel.setText("No Server Selected!")
        self.ui.startButton.setText("Select a\nServer!")
        self.selectedServer = None

        self.refreshSettings()
        gui = "" if self.ui.jarGuiCheck.isChecked() else "nogui"
        self.serverManager.setProp(name, self.selectedDir, ram, gui)
        self.serverManager.start()
    def delDirs(self, dire):
        jdb.delServerPath(dire)
        self.refreshingDirs()
        self.refreshingServers()

    def updateTheme(self, theme):
        jdb.updateSettingValue("CurrentTheme", theme)
        self.printl("Javier will apply this theme upon reboot!")
        
    def updateJavas(self, java):
        if self.ui.defaultCheck.isChecked():
            jdb.updateSettingValue("DefaultJava",java)
            self.printl("set the default java as " + java)
        else: #prm,graming at 2:30 AM like that's agood idea :) ) :)
            name = self.selectedServer 
            jdb.updateServerValue(name,"JavaFilePath", java)
            self.printl("set " + name +"'s java as " + java)
    


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
                self.favorButton.setFixedSize(15,15)
                #490 is the max height
                self.serverButton = QtWidgets.QPushButton(str(server))
                #self.serverButton.setFixedSize(500,45)
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
            listsize =len(self.favorites["buttons"]) + len(self.normal["buttons"]) 
            height = int(500/(listsize+.1) - 10) if listsize < 10 else 45

            for i in range (0, len(self.favorites["buttons"])):
                self.favorites["buttons"][i].setFixedSize(500, height)
                self.SButtonFrames.addWidget(self.favorites["buttons"][i], i+1,1,1,1)
                self.SButtonFrames.addWidget(self.favorites["checks"][i],i+1,0,1,1)
            for i in range (0, len(self.normal["buttons"])): #this disgusts you as much as it does me
                self.normal["buttons"][i].setFixedSize(500, height)
                self.SButtonFrames.addWidget(self.normal["buttons"][i], i+len(self.favorites["buttons"])+1,1,1,1)
                self.SButtonFrames.addWidget(self.normal["checks"][i],i+len(self.favorites["buttons"])+1,0,1,1)
            

            
        self.printl("Servers Refreshed successfully!")

    def favoritism(self, server, button):
        if jdb.readServer(server) == False:
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
        
        if len(directs) < 4:
            height = int(150/(len(directs)+.1) - 5)
        else:
            height = 30
        for i in range (0, len(directs)):
            dire = str(directs[i])
            if dire.isdigit():
                continue
            
            self.deldirbutton = QtWidgets.QToolButton(text='DEL')
            self.deldirbutton.setFixedSize(30,height)
            self.deldirbutton.clicked.connect(lambda _=False, d = dire: self.delDirs(d))
            self.deldirlist.append(self.deldirbutton)
            self.deldirbutton.setContentsMargins(0,0,0,0)

            #132 is max height

            self.directButton = QtWidgets.QPushButton(str(dire))
            self.directButton.setFixedSize(500,height)
            self.directButton.setContentsMargins(0,0,0,0)
            self.directButton.clicked.connect(lambda _=False, e = dire: self.openDir(e))
            self.dirbuttlist.append(self.directButton)
            if len(self.dirbuttlist) > 10:
                    self.ui.dirScrollerWidget.setFixedHeight(self.ui.dirScrollerWidget.height() +45)
        for i in range (0, len(self.dirbuttlist)):
            
            self.DButtonframes.addWidget(self.dirbuttlist[i], i,1,1,1)
            self.DButtonframes.addWidget(self.deldirlist[i],i,0,1,1)
        self.subsequentdirs = True

    def refreshingThemes(self, subs = True): # i absolutely love reusing HUGE chunks of code 3 times because im incompetent!!! it *will* happen again.
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
        #self.deftheme.setFixedSize(155,45)
        self.deftheme.setStyleSheet("") # this makes it ignore the current theme (it doesn't and i don't know how.)
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
            #self.themebutton.setFixedSize(155,45)
            self.themebutton.setStyleSheet(the)
            self.themebutton.clicked.connect(lambda _=False, d = theme: '')
            self.themebutts.append(self.themebutton)
            self.TButtonframes.addWidget(self.themebutton)
        if len(self.themebutts) < 6: # max height is 291
            height = int(300/(len(self.themebutts)+.1) - 10)
        else:
            height = 45
        height = 120 if height > 120 else height
        for i in range (0, len(self.themebutts)):
            self.themebutts[i].setFixedSize(155, height)
        self.printl("Successfully refreshed themes!")
    
    #def themeCreation(self, subs = True): # A FOURTH TIME? WILL THERE BE A FIFTH? (yes! there will be!)
    #    if subs:
    #        for button in self.javabutts:
    #            self.JButtonframes.removeWidget(button)
    #            shiboken6.delete(button)
    #        shiboken6.delete(self.JButtonframes)
    #        del self.JButtonframes
    #    self.JButtonframes = QtWidgets.QVBoxLayout(self.ui.javaArea)
    #    self.JButtonframes.setContentsMargins(0,0,0,0)
    #    self.javabutts = []
    #def serverCreation(self):
    #    return

    def refreshingJavas(self, subs = True):
        if subs:
            for button in self.javabutts:
                self.JButtonframes.removeWidget(button)
                shiboken6.delete(button)
            shiboken6.delete(self.JButtonframes)
            del self.JButtonframes
        self.JButtonframes = QtWidgets.QVBoxLayout(self.ui.javaArea)
        self.JButtonframes.setContentsMargins(0,0,0,0)
        self.javabutts = []
        #self.deftheme.setFixedSize(155,45)

        javalist = os.listdir("./Internals/javas")
        expected = "java.exe" if os.name == "nt" else "java"
        for java in javalist:
            if not os.path.isfile("./Internals/javas/" + java + "/bin/" + expected):
                continue
            else:
                jpath =os.path.abspath("./Internals/javas/" + java + "/bin/" + expected) 
            self.javabutton = QtWidgets.QToolButton(text=java)
            self.javabutton.clicked.connect(lambda _=False, d = java: self.updateJavas(jpath))
            self.javabutts.append(self.javabutton)
            self.JButtonframes.addWidget(self.javabutton)
        if len(self.javabutts) < 6: # max height is 291
            height = int(300/(len(self.javabutts)+.1) - 10)
        else:
            height = 45
        height = 120 if height > 120 else height
        for i in range (0, len(self.javabutts)):
            self.javabutts[i].setFixedSize(155, height)
        self.printl("Successfully refreshed Javas!")
        

def filefinders():
    if not os.path.exists("./Internals"):
        os.mkdir("./Internals")
    if not os.path.exists("./Internals/themes"):
        os.mkdir("./Internals/themes") #will probably move this to launcher.py
    if not os.path.exists("./Internals/javas"): #eventually
        os.mkdir("./Internals/javas") # but since Javier.py is the current launcher
filefinders() # it'll be here! until the auto updater comes to be
app = QtWidgets.QApplication()
widget = MainJavier()
style = jdb.readSettingValue("CurrentTheme")
if style != '' and style != None:
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
if os.path.exists("./Internals/resources/icon.png"):
    widget.setWindowIcon(QtGui.QIcon("./Internals/resources/icon.png"))
serverRelated.progger.progUpdate.connect(widget.on_progUpdate)
serverRelated.jf.javaDownloadFinish.connect(widget.on_javaDownloadFinish)

widget.show()
app.exec()