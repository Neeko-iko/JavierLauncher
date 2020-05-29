import tkinter
import time
import os
import zipfile
import json
## The launch function
toggle = True



def safeTog(safeStr):
    safe = safeStr.get()[10:]
    if safe == "OFF":
        safeStr.set("Safemode: ON")
    else:
        safeStr.set("Safemode: OFF")
    return safeStr


def ThemeChange(theme, gui):
    global data
    data["curTheme"] = theme
    jsonfile = open("./Javier.json", 'w')
    json.dump(data, jsonfile, indent = 4)
    jsonfile.close()
    print("These changes will apply next time Javier is launched.")

def aboutWindow():
    import webbrowser
    webbrowser.open_new("https://github.com/Neeko-iko/JavierLauncher#FAQ")
    del webbrowser
def conformWindow(gui):
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

def confirmUpdate(server, RAM, selectStr, customs):

    def dataupdate():
        data['servers'][server] = ['', '']
        jsonfile = open("./Javier.json", 'w')
        json.dump(data, jsonfile, indent = 4)
        jsonfile.close()



        #awful check to see if the key is wrong, or if the index is incorrect.
    try:
        data['servers'][server][2]
    except KeyError:
        dataupdate()
    except IndexError:
        pass



    selectStr.set(f"Start: {server}")
    try:
        if data['servers'][server][0] != '':
            RAM.delete(0, "end")
            RAM.insert(0,data['servers'][server][0])
        else:
            print("No Ram found insert it using the box if you may.")
    except KeyError:
        print("No Ram found insert it using the box if you may.")
    try:
        if data['servers'][server][1] != '':
            customs.delete(0, "end")
            customs.insert(0, data['servers'][server][1])
    except KeyError:
        pass




def javierLaunch(selectStr, RAM, gui, safeStr, customs):
    # Reformat the JSON to properly work with seerver stuff ig idk this is a quick fix

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
    jsonfile = open("./Javier.json", 'w')
    json.dump(data, jsonfile, indent = 4)
    jsonfile.close()

    ## Code to find the right JAR file to launch
    file = []
    safe = safeStr.get()[10:]
    for item in os.listdir(f"./{server}"):
        if item[-4:] == '.jar':
            file.append(item)
    if len(file) > 1:
        for item in file:
            print(item)
            check = zipfile.ZipFile(f"./{server}/{item}",'r')
            check = check.open('META-INF/MANIFEST.MF','r')
            check = check.readlines()
            for line in check:
                if 'net.minecraft.server.MinecraftServer' in str(line):
                    if safe == "ON":
                        file = item
                        break
                    else:
                        file.remove(item)
    if safe != "ON":
        file = file[0]
    #del safe, check
    ## Actual launch code.
    back = os.getcwd()
    gui.destroy()
    while True:
        os.chdir(f"./{server}")
        os.system(f"java -Xmx{maxRAM}G -Xms256M {customs} -jar {file} nogui")

        os.chdir(back)
        print("\n\nit seems as though the server has crashed or was stopped forcibly.\n\n\n\nrestarting the server in 10 seconds...")
        for i in range (10, 0, -1):
            print(str(i) + " seconds remaning\n\n\n")
            time.sleep(1)
def getdata():
    ## Searching for the JSON file to pull RAM values from
    try:
        jsonfile = open("./Javier.json")
        data = json.load(jsonfile)
        jsonfile.close()
    except FileNotFoundError:
        jsonfile = open("./Javier.json", "w")
        jsonfile.write("""{"servers":{},"themes":{"Dark": ["#FFFFFF", "#36393F"],"HC": ["#FFFFFF", "#161719"],"Light": ["#161719", "#FFFFFF"]},"curTheme":"Dark"}""")
        jsonfile.close()
        jsonfile = open("./Javier.json")
        data = json.load(jsonfile)
        jsonfile.close()
    return data
def getServers():
    ## Finding every subfolder in the folder its in. 
    servers = os.listdir('.')
    for item in servers:
        if os.path.isfile(item):
            servers.remove(item)
    servers.remove(os.path.basename(__file__))
    return servers
