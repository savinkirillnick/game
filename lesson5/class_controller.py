from class_gui import *
from class_player import *
import json


class Controller:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.width = 16
        self.height = 9
        self.tile = 24
        # Изменяем создание игрока
        self.player = Player(self)

        with open("data/level.json") as file:
            self.level = json.load(file)
            self.player.x = self.level['start_position']['x']
            self.player.y = self.level['start_position']['y']

        self.gui = Gui(self)

    def collisions_obstacles(self, dx, dy):
        # начальный и конечный столбец
        # сразу проверяем, что начальный столбец не отрицательный, а конечный столбец не больше, чем размер уровня
        c1 = max(self.player.x // self.tile - 1, 0)
        c2 = min((self.player.x + self.player.width) // self.tile + 1, len(self.level['obstacles'][0]) - 1)

        # начальная и конечная строка
        # аналогично проверяем строки
        r1 = max(self.player.y // self.tile - 1, 0)
        r2 = min((self.player.y + self.player.height) // self.tile + 1, len(self.level['obstacles']) - 1)

        for y in range(r1, r2 + 1):
            for x in range(c1, c2 + 1):
                # Если на карте по конкретным координатам стоит 0, т.е. препятствие отсутствует, то пропускаем итерацию
                if self.level['obstacles'][y][x] == 0:
                    continue

                # Если там стоит препятствие (или единица), проводим следующие расчеты
                # Столкновения будем высчитывать внутренними методами pygame:
                # Будем рисовать два прямоугольника - прямоугольник стены и прямоугольник игрока
                # и будем проверять их перекрытие

                # Определяем начальные координаты стены (координаты верхнего левого угла)
                left = x * self.tile
                top = y * self.tile

                # создаем спрайт стены по данным координатам в виде прямоугоника с размерами тайла
                tile_sprite = pygame.sprite.Sprite()
                tile_sprite.rect = pygame.Rect(left, top, self.tile, self.tile)
                # создаем спрайт персонажа по координатам игрока в виде прямоугольника с размерами игрока
                player_sprite = pygame.sprite.Sprite()
                player_sprite.rect = pygame.Rect(self.player.x, self.player.y,
                                                 self.player.width, self.player.height)

                if pygame.sprite.collide_rect(player_sprite, tile_sprite):
                    # Если пересечение с препятствием произошло, проверям в какую сторону мы шли,
                    # чтобы в противоположную отпрыгнуть
                    if dx > 0:
                        # Если шли вправо, то координата x игрока будет на ширину игрока левее, чем тайл стены
                        self.player.x = left - self.player.width
                    if dx < 0:
                        # Если шли влево, то координата x игрока будет на ширину тайла стены правее
                        self.player.x = left + self.tile
                    if dy > 0:
                        # Если шли вниз, то координата y игрока будет на высоту игрока выше, чем тайл стены
                        self.player.y = top - self.player.height
                    if dy < 0:
                        # Если шли вверх, то координата y игрока будет на высоту тайла стены ниже
                        self.player.y = top + self.tile


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
                if e.type == pygame.KEYUP and e.key in [pygame.K_SPACE]:
                    move_jump = False

                if e.type == pygame.QUIT:
                    exit()

            self.player.move(move_left=move_left, move_right=move_right, move_up=move_up, move_down=move_down, move_jump=move_jump)
            self.gui.update()
