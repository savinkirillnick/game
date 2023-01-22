from class_gui import *
from class_player import *
import json


class Controller:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.width = 16
        self.height = 9
        self.tile = 24
        self.player = Player(self)
        self.gui = Gui(self)
        self.back_tiles = []
        self.front_tiles = []
        self.level = dict()
        self.load_level()

    def get_hud(self):
        arr = list()
        arr.append([10, 10, "x: "+str(self.player.sprite.rect.x)])
        arr.append([10, 20, "y: "+str(self.player.sprite.rect.y)])
        arr.append([10, 30, "fps: "+str(self.clock.get_fps()//1)])
        return arr

    # Функция загрузки уровня
    def load_level(self):
        # открываем файл настройки уровня для чтения и считываем нужные переменные
        with open("data/level.json") as file:
            self.level = json.load(file)
            self.player.x = self.level['start_position']['x']
            self.player.y = self.level['start_position']['y']
            # создаем список тайлов, куда предзагрузим все тайлы уровня
            self.back_tiles = []
            # Предзагрузка тайлов бэкграунда
            for y in range(len(self.level['back'])):
                # тут мы делаем двойной массив
                self.back_tiles.append([])
                for x in range(len(self.level['back'][y])):
                    # пробегаемся по всей сетке уровня и считываем номер тайла из заданной ячейки и по номеру тайла получаем его местоположение
                    img = self.level['tiles'][self.level['back'][y][x]]
                    # теперь img - это ссылка на файл
                    if not img:
                        # если стоял 0, то мы получим в ссылку False
                        # тогда ничего не подгружаем и пропускаем итерацию.
                        self.back_tiles[y].append(False)
                        continue
                    # вычисляем координаты установки тайла по координатам сетки
                    coord_x = x * self.tile
                    coord_y = y * self.tile
                    # создаем спрайт, присваиваем ему картинку из img и размещаем в виде прямоугольника по заданным координатам
                    tile_sprite = pygame.sprite.Sprite()
                    tile_sprite.image = pygame.image.load(img)
                    tile_sprite.rect = pygame.Rect(
                        coord_x,
                        coord_y,
                        self.tile,
                        self.tile
                    )
                    # далее записываем загруженный тайл в список
                    self.back_tiles[y].append(tile_sprite)

            self.front_tiles = []
            # Предзагрузка тайлов фронтграунда
            for y in range(len(self.level['front'])):
                # тут мы делаем двойной массив
                self.front_tiles.append([])
                for x in range(len(self.level['front'][y])):
                    # пробегаемся по всей сетке уровня и считываем номер тайла из заданной ячейки и по номеру тайла получаем его местоположение
                    img = self.level['tiles'][self.level['front'][y][x]]
                    # теперь img - это ссылка на файл
                    if not img:
                        # если стоял 0, то мы получим в ссылку False
                        # тогда ничего не подгружаем и пропускаем итерацию.
                        self.front_tiles[y].append(False)
                        continue
                    # вычисляем координаты установки тайла по координатам сетки
                    coord_x = x * self.tile
                    coord_y = y * self.tile
                    # создаем спрайт, присваиваем ему картинку из img и размещаем в виде прямоугольника по заданным координатам
                    tile_sprite = pygame.sprite.Sprite()
                    tile_sprite.image = pygame.image.load(img)
                    tile_sprite.rect = pygame.Rect(
                        coord_x,
                        coord_y,
                        self.tile,
                        self.tile
                    )
                    # далее записываем загруженный тайл в список
                    self.front_tiles[y].append(tile_sprite)

    def collisions_obstacles(self, dx, dy):
        c1 = max(self.player.x // self.tile - 1, 0)
        c2 = min((self.player.x + self.player.width) // self.tile + 1, len(self.level['obstacles'][0]) - 1)

        r1 = max((self.player.y + self.player.height - self.player.step) // self.tile - 1, 0)
        r2 = min((self.player.y + self.player.height) // self.tile + 1, len(self.level['obstacles']) - 1)

        for y in range(r1, r2 + 1):
            for x in range(c1, c2 + 1):
                if self.level['obstacles'][y][x] == 0:
                    continue

                left = x * self.tile
                top = y * self.tile

                tile_sprite = pygame.sprite.Sprite()
                tile_sprite.rect = pygame.Rect(left, top, self.tile, self.tile)
                player_sprite = pygame.sprite.Sprite()
                player_sprite.rect = pygame.Rect(self.player.x, self.player.y + self.player.height - self.player.step,
                                                 self.player.width, self.player.step)

                if pygame.sprite.collide_rect(player_sprite, tile_sprite):
                    if dx > 0:
                        self.player.x = left - self.player.width
                    if dx < 0:
                        self.player.x = left + self.tile
                    if dy > 0:
                        self.player.y = top - self.player.height
                    if dy < 0:
                        self.player.y = top + self.tile - self.player.height + self.player.step

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
