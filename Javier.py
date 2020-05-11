import tkinter
import time
import os
import zipfile
import json


def javierLaunch(server):
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







    file = None  # enter the JAR file here, make sure to put .jar at the end of it.
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

servers = os.listdir('.')
for item in servers:
    if os.path.isfile(item):
        servers.remove(item)
servers.remove("Javier.py")
gui = tkinter.Tk()
gui.title("Javier")
gui.minsize(250, len(servers)*30)
gui.configure(bg='black')

for i in range(0, len(servers)):
    launchButton = tkinter.Button(gui, text=servers[i], width = 35, height=1, command = lambda i=i : javierLaunch(servers[i]), bg = 'white', bd=2)
    launchButton.pack()
    launchButton.place(x = 0, y= 30*i + 50)

RAM = tkinter.Entry(gui, bd =2)
RAM.place(x=0, y=10)
label = tkinter.Label(gui, text="< < < Enter RAM")
label.place(x=30, y=10)
gui.mainloop()