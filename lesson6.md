# Урок 6 – Текстурирование
Сейчас мы будем накладывать текстуры на наши спрайты.

Но перед тем как  начать, необходимо разобраться, где и как мы их собираемся хранить.

Перестроим немного файлы хранения информации и классы обработки и вывода действий на экран.

Первым делом наложим текстуры на игрока. Нарисуем спрайт игрока `player.png` и поместим его в папку `/data/images/player/`.
У меня получился спрайт 32х48 пикселей.

![Игрок](/lesson6/data/images/player/player.png)

Для хранения текстур и информации об игроке, создадим файл `/data/player.json`, где пропишем все основные параметры графики персонажа.

Создаем и редактируем `/data/player.json`:

    {
      "player": "data/images/player/player.png",
      "width": 32,
      "height": 48,
      "step": 16
    }

Теперь перепишем класс `Player` и осуществим загрузку игрока из файла.

    import json

    ...
        # Создадим хранилице данных в виде словаря
        self.player_data = dict()
        with open("data/player.json") as file:
            self.player_data = json.load(file)
        # теперь назначение характеристик спрайта берем из словаря
        self.width = self.player_data['width']
        self.height = self.player_data['height']
        self.step = self.player_data['step']

Там же в функции `__init__` класса `Player` наложем текстуру на наш спрайт игрока

        ...
        self.sprite.image = pygame.image.load(self.player_data['player'])
        
Теперь немного перерисуем уровень. Сделаем еще пару стен, колонны и изменим стартовую позицию. Чтобы игрок не застревал в стене:

Редактируем файл `/data/level.json`.

    {
      "start_position": {
        "x": 100,
        "y": 50
      },
      "obstacles": [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      ]
    }

Теперь наша игра выглядит гораздо интереснее:

![Результат](/images/6-0-1.jpg)

Далее, для текстурирования уровня необходимо нарисовать несколько текстур. Пол, стены, потолок и т.д.

Для корректного вывода текстур, разобьем графику уровня на слои:
- задний слой
- активный слой (слой игрока и npc и интерактивных предметов)
- передний слой
- слой hud (самый верхний слой, на котором выводится интерфейс игры)
- позже можно добавить псевдо-3d слой.

Псевдо-3d слой будет просчитывать перекрытие спрайтов в зависимости от расположения по оси `y` на карте.

Я нарисовал несколько спрайтов стен, пола и потолка, и закинул их в папку `/data/images/level_1/`. Все спрайты разметом 24х24. Но рисовать можно любые, просто они будут ложиться по сетке 24х24.

![Картинка](/lesson6/data/images/level_1/tile_1.png)
![Картинка](/lesson6/data/images/level_1/wall_1.png)
![Картинка](/lesson6/data/images/level_1/wall_2.png)
![Картинка](/lesson6/data/images/level_1/wall_3.png)
![Картинка](/lesson6/data/images/level_1/wall_4.png)
![Картинка](/lesson6/data/images/level_1/wall_5.png)
![Картинка](/lesson6/data/images/level_1/wall_6.png)
![Картинка](/lesson6/data/images/level_1/wall_7.png)
![Картинка](/lesson6/data/images/level_1/wall_8.png)
![Картинка](/lesson6/data/images/level_1/wall_9.png)
![Картинка](/lesson6/data/images/level_1/wall_10.png)
![Картинка](/lesson6/data/images/level_1/wall_11.png)
![Картинка](/lesson6/data/images/level_1/wall_12.png)
![Картинка](/lesson6/data/images/level_1/wall_13.png)

После того, как скопировали картинки в свою папку, надо в файле `level.json` описать их:
Пишем:

    {
      ...
      "tiles": [
        false,
        "data/images/level_1/tile_1.png",
        "data/images/level_1/wall_1.png",
        "data/images/level_1/wall_2.png",
        "data/images/level_1/wall_3.png",
        "data/images/level_1/wall_4.png",
        "data/images/level_1/wall_5.png",
        "data/images/level_1/wall_6.png",
        "data/images/level_1/wall_7.png",
        "data/images/level_1/wall_8.png",
        "data/images/level_1/wall_9.png",
        "data/images/level_1/wall_10.png",
        "data/images/level_1/wall_11.png",
        "data/images/level_1/wall_12.png",
        "data/images/level_1/wall_13.png"
      ],
     ...
    }

