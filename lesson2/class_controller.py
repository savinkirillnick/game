from class_gui import *
import json


class Controller:
    def __init__(self):
        self.width = 16
        self.height = 9
        self.tile = 24

        # читаем файл уровня
        with open("data/level.json") as file:
            self.level = json.load(file)

        self.gui = Gui(self)

    def run(self):
        while 1:
            self.gui.update()
