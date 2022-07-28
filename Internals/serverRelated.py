"""bunch of server related functions, from grabbing servercount to starting servers"""
import os
import subprocess
import zipfile
def folders(dir = os.getcwd()):
    """gets all folders that have a .jar file in it from passed in directory.\n if nothing is passed, will check CWD"""
    servers = []
    dir = os.path.expanduser(dir)
    if dir[-1] != "/":
        dir = dir+"/"
    dir = dir.replace("\\", "/")
    files = os.listdir(dir)
    
    for folder in files:
        if os.path.isdir(dir+folder):
            complete = False
            for things in os.listdir(dir+folder):
                
                if ".jar" in things:
                    servers.append(folder)
                    complete = True
                if complete: break
        if ".jar" in folder:
            servers.append(dir)
    return servers

def runServer(server, dire, RAM):
    
    dire = dire.replace("\\", "/")
    file =[]
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
                        file.remove(item)
    jar = f"{dire}/{server}/{file[0]}"
    universe = f"{dire}/{server}"
    java = "java"
    operating = os.name
    print(operating)
    if operating == "nt":
        cmd = (f'start cmd /C {java} -Xmx{RAM}G -Xms256M -jar "{jar}" nogui')
        subprocess.run((cmd), shell=True, cwd=universe)
        #cmd = (f"{java}", f"-Xmx{RAM}G", "-Xms256M", "-jar", jar, "nogui")  # why doesn't it work!!
        #subprocess.Popen((cmd), shell=True, cwd=universe, creationflags=subprocess.CREATE_NEW_CONSOLE
    else:      #xterm -e    # MacOS hates this.  will have to determine a workaround for Mac, eventually.
        cmd = (f"xterm -e '{java}' -Xmx{RAM}G -Xms256M -jar '{jar}' nogui") # probably will have it limited to 1 server on mac :L
        subprocess.run((cmd), shell=True, cwd=universe)