Тайл с индексом 0 мы оставим пустым, так как им мы будем обозначать отсутствие текстуры для переднего плана.

Теперь в файле `level.json` создаем дополнительные слои.

Слой с препятствиями мы оставим, так как по нему будет вестись расчет столкновений, поэтому копируем его и вставляем под другим именем `back`.

Редактируем `level.json`:

    ...
      "back": [
        [2,12,12,14,13,12, 2,13, 9, 9,10,10, 9, 9,12, 2],
        [6, 9, 9, 9,10, 9, 6, 9, 1, 1, 1, 1, 1, 1, 9, 6],
        [2, 1, 1, 1, 1, 1,12, 1, 1, 1, 1, 1, 1, 1, 1, 8],
        [2, 1, 1, 1, 1, 1,11, 1, 1,14, 1, 1,11, 1, 1, 8],
        [6, 1, 1, 1, 1, 1, 1, 1, 1,13, 1, 1,12, 1, 1, 6],
        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6],
        [2, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6],
        [2, 2, 6, 7, 8, 2, 2, 2, 1, 1, 1, 1, 1, 1, 7, 3],
        [3, 3, 3, 5, 3, 5, 5, 5, 3, 2, 8, 2, 2, 2, 2, 4]
      ]
    ...
    }

Теперь когда задний план готов, перепишем функцию загрузки уровня.

В классе `Controller` в функции `__init__` удалим блок кода начинающийся с `with open()...` и перенесем его в отдельную функцию:

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

Теперь проведем предзагрузку уровня, в `__init__` допишем 

    def __init__(self):
        ...
        self.load_level()

В классе `Gui` сделаем отрисовку заднего фона.

Удаляем все, что написано в теле циклов `for y ... for x ...` и пишем следующее:

    def update(self):
        self.screen.blit(self.background, (0, 0))

        # Рисуем задний фон
        for y in range(len(self.controller.level['back'])):
            for x in range(len(self.controller.level['back'][y])):
                # берем предзагруженный тайл из списка
                tile_sprite = self.controller.back_tiles[y][x]
                # если он пустой, то пропускаем итерацию
                if not tile_sprite:
                    continue
                # выводим тайл на экран
                self.screen.blit(tile_sprite.image, (tile_sprite.rect.x, tile_sprite.rect.y))
        
        # Рисуем активный слой
        self.screen.blit(self.controller.player.sprite.image, (self.controller.player.sprite.rect.x, self.controller.player.sprite.rect.y))

        pygame.display.update()

Если запустить игру, получим прорисованный уровень:

![Результат](/images/6-0-2.jpg)

Теперь добавим передний слой - который будет лежать поверх персонажа.

Копируем слой с препятствиями и вставляем его как `front`.

Редактируем `level.json`

      "front": [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 6, 2, 7, 2, 0, 8, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 2, 2, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      ],

Проводим предзагрузку аналогично слоя `back`:

Редактируем `load_level(self)`

    def load_level(self):
        ...
        with open("data/level.json") as file:
            ...
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

В классе `Gui` делаем вывод переднего плана на экран после вывода игрока

        # Рисуем активный слой
        self.screen.blit(...)

        # Рисуем передний фон аналогично слою back
        for y in range(len(self.controller.level['front'])):
            for x in range(len(self.controller.level['front'][y])):
                tile_sprite = self.controller.front_tiles[y][x]
                if not tile_sprite:
                    continue
                self.screen.blit(tile_sprite.image, (tile_sprite.rect.x, tile_sprite.rect.y))

        pygame.display.update()

При запуске получим более живую картинку. Теперь игрок может прятаться за выступами

![Результат](/images/6-0-3.jpg)

---

### Работа над ошибками

В классе `Controller`, в функции `__init__`, перед тем как вызвать метод `self.load_level()` необходимо объявить еще переменные для хранения уровня и тайлов:

        ...
        self.back_tiles = []
        self.front_tiles = []
        self.level = dict()
        self.load_level()
