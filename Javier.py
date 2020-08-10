import tkinter
import time
import os
import zipfile
import json
from tkinter import filedialog
from os import path
toggle = True



def dump(dta):
    if path.exists(f"{path.dirname(__file__)}/;Javier Settings;"):
        with open(f'{path.dirname(__file__)}/;Javier Settings;/Javier.json', 'w') as f:
            json.dump(dta, f, indent=4)
    else:
        with open(f'{path.dirname(__file__)}/Javier.json', 'w') as f:
            json.dump(dta, f, indent=4)

def addDir(gui):    ## code to create a new window that's basically a menu to add or delete directories.


    def deleteDir(dirStr, dirwindow, gui):  ## function that saves the action to the json, 
        print(dirStr)                        #then relaunches the window due to me not knowing how to update it in real time oops sorry.
        data['dirs'].remove(dirStr)
        dump(data)
        dirwindow.destroy()
        addDir(gui)
        

    def addNewDir(dirwindow, gui, dirStr):     # creates an empty dir for the user to update
        directory = filedialog.askdirectory(master =dirwindow, initialdir=".", title= "Select a folder", mustexist=True)
        data['dirs'].append(directory)
        dump(data)
        dirwindow.destroy()
        addDir(gui)

    

    dirwindow = tkinter.Toplevel(gui, bg = "DARK GREY")   # this makes the new window
    label = tkinter.Label(dirwindow, text="Add your directories below!", bg = "DARK GREY", fg="BLACK")  # creates the label saying "enter the dirs!"
    label.pack()  # this is required for the label to show up, if its not packed it may as well not exist lmao

    buttonContainer = tkinter.Frame(dirwindow, bg= '#40444B',height = 160, width = 120)  ## frame for the scrolling container.
    buttonCanvas = tkinter.Canvas(buttonContainer, bg= '#40444B', height = 150, width = 123) ## canvas that goes into the frame because frames can't have scrollbars because tkinter is awful.
    scroll = tkinter.Scrollbar(buttonContainer, orient='vertical', command = buttonCanvas.yview, bg= '#40444B') #the scroll bar itself
    buttonFrame = tkinter.Frame(buttonCanvas, bg= '#40444B')  # the frame that the buttons go in because iirc they're wonky on canvas..
    buttonFrame.bind("<Configure>",lambda e: buttonCanvas.configure(scrollregion=buttonCanvas.bbox("all"))) 
    buttonCanvas.create_window((0,0), window=buttonFrame, anchor = 'nw')
    buttonCanvas.configure(yscrollcommand=scroll.set)                    

    for i in range(0, len(data['dirs'])):  ## FOR loop makes buttons according to how many there are in 
        direntry = tkinter.Entry(buttonFrame, width =14, bg="WHITE", fg="BLACK")  ## an entry is a small textbox, they're cleaner than just big text blocks imo.
        direntry.insert(0, data['dirs'][i])  ## this inserts the name of the DIR into the text box. allowing the user to edit it or something ig idk this entire thing barely works ngl.
        direntry.grid(row = i+1, column =0)  ## grid tells where to place it.  run it to understand it.
        delete = tkinter.Button(buttonFrame, width = 1, text= "X", bg = "RED", fg="WHITE", command = lambda i= direntry.get(): deleteDir(i, dirwindow, gui))  ## this is the X button that deletes the DIR from the list in the JSON
        delete.grid(row = i+1, column = 1) 
        place = i+2  ## im bad.
    
    addnewButton = tkinter.Button(buttonFrame, width = 14, text = "ADD NEW DIR", bg = "GREEN", fg = "WHITE", command = lambda: addNewDir(dirwindow, gui, direntry.get()))  ## button to run code to add empty dir for user to edit.
    addnewButton.grid(row = place, column = 0)

    buttonContainer.pack() # the scrolling frame is packed here isntead of earlier - it doesn't really matter where its packed as long as it is,
    buttonCanvas.pack(side = 'left', fill = 'both')
    scroll.pack(side = 'right',fill = 'y')





def safeTog(safeStr):  # code to toggle the safemode on/off
    safe = safeStr.get()[10:]
    if safe == "OFF":
        safeStr.set("Safemode: ON")
    else:
        safeStr.set("Safemode: OFF")
    return safeStr

def guiTog(guiStr):  # code to toggle the nogui flag on/off
    tog = guiStr.get()[5:]
    if tog == "ON":
        guiStr.set("GUI: OFF")
    else:
        guiStr.set("GUI: ON")
    return guiStr



def ThemeChange(theme, gui):  # code to update the theme.  still requires a restart as idk how to make javier update in real time.
    global data
    data["curTheme"] = theme
    dump(data)
    #jsonfile = open("./Javier.json", 'w')
    #json.dump(data, jsonfile, indent = 4)
    #jsonfile.close()
    print("These changes will apply next time Javier is launched.")

