import tkinter
import time
import os
import zipfile
import json
## The launch function
toggle = True


def ThemeChange(theme):
    data["curTheme"] = theme
    print(data["curTheme"])
    jsonfile = open("./Javier.json", 'w')
    json.dump(data, jsonfile, indent = 4)
    jsonfile.close()

def aboutWindow():
    import webbrowser
    webbrowser.open_new("https://github.com/Neeko-iko/JavierLauncher#javier")
    del webbrowser
def conformWindow():
    global toggle
    global gui
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

def confirmUpdate(server):
    global RAM
    selectStr.set(f"Start: {server}")
    try:
        RAM.delete(0)
        RAM.insert(0,data['servers'][server])
    except KeyError:
        print("No Ram found insert it using the box if you may.")




def javierLaunch():
    #print(data)
    if selectStr.get() == "Start: None":
        print("please select a server")
        return
    else:
        server = selectStr.get()
        server = server[7:]
    ## Code to grab the RAM value from everything available
    print(server)
    maxRAM = RAM.get()
    if maxRAM == '' or not maxRAM.isdigit():
        if not maxRAM.isdigit():
            print("RAM value wasn't entered properly reverting to JSON...")
        try:

            maxRAM = data['servers'][server]
        except KeyError:
            maxRAM = 'p'
            while not maxRAM.isdigit():
                maxRAM = input("Ram was not entered, or not found in the JSON, please enter a ram amount to save to the JSON file.")
                data['servers'][server] = int(maxRAM)
    else:
        data['servers'][server] = int(maxRAM)
    jsonfile = open("./Javier.json", 'w')
    json.dump(data, jsonfile, indent = 4)
    jsonfile.close()
    ## Code to find the right JAR file to launch
    file = None
    if file == None:
        files = []
        for item in os.listdir(f"./{server}"):
            if item[-4:] == '.jar':
                files.append(item)
        if len(files) > 1:
            for item in files:
                print(item)
                manafestcheck = zipfile.ZipFile(f"./{server}/{item}",'r')
                test = manafestcheck.open('META-INF/MANIFEST.MF','r')
                garbagecheck = test.readlines()
                for line in garbagecheck:
                    if 'net.minecraft.server.MinecraftServer' in str(line):
                        files.remove(item)
        file = files[0]
    ## Actual launch code.
    customs = 'nogui'  ### Make sure to seperate customs with a space.
    back = os.getcwd()
    gui.destroy()
    while True:
        os.chdir(f"./{server}")
        os.system(f"java -Xmx{maxRAM}G -Xms256M -jar {file} {customs}")

        os.chdir(back)
        print("\n\nit seems as though the server has crashed or was stopped forcibly.\n\n\n\nrestarting the server in 10 seconds...")
        for i in range (10, 0, -1):
            print(str(i) + " seconds remaning\n\n\n")
            time.sleep(1)
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
## Finding every subfolder in the folder its in. 
servers = os.listdir('.')
for item in servers:
    if os.path.isfile(item):
        servers.remove(item)
servers.remove(os.path.basename(__file__))
## GUI code
gui = tkinter.Tk()
gui.title("Javier - MCSL")


JavierFrame = tkinter.Frame(gui, height =360, width = 250, bg = '#40444B')
JavierFrame.grid(row=0, column = 0)

#(gui, height = 364, width = 250, bg = '#40444B')
settingsFrame = tkinter.Frame(gui, bg = '#40444B')
settingsFrame.grid(row=0, column = 1, ipadx=48, ipady=170)

ramFrame = tkinter.Frame(JavierFrame, height = 60, width = 250, bg = '#40444B')
ramFrame.pack()

buttonContainer = tkinter.Frame(JavierFrame, bg= '#40444B',height = 60, width = 255)
buttonCanvas = tkinter.Canvas(buttonContainer, bg= '#40444B', height = 300, width = 229)
scroll = tkinter.Scrollbar(buttonContainer, orient='vertical', command = buttonCanvas.yview, bg= '#40444B')
buttonFrame = tkinter.Frame(buttonCanvas, bg= '#40444B')

