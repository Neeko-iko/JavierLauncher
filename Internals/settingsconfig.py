import gi
gi.require_version("Gtk", "3.0")  # this is for GTK. 
from gi.repository import Gtk as gtk


class settingswindow(gtk.Window):
    def __init__(self):
        super().__init__(title = "settings")

        self.settingbutton = gtk.Button(label = "open settings")
        self.settingbutton.connect("clicked", self.dothing)
        self.add(self.settingbutton)