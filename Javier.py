import time
import os
import zipfile
def setRAM(maxRAM = ''):
    while True:
        try:
            int(maxRAM)
        except:
            maxRAM = input("Please enter the amount of ram you'd like to dedicate to your Minecraft Server:\n")
        else:
            break
    os.rename(os.path.basename(__file__),(f"Javier {str(maxRAM)}.py"))
    input('The program needs to be restarted for changes to take effect.\nPress enter to close.')
    raise SystemExit

try:
    maxRAM = int(str(os.path.basename(__file__))[6:-3])
except ValueError:
    setRAM()
else:
    while True:
        choice = input("\nWhat would you like to do?\n1) Run the Server\n2) Change the amount of dedicated RAM\n\n")
        if choice == '1':
            files = []
            for item in os.listdir():
                if item[-4:] == '.jar':
                    files.append(item)
            if len(files) > 1:
                for item in files:
                    check = zipfile.ZipFile(item,'r')
                    check = check.open('META-INF/MANIFEST.MF','r')
                    check = check.readlines()
                    for line in check:
                        if 'net.minecraft.server.MinecraftServer' in str(line):
                            files.remove(item)
                    del check
            break
        elif choice == '2':
            setRAM()
            break
        else:
            print("Invalid input")
    del choice
files = files[0]
while True:
    os.system(f"java -Xmx{maxRAM}G -Xms256M -jar {files} nogui")
    print("\n\nit seems as though the server has crashed or was stopped forcibly.\n\n\n\nRestarting the server in 3 seconds...")
    for i in range (3, 0, -1):
        print(str(i) + " seconds remaning\n\n\n")
        time.sleep(1)