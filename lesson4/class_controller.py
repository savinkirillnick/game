from class_gui import *
from class_player import *
import json


class Controller:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.width = 16
        self.height = 9
        self.tile = 24
        self.player = Player()

        with open("data/level.json") as file:
            self.level = json.load(file)
            self.player.x = self.level['start_position']['x']
            self.player.y = self.level['start_position']['y']

        self.gui = Gui(self)

    def run(self):
        # Задаем начальные значения сторон движения равные False
        move_left = move_right = move_up = move_down = False

        while 1:
            self.clock.tick(60)

            for e in pygame.event.get():
                # Общая логика такая:
                # Если нажата клавиша, и она является одной из списка:
                # То необходимая сторона движения меняется на True

                if e.type == pygame.KEYDOWN and e.key in [pygame.K_LEFT,
                                                          pygame.K_a]:
                    move_left = True
                if e.type == pygame.KEYDOWN and e.key in [pygame.K_RIGHT,
                                                          pygame.K_d]:
                    move_right = True
                if e.type == pygame.KEYDOWN and e.key in [pygame.K_UP,
                                                          pygame.K_w]:
                    move_up = True
                if e.type == pygame.KEYDOWN and e.key in [pygame.K_DOWN,
                                                          pygame.K_s]:
                    move_down = True
                # Логика так же:
                # Если клавиша отжата, и она является одной из списка:
                # То необходимая сторона движения меняется на False
                if e.type == pygame.KEYUP and e.key in [pygame.K_LEFT,
                                                        pygame.K_a]:
                    move_left = False
                if e.type == pygame.KEYUP and e.key in [pygame.K_RIGHT,
                                                        pygame.K_d]:
                    move_right = False
                if e.type == pygame.KEYUP and e.key in [pygame.K_UP,
                                                        pygame.K_w]:
                    move_up = False
                if e.type == pygame.KEYUP and e.key in [pygame.K_DOWN,
                                                        pygame.K_s]:
                    move_down = False

                if e.type == pygame.QUIT:
                    exit()

            # в теле цикла проводим передвижение персонажа
            self.player.move(move_left=move_left, move_right=move_right, move_up=move_up, move_down=move_down)
            # а после выводим на экран
            self.gui.update()
