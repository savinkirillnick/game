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

        move_left = move_right = move_up = move_down = move_jump = False

        while 1:
            self.clock.tick(60)

            for e in pygame.event.get():
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
                # Если нажата клавиша пробел, то выполняется прыжок
                if e.type == pygame.KEYDOWN and e.key in [pygame.K_SPACE]:
                    move_jump = True

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
                # Если отжата клавиша пробел, то выполняется прыжок
                if e.type == pygame.KEYUP and e.key in [pygame.K_SPACE]:
                    move_jump = False

                if e.type == pygame.QUIT:
                    exit()

            # Передаем состояние прыжка в класс игрока
            self.player.move(move_left=move_left, move_right=move_right, move_up=move_up, move_down=move_down, move_jump=move_jump)
            self.gui.update()
