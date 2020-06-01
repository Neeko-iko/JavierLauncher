# Javier
Javier is a minecraft server launcher that is intended for those who have multiple servers in a folder, but only run 1 at a time

If you only have 1 server, and need a quick and easy server launcher that applies to (hopefully) everything, then you should swap over to the old but still useful [master branch](https://github.com/Neeko-iko/JavierLauncher/tree/master) which is maintained by [Jumpy](https://www.github.com/jumpyvonvagabond) in her free time.

thank



# FAQ

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

> what's a launch flag?

Launch flags are something that the .jar checks for to run different options, this can increase or decrease performance on the server.  Find the flags that are right with your server to make it as efficient as possible!
