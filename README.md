# Javier
Javier is a minecraft server launcher that is intended for those who have multiple servers in a folder, but only run 1 at a time

If you only have 1 server, and need a quick and easy server launcher that applies to (hopefully) everything, then you should swap over to the old but still useful [Javier LITE](https://github.com/Neeko-iko/JavierLauncher/tree/LITE) which is maintained by [Jumpy](https://www.github.com/jumpyvonvagabond) in her free time.


Thank you for your continued support.


# Libraries/Modules Used
All of the libraries/modules used are open source and included with the python installer at [Pythons official website](https://python.org)

 - tkinter for the GUI
 - os for filepathing and almost literally everything else 
 - json for the json (crazy i know)
 - zipfile for accessing the jar files
 - time for server restart



# FAQ
> is Javier available as a windows executable file?

yes, its available [on the 1.9.0 release of Javier](https://github.com/Neeko-iko/JavierLauncher/releases/tag/1.9.0), which should be the last python release for a while.  I (Neeko) may do a few bugfixes if they ever come in. but don't expect many updates past 1.9.0.  Thank you for your continued support.

> Do I have to enter the RAM value each time I launch a server?
 
No, that's only to update the JSON incase you want to decrease or increase the RAM for the server.
 
 
> Javier crashes upon launch!

Did you rename the JSON Javier pulls from?  Did you clear the JSON to be empty?  Does Javier have any server folders to see?

  
  
  
> I wanna make my own theme!

Glad to hear it! you can make as many themes as you want in the JSON just use the following format
  
  "Name of theme":["text color in hex", "background color in hex"]
  
  example: 
  ` "Light": ["#161719","#FFFFFF"]`
  
  
  
  
> Javier doesn't change themes when I click the buttons!

  Javier has to be restarted for the theme change to take affect. 

> What is Javier's Safemode button?

 Javier's Safemode is meant for modded servers.  when ON it will actively avoid any modded JAR files and only run the base minecraft jar file.  useful for testing if mods are breaking the world, or if the world file is simply corrupted (at least that's what i've been told.)   - using this on a vanilla server will net no changes.  it will run like normal.

> Why is there a toggle for a "GUI"???

that's for the MC server GUI, its defaulted to OFF as that saves CPU and probably some RAM, but it shows extra stats, so for those who would like to see those extra statistics, they now can  (defualted to off *per launch*)

> what's a launch flag?

Launch flags are something that the .jar checks for to run different options, this can increase or decrease performance on the server.  Find the flags that are right with your server to make it as efficient as possible!

> What's the dot doing in my directories???

that's just what the python file is seeing.  if you remove it Javier will no longer look for whatever folder *he* is in, only elsewhere.

> What are the ">" buttons next to all my servers?

They're open folder buttons, they allow you to open up the server folder for easy access to the folders.  It's especially useful if you use Javier as a shortcut.
