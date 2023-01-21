# Урок 3 – Игрок.
Для хранения настроек игрока обработки событий создадим отдельный класс.

Для этого создадим файл `class_player.py` и запишем в него следующее:


    import pygame

    
    class Player:
        def __init__(self):
            # Задаем координаты, по которым стоит персонаж
            self.x = 0
            self.y = 0
            # Задаем размер тайла героя
            self.width = 40
            self.height = 48
            # Создаем спрайт персонажа
            self.sprite = pygame.sprite.Sprite()
            # Создаем квадратик размерами тайла персонажа
            self.sprite.image = pygame.Surface((self.width, self.height))
            # Задаем цвет тайла
            self.sprite.image.fill(pygame.Color("#00FF19"))

Отлично! Персонажа создали, теперь выводим его на экран:

Для начала в файле `class_controller.py` импортируем класс игрока:

    from class_player import *
    ...

Далее при инициализации контроллера создаем объект класса игрока

    def __init__(self):
        ...
        # Создаем в контроллере объект класса игрока, 
        # потому как именно контроллер отслеживает игрока 
        # и его действия
        self.player = Player()

В файле `class_gui.py` запишем вывод персонажа в функции `update`:

        ...
        # Рисуем персонажа по его координатам
        self.screen.blit(self.controller.player.sprite.image, (self.controller.player.x, self.controller.player.y))

        pygame.display.update()

Если запустить `main.py` мы получим белый экран с синими стенами по периметру и зеленым прямоугольников в левом верхнем углу - это и есть наш игрок.

---

# Урок 3.1 – Располагаем игрока по стартовым координатам уровня.

Так как у каждого уровня могут быть свои настройки стартовой позиции, то давайте будем задавать ее в файле настроек уровня.
Редуктируем файл `/data/level.json`:

    {
      "start_position": {
        "x": 150,
        "y": 150
      },
      "obstacles": [...]
    }

Чтобы применить позицию на игроке, в классе `Controller`, при загрузке уровня прописываем новые координаты игроку:

        with open("data/level.json") as file:
            self.level = json.load(file)
            # ставим игрока в стартовую позицию уровня
            self.player.x = self.level['start_position']['x']
            self.player.y = self.level['start_position']['x']

---

### Работа над ошибками

В коде приведена ошибка в самом конце урока. Для позиционирования по координате `y` необходимо прописывать:

`self.player.y = self.level['start_position']['y']`