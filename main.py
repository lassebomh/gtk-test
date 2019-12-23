
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="GNOME Button", application=app)
        self.set_default_size(250, 50)

        button = Gtk.Button()
        button.set_label("Tryk på knappen!!!")
        button.connect("clicked", self.do_clicked)
        self.add(button)



    def do_clicked(self, button):
        print("You clicked me!")


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)