buttonFrame.bind("<Configure>",lambda e: buttonCanvas.configure(scrollregion=buttonCanvas.bbox("all")))
buttonCanvas.create_window((0,0), window=buttonFrame, anchor = 'nw')

buttonCanvas.configure(yscrollcommand=scroll.set)




gui.minsize(250, 363)
gui.configure(bg = 'white')
gui.maxsize(250, 363)

for i in range(0, len(servers)):
    launchButton = tkinter.Button(buttonFrame, text=servers[i], width = 32, height=1, command = lambda i=i : confirmUpdate(servers[i]), bg=data["themes"][data["curTheme"]][1], fg=data["themes"][data["curTheme"]][0], bd=2, )
    launchButton.pack()

background = data["themes"][data["curTheme"]][1]
foreground = data["themes"][data["curTheme"]][0]


RAM = tkinter.Entry(ramFrame, bd =2,width = 3, bg=background, fg=foreground)
RAM.place(x=4, y=4)
label = tkinter.Label(ramFrame, text="< < < Enter RAM", height = 0, bg='#40444B', fg= "#FFFFFF")
label.place(x=27, y=4)

SettingsButton = tkinter.Button(ramFrame, bd = 1, width = 10, bg=background, fg= "#9999FF", text="Settings", command= conformWindow)
SettingsButton.place(x=46, y=34)

aboutButton = tkinter.Button(ramFrame, bd=1, width = 4, bg=background, fg = "#FF9999", text = 'FAQ', command = aboutWindow)
aboutButton.place(x=4, y=34)

buttonContainer.pack()
buttonCanvas.pack(side = 'left', fill = 'both')
scroll.pack(side = 'right',fill = 'y')


selectStr = tkinter.StringVar(value="Start: None")
confirmBut = tkinter.Button(ramFrame, textvariable = selectStr, width = 17, height =3, command = javierLaunch, bd=1, bg=data["themes"][data["curTheme"]][1], fg= data["themes"][data["curTheme"]][0])
confirmBut.place(x=127, y=4)

### settings lmao

settingsFrame = tkinter.Frame(gui, bg = '#40444B')

## padding ipadx=48, ipady=170
settingsFrame.grid(row=0, column = 1, ipadx=78, ipady= 132)

themeButtonContainer = tkinter.Frame(settingsFrame, bg= '#40444B',height = 75, width = 75)
themeButtonCanvas = tkinter.Canvas(themeButtonContainer, bg= '#40444B', height = 75, width = 75)
themeScroll = tkinter.Scrollbar(themeButtonContainer, orient='vertical', command = themeButtonCanvas.yview, bg= '#40444B')
themeButtonFrame = tkinter.Frame(themeButtonCanvas, bg= '#40444B')


themeButtonFrame.bind("<Configure>",lambda e: themeButtonCanvas.configure(scrollregion=themeButtonCanvas.bbox("all")))
themeButtonCanvas.create_window((0,0), window=themeButtonFrame, anchor = 'nw')

themeButtonCanvas.configure(yscrollcommand=themeScroll.set)

themeButtonContainer.grid(row=1, column = 0)
themeButtonCanvas.pack(side = 'left', fill = 'both')
themeScroll.pack(side = 'right',fill = 'y')

for theme in data["themes"]:
    themeButton = tkinter.Button(themeButtonFrame, text= (list(data["themes"].keys())[list(data["themes"].values()).index(data["themes"][theme])])   , width = 10, height=1, command = lambda theme=theme : ThemeChange((list(data["themes"].keys())[list(data["themes"].values()).index(data["themes"][theme])])), bg=data["themes"][theme][1], fg=data["themes"][theme][0], bd=2, )
    themeButton.pack()


themeLabel = tkinter.Label(settingsFrame, width= 13, text = "Themes", bg = background, fg =foreground)
themeLabel.grid(row=0, column = 0)

gui.mainloop()
