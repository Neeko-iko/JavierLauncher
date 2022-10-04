"""bunch of server related functions, from grabbing servercount to starting servers"""
import os
import subprocess
from zipfile import ZipFile
import tarfile
import requests
from PySide6.QtCore import Signal, QObject, QThread
from Internals import jdb
import threading
jdb.deploy()



def start(cmd, universe): # used for linux launch but maybe will be useful later :)
    subprocess.run((cmd), shell=True, cwd=universe)


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
    try:
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
    except FileNotFoundError:
        jf.javaDownloadFinish.emit(1)
        jdb.jfin = 1
        return
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

class ServerThread(QThread):
  def __init__(self):
    super().__init__()
    self.server = ''
    self.dire = ''
    self.RAM = 0
    self.gui = ''
  def run(self):
    if self.dire == ".":
        self.dire = os.getcwd()
    t = str(jdb.readServerValue(self.server, "JARName"))
    print(os.path.isfile(t))
    if os.path.isfile(t):
        jar = jdb.readServerValue(self.server, "JARName")
    else:
        self.dire = self.dire.replace("\\", "/") 
        file =[]
        for item in os.listdir(f"{self.dire}/{self.server}"):
            if item[-4:] == '.jar':
                file.append(item)
        if len(file) > 1:
            for item in file:
                check = ZipFile(f"{self.dire}/{self.server}/{item}",'r')
                check = check.open('META-INF/MANIFEST.MF','r')
                check = check.readlines()
                for line in check:
                    if 'net.minecraft.server.MinecraftServer' in str(line):
                            file.remove(item)
        jar = f"\"{self.dire}/{self.server}/{file[0]}\""
        jdb.updateServerValue(self.server, "JARName", jar)
    
    universe = f"{self.dire}/{self.server}/"
    javaS = str(jdb.readServerValue(self.server, "JavaFilePath"))
    javaD = str(jdb.readSettingValue("DefaultJava"))
    if os.path.isfile(javaS) :
        java = javaS
    elif  os.path.isfile(javaD):
        java = javaD
    else:
        java = "java"
    jraS = jdb.readServerValue(self.server, "LaunchFlags")
    jraD = jdb.readSettingValue("DefaultJRA")
    if jraS != None and jraS != '':
        jra = jraS
    elif jraD != None and jraD != '':
        jra = jraD
    else:
        jra = ''
    if len(java.split(" ")) > 1:
        java = f"\"{java}\""
    print(jar)
    if os.name == "nt":
        print("Jar Path: ", jar)
        print("Java Path: ", java)
        cmd = (f"{java} -Xmx{self.RAM}G -Xms256M {jra} -jar {jar} {self.gui}")
        if self.gui == "nogui":
            cmd = "start cmd /k " + cmd
        subprocess.run(cmd, shell=True, cwd=universe) # i wanted it to use the CMD. not the jar gui
            #cmd = (f"{java}", f"-Xmx{RAM}G", "-Xms256M", "-jar", jar, "nogui")  # why doesn't it work!!
            #subprocess.Popen((cmd), shell=True, cwd=universe, creationflags=subprocess.CREATE_NEW_CONSOLE
    else:      #xterm -e    # MacOS hates this.  will have to determine a workaround for Mac, eventually.
        cmd = (f"{java} -Xmx{self.RAM}G -Xms256M {jra} -jar {jar} {self.gui}")
        if self.gui == "nogui":
            cmd = f"""xterm -T 'Minecraft server "{self.server}"' -e """ + cmd
        print(cmd)
        a = threading.Thread(target = start, args = (cmd,universe))
        a.start()
        #subprocess.run((cmd), shell=True, cwd=universe)
  def setProp(self, server, dire, RAM, gui):
    self.server = server
    self.dire = dire
    self.RAM = RAM
    self.gui = gui
