
try:
    from PySide6 import QtWidgets, QtCore
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





        #TODO: grab stuff from eventual mongo/json data
        self.SButtonFrames = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents)
        self.ServerRefresh = QtWidgets.QPushButton("refreshing!")  # couldn't get this working in QTDesigner so i had to force it into the mian script
        self.SButtonFrames.addWidget(self.ServerRefresh, 0, 0, 1, 1) # not a super big deal just a little annoying :)
        servers = serverfinder.folders("test")  # testing cuz it doesn't have proper functionality yet anyways. will remove in future update
        for i in range(0, len(servers)):
            server = servers[i]
            self.ui.scrollAreaWidgetContents.setFixedHeight(self.ui.scrollAreaWidgetContents.height() +50)
            
            self.serverButton = QtWidgets.QPushButton(str(server))
            self.serverButton.setFixedSize(500,50)
            print(server)
            self.serverButton.clicked.connect(lambda e = server: self.setServer(e))
            self.SButtonFrames.addWidget(self.serverButton, i+1,0,1,1)
        
            

    @QtCore.Slot()
    def setServer(self, name):
        print(f"ah shit here we go again, {name}")
            
        
        

        
        

    




app = QtWidgets.QApplication()
widget = MainJavier()

widget.show()
app.exec()