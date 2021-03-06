import tkinter
import time
import os
import zipfile
import json
from tkinter import filedialog
from os import path
toggle = True
c = 0




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
        directory = filedialog.askdirectory(master =dirwindow, initialdir=".", title= "Select a folder")
        data['dirs'].append(directory)
        dump(data)
        dirwindow.destroy()
        addDir(gui)


    fg = data["themes"][data["curTheme"]][0]
    bg = data["themes"][data["curTheme"]][1]

    

    dirwindow = tkinter.Toplevel(gui, bg = bg)   # this makes the new window
    dirwindow.minsize(170, 170)
    dirwindow.maxsize(170, 170)
    label = tkinter.Label(dirwindow, text="Add your directories below!", bg =bg, fg=fg)  # creates the label saying "enter the dirs!"
    label.pack()  # this is required for the label to show up, if its not packed it may as well not exist lmao

    buttonContainer = tkinter.Frame(dirwindow, bg= bg,height = 160, width = 150)  ## frame for the scrolling container.
    buttonCanvas = tkinter.Canvas(buttonContainer, bg= bg, height = 150, width = 153) ## canvas that goes into the frame because frames can't have scrollbars because tkinter is awful.
    scroll = tkinter.Scrollbar(buttonContainer, orient='vertical', command = buttonCanvas.yview, bg= bg) #the scroll bar itself
    buttonFrame = tkinter.Frame(buttonCanvas, bg= bg)  # the frame that the buttons go in because iirc they're wonky on canvas..
    buttonFrame.bind("<Configure>",lambda e: buttonCanvas.configure(scrollregion=buttonCanvas.bbox("all"))) 
    buttonCanvas.create_window((0,0), window=buttonFrame, anchor = 'nw')
    buttonCanvas.configure(yscrollcommand=scroll.set)                    

    for i in range(0, len(data['dirs'])):  ## FOR loop makes buttons according to how many there are in 
        direntry = tkinter.Entry(buttonFrame, width =19, bg=bg, fg=fg)  ## an entry is a small textbox, they're cleaner than just big text blocks imo.
        direntry.insert(0, data['dirs'][i])  ## this inserts the name of the DIR into the text box. allowing the user to edit it or something ig idk this entire thing barely works ngl.
        direntry.grid(row = i+1, column =0)  ## grid tells where to place it.  run it to understand it.
        delete = tkinter.Button(buttonFrame, width = 1, text= "X", bg = "RED", fg="WHITE", command = lambda i= direntry.get(): deleteDir(i, dirwindow, gui))  ## this is the X button that deletes the DIR from the list in the JSON
        delete.grid(row = i+1, column = 1) 
        place = i+2  ## im bad.
    
    addnewButton = tkinter.Button(buttonFrame, width = 20, text = "ADD NEW DIR", bg = "GREEN", fg = "WHITE", command = lambda: addNewDir(dirwindow, gui, direntry.get()))  ## button to run code to add empty dir for user to edit.
    addnewButton.grid(row = place, column = 0, columnspan= 2, sticky=tkinter.W+tkinter.E)

    buttonContainer.pack() # the scrolling frame is packed here isntead of earlier - it doesn't really matter where its packed as long as it is,
    buttonCanvas.pack(side = 'left', fill = 'both')
    scroll.pack(side = 'right',fill = 'y')


def themeMaker():
    print("This isn't ready yet lmao :)))))))")


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
    data['servers'][server] = ['', '','']
    dump(data)

def confirmUpdate(server, RAM, selectStr, customs, d, javaOverride):  # code to select a server, not launch it.
    global dire
    global c
    dire = d

    java = javaOverride.get()
    if len(java) < 8:
        if java != "java":
            java = "java"
    data["java"] = java

    #awful check to see if the key is wrong, or if the index is incorrect.
    try:
        data['servers'][server][3]
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

    if c ==0:
        jarOverride.place(x=0, y=258)
        jarButton.place(x=180, y=257)
        jarButton.lower(javaLabel)
        jarOverride.lower(jarButton)
        
        
        c = True
    jarOverride.delete(0, "end")
    jarOverride.insert(0, data['servers'][server][2])

    return dire

    



