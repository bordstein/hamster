#!/usr/bin/env python
from gi.repository import Gtk
import sys

class HamsterGui(object):
    def __init__(self):
        
        #Set the UI file
        builder = Gtk.Builder()
        builder.add_from_file("test.glade")
        
        #Get the Main Window, and connect the "destroy" event
        #self.window = self.wTree.get_widget("MainWindow")
        #if (self.window):
        #    self.window.connect("destroy", Gtk.main_quit)
        self.window = builder.get_object("MainWindow")
        self.cover = builder.get_object("cover")

        builder.connect_signals(self)      
        self.window.connect_after('destroy', self.destroy)
        self.cover.set_from_file("/home/nurio/Downloads/movie_cover.jpg")

        self.window.show_all()

    def destroy(window, self):
        Gtk.main_quit()

def main():
    gui = HamsterGui()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())
