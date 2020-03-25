import time
import os
import zipfile
maxRAM = None  ##This is in terms of GIGABYTES
if maxRAM == None:
    try:
        maxRAM = int(str(os.path.basename(__file__))[:-3])

    except ValueError:
        maxRAM = 'p'
        print("The File isn't named after the amount of gigs of ram you'd like")
        while(not maxRAM.isdigit()):
            maxRAM = input("please enter the amount of ram you'd like to dedicate to this.")
        os.rename(os.path.basename(__file__),str(maxRAM) + '.py')
        input('press anything to close this - re-open.')
        sys.exit()



file = None  # enter the JAR file here, make sure to put .jar at the end of it.
if file == None
    files = []
    for item in os.listdir():
        if item[-4:] == '.jar':
            files.append(item)
    if len(files) > 1:
        for item in files:
            manafestcheck = zipfile.ZipFile(item,'r')
            test = manafestcheck.open('META-INF/MANIFEST.MF','r')
            garbagecheck = test.readlines()
            for line in garbagecheck:
                if 'net.minecraft.server.MinecraftServer' in str(line):
                    files.remove(item)
    file = files[0]
customs = 'nogui'  ### Make sure to seperate customs with a space.
while True:
    os.system(f"java -Xmx{maxRAM}G -Xms256M -jar {file} {customs}")
    print("\n\nit seems as though the server has crashed or was stopped forcibly.\n\n\n\nrestarting the server in 10 seconds...")
    for i in range (10, 0, -1):
        print(str(i) + " seconds remaning\n\n\n")
        time.sleep(1)
