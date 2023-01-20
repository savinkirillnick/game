from class_gui import *


class Controller:
    def __init__(self):
        # Задаем ширину окна в тайлах
        self.width = 16
        # Задаем высоту окна в тайлах
        self.height = 9
        # Задаем ширину тайлов в пикселях
        self.tile = 24
        # Для того чтобы наш Gui видел настройки, передаем ссылку на контроллер в класс Gui
        self.gui = Gui(self)

    def run(self):
        while 1:
            self.gui.update()