def aboutWindow():  # this literally just opens the users browser to take them to the FAQ.
    import webbrowser
    webbrowser.open_new("https://github.com/Neeko-iko/JavierLauncher#FAQ")
    del webbrowser



def conformWindow(gui):   # this deforms the window to show the settings page - im pretty sure its really inefficient but its also really cool so leave me be please :C
    global toggle
    if toggle:
        toggle = False
        gui.title("Javier - Minecraft Server Launcher              |        Settings")
        gui.minsize(500, 363)
        gui.maxsize(500, 363)
    else:
        toggle = True
        gui.title("Javier - MCSL")
        gui.maxsize(250, 363)
        gui.minsize(250, 363)
def dataupdate(server):  # when adding launch flags Javier would complain about indexing, so i have it make a list for every server you click on.
    data['servers'][server] = ['', '']
    dump(data)
    #jsonfile = open("./Javier.json", 'w')
    #json.dump(data, jsonfile, indent = 4)
    #jsonfile.close()

def confirmUpdate(server, RAM, selectStr, customs, d):  # code to select a server, not launch it.
    global dire
    dire = d

    #awful check to see if the key is wrong, or if the index is incorrect.
    try:
        data['servers'][server][2]
    except KeyError:
        dataupdate(server)
    except IndexError:
        pass



    selectStr.set(f"Start: {server}") # this updates the start button to show the server name in the worst way possible.
    try:
        if data['servers'][server][0] != '':
            RAM.delete(0, "end")
            RAM.insert(0,data['servers'][server][0])  # inserts the ram value found in the JSON
        else:
            print("No Ram found insert it using the box if you may.")
    except KeyError:
        print("No Ram found insert it using the box if you may.")
    try:
        if data['servers'][server][1] != '':
            customs.delete(0, "end")
            customs.insert(0, data['servers'][server][1]) # inserts the flags found in the JSON.
    except KeyError:
        pass
    return dire





def javierLaunch(selectStr, RAM, gui, safeStr, customs, guiStr, dire):
    dire = data['dirs'][dire]
    nogui = ''
    if guiStr.get()[5:] == "OFF":
        nogui="nogui"
    

    if selectStr.get() == "Start: None":
        print("please select a server")
        return
    else:
        server = selectStr.get()
        server = server[7:]

    try:
        data['servers'][server][1]
    except:
        data['servers'][server][1] = ''
    ## Code to grab the RAM value from everything available
    print(server)
    maxRAM = RAM.get()
    if maxRAM == '' or not maxRAM.isdigit():
        if not maxRAM.isdigit():
            print("RAM value wasn't entered properly reverting to JSON...")
        try:

            maxRAM = data['servers'][server][0]
            print(data['servers'][server][0])
        except KeyError:
            maxRAM = 'p'
            while not maxRAM.isdigit():
                maxRAM = input("Ram was not entered, or not found in the JSON, please enter a ram amount to save to the JSON file.")
                data['servers'][server][0] = int(maxRAM)
    else:
        data['servers'][server][0] = int(maxRAM)

    ## code to try and grab launch options from the JSON

    customs = customs.get()
    if customs == '':
        try:
            customs = data['servers'][server][1]
        except:
            pass
    else:
        data['servers'][server][1] = customs
    dump(data)
    #jsonfile = open("./Javier.json", 'w')
    #json.dump(data, jsonfile, indent = 4)
    #jsonfile.close()

    ## Code to find the right JAR file to launch
    file = []
    safe = safeStr.get()[10:]
    for item in os.listdir(f"{dire}/{server}"):
        if item[-4:] == '.jar':
            file.append(item)
    if len(file) > 1:
        for item in file:
            print(item)
            check = zipfile.ZipFile(f"{dire}/{server}/{item}",'r')
            check = check.open('META-INF/MANIFEST.MF','r')
            check = check.readlines()
            for line in check:
                if 'net.minecraft.server.MinecraftServer' in str(line):
                    if safe == "ON":
                        file = item
                        break
                    else:
                        file.remove(item)
    try:
        if safe != "ON":
            file = file[0]
    except:
        print("something went wrong. . .")
        return
    ## Actual launch code.
    back = os.getcwd()
    gui.destroy()   #DESTORYS JAVIER WITH FACTS AND LOGIC - because i don't wanna thread him yet.  i'll do that after 1.7 - it'll probably have to be a 2.0 update.
    #del check, safe

    while True:
        os.chdir(f"{dire}/{server}")
        os.system(f"java -Xmx{maxRAM}G -Xms256M {customs} -jar {file} {nogui}")

        os.chdir(back)
        print("\n\nit seems as though the server has crashed or was stopped forcibly.\n\n\n\nrestarting the server in 10 seconds...")
        for i in range (10, 0, -1):
            print(str(i) + " seconds remaning\n\n\n")
            time.sleep(1)


