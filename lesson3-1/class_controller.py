from class_gui import *
from class_player import *
import json


class Controller:
    def __init__(self):
        self.width = 16
        self.height = 9
        self.tile = 24

        # Создаем в контроллере объект класса игрока, потому как именно контроллер отслеживает игрока и его действия
        self.player = Player()

        with open("data/level.json") as file:
            self.level = json.load(file)
            # ставим игрока в стартовую позицию уровня
            self.player.x = self.level['start_position']['x']
            self.player.y = self.level['start_position']['y']

        self.gui = Gui(self)

    def run(self):
        while 1:

            self.gui.update()
