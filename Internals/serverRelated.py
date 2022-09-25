"""bunch of server related functions, from grabbing servercount to starting servers"""
import os
import subprocess
from zipfile import ZipFile
import tarfile
import requests
from Internals import jdb
jdb.deploy()

def dlJava(ver, bar, but):
    operating = os.name
    operating = "windows" if operating == "nt" else "linux"
    ft = ".zip" if os.name == "nt" else ".tar.gz"
    fp = "./Internals/javas/java"
    header = {"User-Agent": "QterJavier"} # it can be anything! :)
    java = requests.request(method="get",url=f"https://api.adoptium.net/v3/binary/latest/{ver}/ga/{operating}/x64/jre/hotspot/normal/eclipse",headers=header,stream=True)
    #print(f"https://api.adoptium.net/v3/binary/latest/{ver}/ga/{operating}/x64/jre/hotspot/normal/eclipse")
    #print(java.status_code) # their api site says 307 is good but 200 is fairly universal.
    if java.status_code == 307 or java.status_code == 200:
        bar.setMaximum(int(java.headers.get('content-length', 0)))
        progress = 0
        with open(fp+ver+ft,"wb+") as e:
            for bite in java.iter_content(chunk_size=4048):
                progress = progress + len(bite)
                bar.setValue(progress)
                e.write(bite)
    else:
        bar.setMaximum(1)
        bar.setValue(0)
        bar.setEnabled(False)
        but.setEnabled(True)
        return
    #os.mkdir(fp+ver)
    bar.setMaximum(0)
    bar.setValue(0)
    if operating == "windows":
        file = ZipFile(fp+ver+ft, "r")
        ftr = file.namelist()[0] #hopefully this works lmoaoooo
        file.extractall(fp[:-4])
        file.close()
    else:
        file = tarfile.open(fp+ver+ft, "r")
        ftr = file.getnames()[0] #gotta love that all linux distros + mac will eat a tar.gz just fine
        file.extractall(fp[:-4])
        file.close()
    os.remove(fp+ver+ft) #cleanup
    os.rename(fp[:-4]+ftr, fp+ver) #so that it's an easier check.
    bar.setMaximum(1) # probably better ways to do this lmaooo
    bar.setEnabled(False)
    but.setEnabled(True)
    return
        



def folders(dir = os.getcwd()):
    """gets all folders that have a .jar file in it from passed in directory.\n if nothing is passed, will check CWD"""
    servers = []
    if dir == ".":
        dir == os.getcwd()
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
    t =jdb.readServerValue(server, "JARName") 
    if  t == '' or t == None:
        dire = dire.replace("\\", "/") 
        file =[]
        for item in os.listdir(f"{dire}/{server}"):
            if item[-4:] == '.jar':
                file.append(item)
        if len(file) > 1:
            for item in file:
                check = ZipFile(f"{dire}/{server}/{item}",'r')
                check = check.open('META-INF/MANIFEST.MF','r')
                check = check.readlines()
                for line in check:
                    if 'net.minecraft.server.MinecraftServer' in str(line):
                            file.remove(item)
        jar = f"{dire}/{server}/{file[0]}"
        jdb.updateServerValue(server, "JARName", jar)
    else:
        jar = jdb.readServerValue(server, "JARName")
    universe = f"{dire}/{server}"
    if jdb.readServerValue(server, "JavaFilePath") != None:
        java = jdb.readServerValue(server,"JavaFilePath")
    elif jdb.readSettingValue("DefaultJava") != None:
        java = jdb.readSettingValue("DefaultJava")
    else:
        java = "java"
    operating = os.name
    if operating == "nt":
        cmd = (f'start cmd /C {java} -Xmx{RAM}G -Xms256M -jar "{jar}" nogui')
        subprocess.run((cmd), shell=True, cwd=universe)
            #cmd = (f"{java}", f"-Xmx{RAM}G", "-Xms256M", "-jar", jar, "nogui")  # why doesn't it work!!
            #subprocess.Popen((cmd), shell=True, cwd=universe, creationflags=subprocess.CREATE_NEW_CONSOLE
    else:      #xterm -e    # MacOS hates this.  will have to determine a workaround for Mac, eventually.
        cmd = (f"xterm -e '{java}' -Xmx{RAM}G -Xms256M -jar '{jar}' nogui")
        subprocess.run((cmd), shell=True, cwd=universe)