def getdata():
    ## Searching for the JSON file to pull RAM values from
    try:
        if path.exists(f"{path.dirname(__file__)}/;Javier Settings;"):
            with open(f'{path.dirname(__file__)}/;Javier Settings;/Javier.json', 'r') as f:
                data = json.loads(f.read())
        else:
            with open(f'{path.dirname(__file__)}/Javier.json', 'r') as f:
                data = json.loads(f.read())
    except FileNotFoundError:
        data = {"dirs":["."],"servers":{},"themes":{"Dark": ["#FFFFFF", "#36393F"],"HC": ["#FFFFFF", "#161719"],"Light": ["#161719", "#FFFFFF"]},"curTheme":"Dark"}
        dump(data)
        if path.exists(f"{path.dirname(__file__)}/;Javier Settings;"):
            jsonfile = open(f"{path.dirname(__file__)}/;Javier Settings;/Javier.json")
        else:
            jsonfile = open(f"{path.dirname(__file__)}/Javier.json")
        data = json.load(jsonfile)
        jsonfile.close()
    return data


def getServers(dires):
    servers = []
    serv = []
    ## finds every folder in the directory given.  if "javier" is passed, it checks the folder javier is in.
    for dire in dires:
        if not path.isdir(dire):
            data['dirs'].remove(dire)
            servers = [["ERROR - RESTART"]]
            #if os.path.exists(f"{os.path.dirname(__file__)}/;Javier Settings;"):
            #    jsonfile = open(f"{os.path.dirname(__file__)}/;Javier Settings;/Javier.json", 'w')
            #else:
            #    jsonfile = open(f"{path.dirname(__file__)}/Javier.json", 'w')
            #json.dump(data, jsonfile, indent = 4)
            #jsonfile.close()
            dump(data)
            return servers

        with os.scandir(dire) as lservers:
            for item in lservers:
                if path.isdir(path.abspath(item)):
                    if item.name != ";Javier Settings;":
                        serv.append(item.name)
            servers.append(serv)
            serv = []
    return servers