## GUI code
def runGUI():

    gui = tkinter.Tk()
    gui.title("Javier - MCSL")

    background = data["themes"][data["curTheme"]][1]
    foreground = data["themes"][data["curTheme"]][0]


    JavierFrame = tkinter.Frame(gui, height =360, width = 250, bg = '#40444B')
    JavierFrame.grid(row=0, column = 0)

    #(gui, height = 364, width = 250, bg = '#40444B')
    settingsFrame = tkinter.Frame(gui,height =363, width = 250, bg = '#40444B')
    settingsFrame.grid(row=0, column = 1)

    ramFrame = tkinter.Frame(JavierFrame, height = 60, width = 250, bg = '#40444B')
    ramFrame.pack()

    buttonContainer = tkinter.Frame(JavierFrame, bg= '#40444B',height = 60, width = 255)
    buttonCanvas = tkinter.Canvas(buttonContainer, bg= '#40444B', height = 300, width = 229)
    scroll = tkinter.Scrollbar(buttonContainer, orient='vertical', command = buttonCanvas.yview, bg= '#40444B')
    buttonFrame = tkinter.Frame(buttonCanvas, bg= '#40444B')

    buttonFrame.bind("<Configure>",lambda e: buttonCanvas.configure(scrollregion=buttonCanvas.bbox("all")))
    buttonCanvas.create_window((0,0), window=buttonFrame, anchor = 'nw')

    buttonCanvas.configure(yscrollcommand=scroll.set)

    safeStr = tkinter.StringVar(value='Safemode: OFF')
    safeButton = tkinter.Button(settingsFrame, command = lambda: safeTog(safeStr), bd=2, height = 1, width = 12, textvariable = safeStr, bg = background, fg = foreground)
    safeButton.place(x=-1, y=297)


    customsFrame = tkinter.Frame(settingsFrame, bg=background)
    customsl = tkinter.Label(customsFrame, text = " ADVANCED: Launch Flags ", bg=background, fg=foreground)
    customs = tkinter.Entry(customsFrame, width=41, bg = background, fg = foreground, bd=2)
    customsl.pack()
    customs.pack()
    customsFrame.place(x=0, y=323)


    gui.minsize(250, 363)
    gui.configure(bg = 'white')
    gui.maxsize(250, 363)

    for i in range(0, len(servers)):
        launchButton = tkinter.Button(buttonFrame, text=servers[i], width = 32, height=1, command = lambda i=i : confirmUpdate(servers[i], RAM, selectStr, customs), bg=background, fg=foreground, bd=2)
        launchButton.pack()

    RAM = tkinter.Entry(ramFrame, bd =2,width = 3, bg=background, fg=foreground)
    RAM.place(x=4, y=4)
    label = tkinter.Label(ramFrame, text="< < < Enter RAM", height = 0, bg='#40444B', fg= "#FFFFFF")
    label.place(x=27, y=4)

    SettingsButton = tkinter.Button(ramFrame, bd = 1, width = 10, bg=background, fg= "#9999FF", text="Settings", command= lambda : conformWindow(gui))
    SettingsButton.place(x=46, y=34)

    aboutButton = tkinter.Button(ramFrame, bd=1, width = 4, bg=background, fg = "#FF9999", text = 'FAQ', command = aboutWindow)
    aboutButton.place(x=4, y=34)

    buttonContainer.pack()
    buttonCanvas.pack(side = 'left', fill = 'both')
    scroll.pack(side = 'right',fill = 'y')


    selectStr = tkinter.StringVar(value="Start: None")
    confirmBut = tkinter.Button(ramFrame, textvariable = selectStr, width = 17, height =3, command = lambda :  javierLaunch(selectStr, RAM, gui, safeStr, customs), bd=1, bg=background, fg=foreground)
    confirmBut.place(x=127, y=4)

    ### settings and stuff


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


data = getdata()
servers = getServers()
runGUI()