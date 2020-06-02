import time
import os
import zipfile
import json

#Checks if RAM has been set in JSON
def setRAM(maxRAM = ''):
    while True:
        try:
            int(maxRAM)
        except:
            maxRAM = input("Please enter the amount of ram you'd like to dedicate to your Minecraft Server:\n")
        else:
            break
    data['ram'] = maxRAM
    dump()

def dump():
    with open('javier.json', 'w') as f:
        json.dump(data, f)
if os.path.exists('javier.json'):           #Checks for a javier.json
    with open('javier.json') as f:          #Loads if one is found
        data = json.loads(f.read())
else:
    data = {'ram': 1, 'flags': '', 'path': '.', 'dir': False}          #Creates one with default values if one isn't found
    dump()
while True:
    choice = input("\nWhat would you like to do?\n1) Launch the Server\n2) Launch the Server in Safe Mode\n3) Change the amount of dedicated RAM\n4) Use custom filepath to server\n5) Add launch flags\n\n")
    if choice == '1' or choice == '2':
        files = []
        if os.path.isdir(data['path']):
            for item in os.listdir(data['path']):
                if item[-4:] == '.jar':
                    files.append(item)
            if len(files) > 1:
                for item in files:
                    check = zipfile.ZipFile(item,'r')
                    check = check.open('META-INF/MANIFEST.MF','r')
                    check = check.readlines()
                    for line in check:
                        if 'net.minecraft.server.MinecraftServer' in str(line):            #Searches for the Server's .jar file
                            if choice == '2':           #If Safe Mode is selected
                                files = item            #The server is launched
                                break
                            else:                       #Otheriwse the Server is removed from the list of jar files
                                files.remove(item)
                del check
        if len(files) == 0:
            files = data['path']
        else:
            files = files[0]
        if data['dir'] == True:
            if os.path.isfile(data['path']):
                path = os.path.dirname(os.path.abspath(data['path']))
                os.chdir(path)
            else:
                os.chdir(data['path'])
        break
    elif choice == '3':
        setRAM()
    elif choice == '4':
        while True:
            path = input('Please enter the location of your server.jar\n')
            if os.path.exists(path):
                data['path'] = path
                data['dir'] = True
                dump()
                break
    elif choice == '5':
        data['flags'] = input(f'Your current launch flags are:\n{data["flags"]}\nPlease enter what you would like to overwrite them with\n')
    else:
        print("\n\nInvalid input\n")
del choice
while True:
    os.system(f"java -Xmx{data['ram']}G -Xms256M {data['flags']} -jar {files} nogui")
    print("\n\nit seems as though the server has crashed or was stopped forcibly.\n\n\n\nRestarting the server in 3 seconds...")
    for i in range (3, 0, -1):
        print(str(i) + " seconds remaning\n\n\n")
        time.sleep(1)