## GUI code
def runGUI():


    gui = tkinter.Tk()
    if path.isfile(f"{path.dirname(__file__)}/;Javier Settings;/icons/Javier.ico"):
        gui.iconbitmap(f"{path.dirname(__file__)}/;Javier Settings;/icons/Javier.ico")  # doesn't work, im a terrible programmer lmao   will prolly fix later
    gui.title("Javier - MCSL")
    gui.configure(bg = 'white')
    gui.minsize(250, 363)
    gui.maxsize(250, 363)
    ## IK it seems redundant to make the min/max the same, but it makes Javier not resizable, saving me a lot of headache.  don't try to change this, it won't help you.


    background = data["themes"][data["curTheme"]][1]  #grabs the BG and FG colors for the theme the user is currently using.
    foreground = data["themes"][data["curTheme"]][0]

    ## Frames


    JavierFrame = tkinter.Frame(gui, height =360, width = 250, bg = '#40444B')
    JavierFrame.grid(row=0, column = 0)

    settingsFrame = tkinter.Frame(gui,height =363, width = 250, bg = '#40444B')
    settingsFrame.grid(row=0, column = 1)

    ramFrame = tkinter.Frame(JavierFrame, height = 60, width = 250, bg = '#40444B')
    ramFrame.pack()

    ## Buttons in settings and similar things.

    safeStr = tkinter.StringVar(value='Safemode: OFF')
    safeButton = tkinter.Button(settingsFrame, command = lambda: safeTog(safeStr), bd=2, height = 1, width = 12, textvariable = safeStr, bg = background, fg = foreground)
    safeButton.place(x=-1, y=297)

    guiStr = tkinter.StringVar(value='GUI: OFF')
    guiTogButton = tkinter.Button(settingsFrame, command = lambda: guiTog(guiStr), bd=2, height = 1, width = 8, textvariable = guiStr, bg = background, fg = foreground)
    guiTogButton.place(x=92, y=297)

    customsFrame = tkinter.Frame(settingsFrame, bg=background)
    customsl = tkinter.Label(customsFrame, text = " ADVANCED: Launch Flags ", bg=background, fg=foreground)
    customs = tkinter.Entry(customsFrame, width=41, bg = background, fg = foreground, bd=2)
    customsl.pack()
    customs.pack()
    customsFrame.place(x=0, y=323)


    ## server list code

    buttonContainer = tkinter.Frame(JavierFrame, bg= '#40444B',height = 60, width = 255)
    buttonCanvas = tkinter.Canvas(buttonContainer, bg= '#40444B', height = 300, width = 229)
    scroll = tkinter.Scrollbar(buttonContainer, orient='vertical', command = buttonCanvas.yview, bg= '#40444B')
    buttonFrame = tkinter.Frame(buttonCanvas, bg= '#40444B')
    buttonFrame.bind("<Configure>",lambda e: buttonCanvas.configure(scrollregion=buttonCanvas.bbox("all")))
    buttonCanvas.create_window((0,0), window=buttonFrame, anchor = 'nw')
    buttonCanvas.configure(yscrollcommand=scroll.set)
    
    count = 0
    servers = getServers(data['dirs'])
    for d in servers:
        dlbl = tkinter.StringVar(value=data['dirs'][count])
        listdirL = tkinter.Label(buttonFrame, textvariable = dlbl, bg = foreground, fg=background, width= 33) # label is made to categorize by dir instead of just dumping everything out at once.
        if listdirL.cget('text') == '.':
            dlbl.set("Javier")
        listdirL.pack()
        for i in range(0, len(servers[count])):
            launchButton = tkinter.Button(buttonFrame, text=servers[count][i], width = 32, height=1, command = lambda i=i, d=d, count=count : confirmUpdate(servers[count][i], RAM, selectStr, customs, count), bg=background, fg=foreground, bd=2)
            launchButton.pack()
        count += 1
    newdirButton = tkinter.Button(buttonFrame, text="Add a Directory. . .", width = 32, height = 1, command= lambda : addDir(gui), bg=foreground, fg=background, bd=2)  # persistant button at the bottom to add a DIR.
    newdirButton.pack()

    buttonContainer.pack()
    buttonCanvas.pack(side = 'left', fill = 'both')
    scroll.pack(side = 'right',fill = 'y')

    ## stuff in the ramFrame


    RAM = tkinter.Entry(ramFrame, bd =2,width = 3, bg=background, fg=foreground)  # cute ram entry
    RAM.place(x=4, y=4)
    label = tkinter.Label(ramFrame, text="< < < Enter RAM", height = 0, bg='#40444B', fg= "#FFFFFF")
    label.place(x=27, y=4)

    SettingsButton = tkinter.Button(ramFrame, bd = 1, width = 10, bg=background, fg= "#9999FF", text="Settings", command= lambda : conformWindow(gui)) # the button that makes javier pop in and out his jacket.
    SettingsButton.place(x=46, y=34)

    aboutButton = tkinter.Button(ramFrame, bd=1, width = 4, bg=background, fg = "#FF9999", text = 'FAQ', command = aboutWindow)  # button to open the FAQ on javiers github.
    aboutButton.place(x=4, y=34)


    selectStr = tkinter.StringVar(value="Start: None")
    confirmBut = tkinter.Button(ramFrame, textvariable = selectStr, width = 17, height =3, command = lambda :  javierLaunch(selectStr, RAM, gui, safeStr, customs, guiStr, dire), bd=1, bg=background, fg=foreground)
    confirmBut.place(x=127, y=4)

    ### Themes


    ThemeMenu = tkinter.Frame(settingsFrame, bg= '#30443B')
    themeButtonContainer = tkinter.Frame(ThemeMenu, bg= '#40444B',height = 75, width = 75)
    themeButtonCanvas = tkinter.Canvas(themeButtonContainer, bg= '#40444B', height = 75, width = 75)
    themeScroll = tkinter.Scrollbar(themeButtonContainer, orient='vertical', command = themeButtonCanvas.yview, bg= '#40444B')
    themeButtonFrame = tkinter.Frame(themeButtonCanvas, bg= '#40444B')


    themeButtonFrame.bind("<Configure>",lambda e: themeButtonCanvas.configure(scrollregion=themeButtonCanvas.bbox("all")))
    themeButtonCanvas.create_window((0,0), window=themeButtonFrame, anchor = 'nw')

    themeButtonCanvas.configure(yscrollcommand=themeScroll.set)

    themeButtonContainer.pack(side="bottom")

    themeButtonCanvas.pack(side = 'left', fill = 'both')
    themeScroll.pack(side = 'right',fill = 'y')

    for theme in data["themes"]:
        themeButton = tkinter.Button(themeButtonFrame, text= (list(data["themes"].keys())[list(data["themes"].values()).index(data["themes"][theme])])   , width = 10, height=1, command = lambda theme=theme : ThemeChange((list(data["themes"].keys())[list(data["themes"].values()).index(data["themes"][theme])]), gui), bg=data["themes"][theme][1], fg=data["themes"][theme][0], bd=2, )
        themeButton.pack()


    themeLabel = tkinter.Label(ThemeMenu, width= 13, text = "Themes", bg = background, fg =foreground)
    themeLabel.pack(side='top')

    ThemeMenu.place(x=155, y=223)


    gui.mainloop()

## actual script.
print(os.path.isfile(f"{path.dirname(__file__)}/;Javier Settings;/icons/Javier.ico"))
dire = None
data = getdata()
runGUI()
