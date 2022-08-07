# Javier
Javier is a minecraft server launcher that is intended for those who have multiple servers in a folder, but only run 1 at a time

If you only have 1 server, and need a quick and easy server launcher that applies to (hopefully) everything, then you should swap over to the old but still useful [Javier LITE](https://github.com/Neeko-iko/JavierLauncher/tree/LITE) which is maintained by [Jumpy](https://www.github.com/jumpyvonvagabond) in her free time.
if you want a working build of Javier that has features, check out the [GUI](https://github.com/Neeko-iko/JavierLauncher/tree/GUI) branch


Thank you for your continued support.


# Libraries/Modules and Tools Used
Tools
 - Mainly developed with Python 3.10 on ~~Debian~~ Manjaro
 - Using VSCode for Code editing
 - Using QTDesigner for designing the UI

Libraries/Modules
 - SQLite3 for the db and subsequent settings
 - QT for the GUI (PySide6)
 - shiboken6 for some quirky code (PySide6)
 - requests for the auto-updater and server creator
 - OS for finding servers
 - subproccess for launching everything
 - threading for Javier to launch multiple everythings
 - zipfile for finding the right file



not really a lib or mod but Xterm is used for launching the servers consoles' on Linux
figured that should be said somehwere


# FAQ
> is Qter Javier available as a windows executable file?

not at the moment. if you want to run it, you'll have to install QT (PySide6 is the package im using) on your local machine and run Javier.py from your terminal (or by double clicking, how fancy)
i'll make a Windows~~, MacOS,~~ and Linux executable when it's capable of doing anything proper. 

> Why not just continue the old (GUI) build?

Tkinter, which is what the GUI build uses, is fine as a starter, but using it now is tiresome and the way i've structured it is so insanely terrible that it would genuinely be more efficient to restart.  Assuming i even keep up with the project.

> Why is progress slow?

Pessimism to the project causes me to not want to work on it, followed by burnout from working a software engineering job.

> What are these .JSS files?

The way Javier handles themes now is essentially through CSS, but the way I have them set to be handled is dumb.  so I made my own filetype!



# THANKS
[@J-umpy](https://www.github.com/jumpyvonvagabond) - - - - say kind words to her on [Twitter](https://twitter.com/J_umpy)
 - Handling the DB 
 - Handling the AutoUpdater (TBA)
 - Legality 

|

[@zaisayshi](https://twitter.com/zaisayshi) - - - - [Zai's Ko-Fi](https://ko-fi.com/zaisayshi)
 - Creation of the new Javier logo
 


