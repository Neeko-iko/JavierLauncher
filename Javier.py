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
    else:
        server = selectStr.get()
        server = server[7:]

    ## Code to grab the RAM value from everything available
    gui.withdraw()
    print(server)
    maxRAM = RAM.get()
    if maxRAM == '':
        try:

            maxRAM = data[server]
        except KeyError:
            maxRAM = 'p'
            while not maxRAM.isdigit():
                maxRAM = input("Ram was not entered, nor found in the JSON, please enter a ram amount to save to the JSON file.")
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
servers.remove("Javier.py")

## GUI code

gui = tkinter.Tk()
gui.title("Javier")
gui.minsize(250, len(servers)*30)
gui.configure(bg='black')

for i in range(0, len(servers)):
    launchButton = tkinter.Button(gui, text=servers[i], width = 35, height=1, command = lambda i=i : confirmUpdate(servers[i]), bg = 'light grey', bd=2)
    launchButton.pack()
    launchButton.place(x = 0, y= 30*i + 50)

RAM = tkinter.Entry(gui, bd =2)
RAM.place(x=0, y=14)
label = tkinter.Label(gui, text="< < < Enter RAM")
label.place(x=30, y=14)


selectStr = tkinter.StringVar(value="Start: None")
confirmBut = tkinter.Button(gui, textvariable = selectStr, width = 16, height =2, command = javierLaunch)
confirmBut.place(x=135, y=5)

gui.mainloop()
