"""bunch of server related functions, from grabbing servercount to starting servers"""
import os
import subprocess
from zipfile import ZipFile
import tarfile
import requests
import asyncio
from PySide6.QtCore import Signal, QObject
from Internals import jdb
jdb.deploy()

#Signal Emitters for the progress bar
#They must be defined outside of a function
class ProgEmitter(QObject):
  progUpdate = Signal(int)
progger = ProgEmitter()
class FinishEmitter(QObject):
  javaDownloadFinish = Signal(bool)
jf = FinishEmitter()

def dlJava(ver):
    operating = os.name
    operating = "windows" if operating == "nt" else "linux"
    ft = ".zip" if os.name == "nt" else ".tar.gz"
    fp = "./Internals/javas/java"
    header = {"User-Agent": "QterJavier"}
    #print(f"https://api.adoptium.net/v3/binary/latest/{ver}/ga/{operating}/x64/jre/hotspot/normal/eclipse")
    #print(java.status_code) # their api site says 307 is good but 200 is fairly universal.
    java = requests.request(method="get",url=f"https://api.adoptium.net/v3/binary/latest/{ver}/ga/{operating}/x64/jre/hotspot/normal/eclipse",headers=header,stream=True)
    print("Status Code: ", java.status_code)
    jdb.jsize = int(java.headers.get('content-length', 0))
    print("Size: ", jdb.jsize)
    jdb.jready = 1
    if java.status_code == 307 or java.status_code == 200:
        progress = 0
        with open(fp+ver+ft,"wb+") as e:
            for bite in java.iter_content(chunk_size=4048):
                progress = progress + len(bite)
                progger.progUpdate.emit(progress)
                e.write(bite)
    #os.mkdir(fp+ver)
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
    jf.javaDownloadFinish.emit(1)
    jdb.jfin = 1
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

def runServer(server, dire, RAM, gui):
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
    universe = f"{dire}/{server}/"
    if jdb.readServerValue(server, "JavaFilePath") != None:
        java = jdb.readServerValue(server,"JavaFilePath")
    elif jdb.readSettingValue("DefaultJava") != '':
        java = jdb.readSettingValue("DefaultJava")
    else:
        java = "java"
    if len(java.split(" ")) > 1:
        java = f"'{java}'"
    if os.name == "nt":
        cmd = (f"start cmd /k {java} -Xmx{RAM}G -Xms256M -jar '{jar}' nogui") #not happy about this.
        subprocess.run((java, "-Xms256M", f"-Xmx{RAM}G", '-jar', jar, gui), cwd=universe) # i wanted it to use the CMD. not the jar gui
            #cmd = (f"{java}", f"-Xmx{RAM}G", "-Xms256M", "-jar", jar, "nogui")  # why doesn't it work!!
            #subprocess.Popen((cmd), shell=True, cwd=universe, creationflags=subprocess.CREATE_NEW_CONSOLE
    else:      #xterm -e    # MacOS hates this.  will have to determine a workaround for Mac, eventually.
        cmd = (f"xterm -e '{java}' -Xmx{RAM}G -Xms256M -jar '{jar}' {gui}")
        subprocess.run((cmd), shell=True, cwd=universe)