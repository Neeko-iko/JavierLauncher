import tkinter
import time
import os
import zipfile
import json
## The launch function

def confirmUpdate(server):
    selectStr.set(f"Start: {server}")

def javierLaunch():
    if selectStr.get() == "Start: None":
        print("please select a server")
        return
    else:
        server = selectStr.get()
        server = server[7:]
    ## Code to grab the RAM value from everything available
    print(server)
    maxRAM = RAM.get()
    gui.withdraw()
    if maxRAM == '' or not maxRAM.isdigit():
        if not maxRAM.isdigit():
            print("RAM value wasn't entered properly reverting to JSON...")
        try:

            maxRAM = data[server]
        except KeyError:
            maxRAM = 'p'
            while not maxRAM.isdigit():
                maxRAM = input("Ram was not entered, or not found in the JSON, please enter a ram amount to save to the JSON file.")
                data[server] = int(maxRAM)
    else:
        data[server] = int(maxRAM)
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
    jsonfile.write("{}")
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
gui.title("Javier")

ramFrame = tkinter.Frame(gui, height = 60, width = 250, bg = 'black')
ramFrame.pack()

buttonContainer = tkinter.Frame(gui, bg= 'black',height = 60, width = 250)
buttonCanvas = tkinter.Canvas(buttonContainer, bg= 'black', height = 300, width = 225)
scroll = tkinter.Scrollbar(buttonContainer, orient='vertical', command = buttonCanvas.yview, bg= 'black')
buttonFrame = tkinter.Frame(buttonCanvas, bg= 'black')

buttonFrame.bind("<Configure>",lambda e: buttonCanvas.configure(scrollregion=buttonCanvas.bbox("all")))
buttonCanvas.create_window((0,0), window=buttonFrame, anchor = 'nw')

buttonCanvas.configure(yscrollcommand=scroll.set)




gui.minsize(250, 350)
gui.configure(bg = 'black')
gui.maxsize(250, 350)

for i in range(0, len(servers)):
    launchButton = tkinter.Button(buttonFrame, text=servers[i], width = 35, height=1, command = lambda i=i : confirmUpdate(servers[i]), bg = 'light grey', bd=2, )
    launchButton.pack()
    #launchButton.place(x = 0, y= 25*i + 50)

RAM = tkinter.Entry(ramFrame, bd =2,width = 3, bg = 'light grey')
RAM.place(x=7, y=14)
label = tkinter.Label(ramFrame, text="< < < Enter RAM")
label.place(x=30, y=14)

buttonContainer.pack()
buttonCanvas.pack(side = 'left', fill = 'both')
scroll.pack(side = 'right', fill = 'y')

selectStr = tkinter.StringVar(value="Start: None")
confirmBut = tkinter.Button(ramFrame, textvariable = selectStr, width = 16, height =2, command = javierLaunch)
confirmBut.place(x=135, y=5)

gui.mainloop()