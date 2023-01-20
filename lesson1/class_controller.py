from class_gui import *


class Controller:
    def __init__(self):
        self.gui = Gui()

    def run(self):
        while 1:
            self.gui.update()