def javierLaunch(selectStr, RAM, gui, safeStr, customs, guiStr, dire, javaOverride):
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
        data['servers'][server][2]  # 2 is jar file, this is stored as of 1.10 because I (Neeko)
    except:                     # have realized that Javier is not perfect, which while sad, means that the USER (the doofus reading this) 
        data['servers'][server][2] = '' # should be perfectly capable of solving his mistakes

    ## Code to grab the RAM value from everything available
    print(server)
    maxRAM = RAM.get()
    if maxRAM == '' or not maxRAM.isdigit():
        if not maxRAM.isdigit():
            print("RAM value wasn't entered properly reverting to JSON...")
        try:
            gui.withdraw()
            maxRAM = data['servers'][server][0]
            
            print(data['servers'][server][0])
            int(maxRAM) + 1
        except (KeyError, ValueError):
            print("!!!! IMPORTANT !!!\n\nRAM value was not entered, and not found in the JSON.\n")
            maxRAM = ''
            while not maxRAM.isdigit():
                maxRAM = input("Please enter a ram amount to save to the JSON file for future use:  ")
            data['servers'][server][0] = int(maxRAM)
    else:
        data['servers'][server][0] = int(maxRAM)  # if its not obvious by the code itself, 0 is ram

    ## code to try and grab launch options from the JSON

    customs = customs.get()
    if customs == '':
        try:
            customs = data['servers'][server][1]  # if its not obvious by the code itself, 1 is customs in the json.
        except:
            pass
    else:
        data['servers'][server][1] = customs


    java = javaOverride.get()
    if len(java) < 8:
        if java != "java":
            java = "java"
            data["java"] = "java"
            print("Mishap in Java Override, assuming Java Runtime is in PATH and continuing.")
    else:
        java = f'"{java}"'


    safe = safeStr.get()[10:]
    ## Code to find the right JAR file to launch
    file = data['servers'][server][2]
    if not path.isfile(f"{dire}/{server}/{file}") or safe == "ON":
        if safe == "OFF":
            print("Jar in override doesn't exist, attempting to find jar...")
        file = []
        for item in os.listdir(f"{dire}/{server}"):
            if item[-4:] == '.jar':
                file.append(item)
        if len(file) > 1:
            for item in file:
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
                data['servers'][server][2] = file
        except:
            print("something went wrong. . .")
            return
    dump(data)
    ## Actual launch code.

    back = os.getcwd()
    gui.destroy()   #DESTORYS JAVIER WITH FACTS AND LOGIC -because i (neeko) won't thread him.  i'll do that at Javier 2.0, if that ever comes around.
    #del check, safe
    
    os.chdir(back)
    while True:
        sTime = int(time.time())
        os.chdir(f"{dire}/{server}")
        try:
            open('eula.txt', 'r')
        except FileNotFoundError:
            print("EULA Was not found")
            input("pressing ENTER means you accept and understand the terms and conditions of the EULA\nThe license can be found at https://account.mojang.com/documents/minecraft_eula.\n If you do NOT accept the EULA, Close Javier now.")
            print("USER accepted the EULA, Starting server.")
            eula = open("eula.txt", 'w')
            eula.write('eula = true\n#This signature was automatically generated by Javier under USER Authorization.\n#find the EULA at https://account.mojang.com/documents/minecraft_eula')
            eula.close()
            print("EULA Created and signed! Have fun!")
            del eula
        
        print("Server Started!")
        os.system(f"{java} -Xmx{maxRAM}G -Xms256M {customs} -jar {file} {nogui}")
        

        if ( int(time.time()) - int(sTime) < 220):
            print("\n\nThe server appears to have crashed on startup, or something else went wrong. \n\nAuto-Restart will not commence, please check if anything went wrong, and then try running the server again. \n\npress enter or click the X to close this CMD.")
            input()
            break

        else:

            os.chdir(back)
            print("\n\nit seems as though the server has crashed or was stopped forcibly.\nfeel free to close the CMD if you want to close the server\n\n\notherwise the server will restart in 10 seconds...")
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
        data = {"java":"java","dirs":["."],"servers":{},"themes":{"Dark": ["#FFFFFF", "#36393F"],"High Contrast": ["#FFFFFF", "#000000"],"Light": ["#161719", "#FFFFFF"]},"curTheme":"Dark"}
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
    ## finds every folder in every directory given.
    for dire in dires:
        if not path.isdir(dire):
            data['dirs'].remove(dire)
            servers = [["ERROR - RESTART"]]
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

    def openExplorer(folder):
        back = os.getcwd()
        os.chdir(folder)
        if os.name == "nt":
            os.system("explorer .")
        else:
            os.system("xdg-open .")
        os.chdir(back)
        del back



    gui = tkinter.Tk()

    if path.isfile(f"{path.dirname(__file__)}/;Javier Settings;/icons/Javier.ico"):
        gui.iconbitmap(f"{path.dirname(__file__)}/;Javier Settings;/icons/Javier.ico")
    gui.title("Javier - MCSL")
    gui.configure(bg = 'white')
    gui.minsize(250, 363)
    gui.maxsize(250, 363)
    ## I know it seems redundant to make the min/max the same, but it makes Javier not resizable, saving me a lot of headache.  don't try to change this, it won't help you.


    background = data["themes"][data["curTheme"]][1]  #grabs the BG and FG colors for the theme the user is currently using.
    foreground = data["themes"][data["curTheme"]][0]

    ## Frames


    JavierFrame = tkinter.Frame(gui, height =360, width = 250, bg = background)
    JavierFrame.grid(row=0, column = 0)

    settingsFrame = tkinter.Frame(gui,height =363, width = 250, bg = background)
    settingsFrame.grid(row=0, column = 1)

    ramFrame = tkinter.Frame(JavierFrame, height = 60, width = 250, bg = background)
    ramFrame.pack()

    


    ## server list code

    buttonContainer = tkinter.Frame(JavierFrame, bg= background,height = 60, width = 255)
    buttonCanvas = tkinter.Canvas(buttonContainer, bg= background, height = 300, width = 229)
    scroll = tkinter.Scrollbar(buttonContainer, orient='vertical', command = buttonCanvas.yview, bg= background)
    buttonFrame = tkinter.Frame(buttonCanvas, bg= background)
    buttonFrame.bind("<Configure>",lambda e: buttonCanvas.configure(scrollregion=buttonCanvas.bbox("all")))
    buttonCanvas.create_window((0,0), window=buttonFrame, anchor = 'nw')
    buttonCanvas.configure(yscrollcommand=scroll.set)
    
    count = 0
    num= 0
    servers = getServers(data['dirs'])
    for d in servers:
        dlbl = tkinter.StringVar(value=data['dirs'][count])
        listdirL = tkinter.Label(buttonFrame, textvariable = dlbl, bg = foreground, fg=background, width= 33) # label is made to categorize by dir instead of just dumping everything out at once.
        if listdirL.cget('text') == '.':
            dlbl.set("Javier  |  " +  os.getcwd())
        listdirL.grid(column = 0, row = num, columnspan= 2, sticky=tkinter.W+tkinter.E)
        num+=1
        for i in range(0, len(servers[count])):
            launchButton = tkinter.Button(buttonFrame, text=servers[count][i], width = 32, height=1, command = lambda i=i, d=d, count=count : confirmUpdate(servers[count][i], RAM, selectStr, customs, count, javaOverride), bg=background, fg=foreground, bd=2)
            launchButton.grid(column = 1, row = num)
            serverDirButton = tkinter.Button(buttonFrame, text = '>', width=1, height = 1, bg = background, fg = foreground, command = lambda i = data['dirs'][count], e = servers[count][i]: openExplorer(i + "/" + e))
            serverDirButton.grid(column = 0, row = num)
            
            num+=1
        count += 1
    newdirButton = tkinter.Button(buttonFrame, text="Add a Directory. . .", width = 33, height = 1, command= lambda : addDir(gui), bg=foreground, fg=background, bd=2)  # persistant button at the bottom to add a DIR.
    newdirButton.grid(column = 0, row = num, columnspan= 2, sticky=tkinter.W+tkinter.E)

    buttonContainer.pack()
    buttonCanvas.pack(side = 'left', fill = 'both')
    scroll.pack(side = 'right',fill = 'y')

    ## stuff in the ramFrame


    RAM = tkinter.Entry(ramFrame, bd =2,width = 3, bg=background, fg=foreground)  # cute ram entry
    RAM.place(x=4, y=4)
    label = tkinter.Label(ramFrame, text="< < < Enter RAM", height = 0, bg=background, fg= foreground)
    label.place(x=27, y=4)

    SettingsButton = tkinter.Button(ramFrame, bd = 1, width = 10, bg=background, fg= "#9999FF", text="Settings", command= lambda : conformWindow(gui)) # the button that makes javier pop in and out his jacket.
    SettingsButton.place(x=46, y=34)

    aboutButton = tkinter.Button(ramFrame, bd=1, width = 4, bg=background, fg = "#FF9999", text = 'FAQ', command = aboutWindow)  # button to open the FAQ on javiers github.
    aboutButton.place(x=4, y=34)


    selectStr = tkinter.StringVar(value="Start: None")
    confirmBut = tkinter.Button(ramFrame, textvariable = selectStr, width = 17, height =3, command = lambda :  javierLaunch(selectStr, RAM, gui, safeStr, customs, guiStr, dire, javaOverride), bd=1, bg=background, fg=foreground)
    confirmBut.place(x=127, y=4)


    ### Directory opener ig

    dirMenu = tkinter.Frame(settingsFrame, bg = background)
    dirButtonContainer = tkinter.Frame(dirMenu, bg = background, height = 72, width = 230)
    dirButtonCanvas = tkinter.Canvas(dirButtonContainer, bg = background, height = 72, width = 230)
    dirScroll = tkinter.Scrollbar(dirButtonContainer, orient="vertical", command = dirButtonCanvas.yview, bg= '#40444B')
    dirButtonFrame = tkinter.Frame(dirButtonCanvas)

    dirButtonFrame.bind("<Configure>",lambda e: dirButtonCanvas.configure(scrollregion=dirButtonCanvas.bbox("all")))
    dirButtonCanvas.create_window((0,0), window = dirButtonFrame, anchor="nw")
    dirButtonCanvas.configure(yscrollcommand = dirScroll.set)
    dirButtonContainer.pack(side="bottom")
    dirButtonCanvas.pack(side="left", fill="both")
    dirScroll.pack(side="right", fill='y')

    for direct in data["dirs"]:
        if direct == '.':
            direct = os.getcwd()
        dirButton=tkinter.Button(dirButtonFrame, text=direct, bg=background, fg=foreground, width = 35, command = lambda : openExplorer(direct))
        dirButton.pack()
    NewDir= tkinter.Button(dirButtonFrame, text="Add a Directory. . . ?", width = 35, height = 1, command= lambda : addDir(gui), bg=foreground, fg=background, bd=2)
    NewDir.pack()

    dirLabel = tkinter.Label(dirMenu, width=35, text="Open a Directory", bg=background, fg=foreground)
    dirLabel.pack(side="top")
    dirMenu.place(x=0, y=0)


    ## Buttons in settings and similar things.

    def browse4Java(javaOverride):
        javapath = filedialog.askopenfile(master = gui, initialdir=".", title= "Select a Java Runtime Executable", filetypes=[("Java Runtime Executable", ("java.exe"))])
        if javapath != None:
            data["java"]=javapath.name
            dump(data)
            javaOverride.delete(0, "end")
            javaOverride.insert(0, javapath.name)
    
    def browse4jar(jarOverride, selectStr):
        serverStr = selectStr.get()[7:]
        jarpath = filedialog.askopenfilename(master=gui, initialdir=f"{data['dirs'][dire]}/{serverStr}", title = "Select a server JAR", filetypes=[("Java Archive file",(".jar"))])
        jarpath = path.basename(jarpath)
        data['servers'][serverStr][2]=jarpath
        dump(data)
        jarOverride.delete(0, "end")
        jarOverride.insert(0, jarpath)


    advancel = tkinter.Label(settingsFrame, text = "_______________________________________________\nADVANCED", width =35, bg=background, fg=foreground)
    advancel.place(x=0, y=208)
    serverselectdiscl = tkinter.Label(settingsFrame, text="Please select a server!", bd= 2, bg=background, fg=foreground)
    serverselectdiscl.place(x=65, y=260)


    javaOverride = tkinter.Entry(settingsFrame, bd=2, width=30, bg=background, fg= foreground)
    javaOverride.insert(0, data["java"])
    javaOverride.place(x=0, y=300)

    javaButton = tkinter.Button(settingsFrame, command = lambda: browse4Java(javaOverride), bd=2, height = 1, width = 9, text="Browse...", bg= background, fg=foreground)
    javaButton.place(x=180, y=298)

    global javaLabel
    javaLabel = tkinter.Label(settingsFrame, text="Java Override", bd=2, width =35, bg=background, fg=foreground)
    javaLabel.place(x=0, y=280)
    
    global jarLabel
    jarLabel = tkinter.Label(settingsFrame, text= "Jar File Override", bd= 2, width = 35, bg=background, fg=foreground)
    jarLabel.place(x=0, y=238)
    
    
    global jarOverride 
    jarOverride = tkinter.Entry(settingsFrame, bd=2, width=30, bg=background, fg=foreground)  # these being global is due to how much of a PAIN they're going to be.

    global jarButton 
    jarButton = tkinter.Button(settingsFrame, command = lambda: browse4jar(jarOverride, selectStr),bd=2, width = 9, text = "Browse...", bg= background, fg = foreground)  # i do generally try to stay away from global variables as they make things a bit messy, but due to the nature of how i want to do these I don't see a much cleaner way


    safebuttondesc = tkinter.Label(settingsFrame, text = "Only runs Vanilla Jar", width = 17, bg= background, fg=foreground)
    safebuttondesc.place(x=127, y=142)

    safeStr = tkinter.StringVar(value='Safemode: OFF')
    safeButton = tkinter.Button(settingsFrame, command = lambda: safeTog(safeStr), bd=2, height = 1, width = 16, textvariable = safeStr, bg = background, fg = foreground)
    safeButton.place(x=127, y=119)

    
    guidesc = tkinter.Label(settingsFrame, text = "Toggles JAR GUI", bg=background, fg=foreground, width=17)
    guidesc.place(x=127, y=197)

    guiStr = tkinter.StringVar(value='GUI: OFF')
    guiTogButton = tkinter.Button(settingsFrame, command = lambda: guiTog(guiStr), bd=2, height = 1, width = 16, textvariable = guiStr, bg = background, fg = foreground)
    guiTogButton.place(x=127, y=171)

    optionsL = tkinter.Label(settingsFrame, text = "Options", bg=background, fg=foreground, width=17)
    optionsL.place(x=127, y=98)


    customsl = tkinter.Label(settingsFrame, text = "Java Runtime Args", bg=background, fg=foreground, width=35, height=1)
    customs = tkinter.Entry(settingsFrame, width=41, bg = background, fg = foreground, bd=2)
    customsl.place(x=0, y=322)
    customs.place(x=0, y=343)

    ### CHECK FOR THIS WHILE CRTL+Z, if this goes away YOU'VE OFFICIALLY GONE TOO FAR!!!


    ### Themes


    ThemeMenu = tkinter.Frame(settingsFrame)
    themeButtonContainer = tkinter.Frame(ThemeMenu,height = 100, width = 105)
    themeButtonCanvas = tkinter.Canvas(themeButtonContainer, height = 100, width = 105)
    themeScroll = tkinter.Scrollbar(themeButtonContainer, orient='vertical', command = themeButtonCanvas.yview)
    themeButtonFrame = tkinter.Frame(themeButtonCanvas,)


    themeButtonFrame.bind("<Configure>",lambda e: themeButtonCanvas.configure(scrollregion=themeButtonCanvas.bbox("all")))
    themeButtonCanvas.create_window((0,0), window=themeButtonFrame, anchor = 'nw')

    themeButtonCanvas.configure(yscrollcommand=themeScroll.set)

    themeButtonContainer.pack(side="bottom")

    themeButtonCanvas.pack(side = 'left', fill = 'both')
    themeScroll.pack(side = 'right',fill = 'y')

    for theme in data["themes"]:
        themeButton = tkinter.Button(themeButtonFrame, text= (list(data["themes"].keys())[list(data["themes"].values()).index(data["themes"][theme])])   , width = 15, height=1, command = lambda theme=theme : ThemeChange((list(data["themes"].keys())[list(data["themes"].values()).index(data["themes"][theme])]), gui), bg=data["themes"][theme][1], fg=data["themes"][theme][0], bd=2, )
        themeButton.pack()
    createThemeButton = tkinter.Button(themeButtonFrame, text = "Create your own. . . ", command = lambda: themeMaker(), bd=2, bg= foreground, fg= background)
    createThemeButton.pack()

    themeLabel = tkinter.Label(ThemeMenu, width= 17, text = "Themes", bg = background, fg =foreground)
    themeLabel.pack(side='top')

    ThemeMenu.place(x=0, y=98)


    gui.mainloop()



## actual script.


#print(os.path.isfile(f"{path.dirname(__file__)}/;Javier Settings;/icons/Javier.ico"))
dire = None
data = getdata()
runGUI()

