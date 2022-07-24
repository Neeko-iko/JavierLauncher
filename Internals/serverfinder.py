import os
def folders(dir = os.getcwd()):
    servers = []
    if dir == "test": # testing garbage because i didn't want to constantly delete it. won't make proper folders, will be deleted later.
        for i in range(0,30):
            servers.append(i)
    else:
        """gets all folders that have a .jar file in it from passed in directory.\n if nothing is passed, will check CWD"""
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