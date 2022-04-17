from http import server
from Internals import serverfinder, settingsconfig
import gi
gi.require_version("Gtk", "3.0")  # this is for GTK. 
from gi.repository import Gtk as gtk

class mainwindow(gtk.Window):
    def __init__(self):
        super().__init__(title = "JavierGTK")

        #settingbutton = gtk.Button(label = "open settings") will work on this stuff L8R NERDS!!!!!!!
        #settingbutton.connect("clicked", self.opensettings)
        #self.add(settingbutton)
        listof = gtk.ListBox()
        listof.set_selection_mode(gtk.SelectionMode.NONE)
        #items = gtk.ListBoxRow()

        serverlist = serverfinder.folders()
        if serverlist == []:
            emptylabel = gtk.Label(label = "Javier found no servers!")
            listof.add(emptylabel)
        else:
            for servers in serverlist:
                serverbutton = gtk.Button(label = servers)
                listof.add(serverbutton)

        #listof.add(items)
        self.add(listof)

    def opensettings(self, item):
       win = settingsconfig.settingswindow()
       win.show_all()


window = mainwindow()
window.show_all()
window.connect("destroy", gtk.main_quit)
gtk.main()