# Урок 5 – Обработка столкновений со стенами.
В этом уроке научимся обрабатывать столкновения с препятствиями.



Столкновения у нас будет обрабатывать контроллер. Для этого в классе `Controller` пишем функцию, которая принимает движения игрока:

    def collisions_obstacles(self, dx, dy):

Чтобы не проверять все стены на уровне, определяем соседние клетки, которые граничат с нашим игроком:
Верхний ряд, нижний ряд, левый столбец, правый столбец

        # начальный и конечный столбец
        # сразу проверяем, что начальный столбец не отрицательный, а конечный столбец не больше, чем размер уровня
        c1 = max(self.player.x // self.tile - 1, 0)
        c2 = min((self.player.x + self.player.width) // self.tile + 1, len(self.level['obstacles'][0]) - 1)
        
        # начальная и конечная строка
        # аналогично проверяем строки
        r1 = max((self.player.y + self.player.height) // self.tile - 1, 0)
        r2 = min((self.player.y + self.player.height) // self.tile + 1, len(self.level['obstacles']) - 1)

Теперь пробегаем по диапазонам строк и столбцов

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
                
Проверяем пересечения двух прямоугольников

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

Функция написана. Вызывать ее будем из функции `move` класса `Player`.

В то время, как происходит присвоение координат игрока по рассчитанным движениям, мы будем проверять столкновения:

Так, как нам нужно вызывать ее из контроллера, то нам нужно в класс `Player` передать объект класса `Controller`.

Для этого в классе `Controller` передаем самого-себя как объект в объект `self.player`:
    
    def __init__(self):
        ...
        # Изменяем создание игрока
        self.player = Player(self)

А в классе `Player` прописывааем:

    def __init__(self, controller):
        self.controller = controller
        ...

Теперь можно оформить вызов функции обработки столкновений из контроллера:
дописываем в функцию `move`:
        
        ...
        self.x += self.dx
        # Сначала проверяем столкновения по оси x
        self.controller.collisions_obstacles(self.dx, 0)
        self.sprite.rect.x = self.x

        self.y += self.dy
        # потом проверяем столкновения по оси y
        self.controller.collisions_obstacles(0, self.dy)
        self.sprite.rect.y = self.y + self.z
        ...

Если запустить `main.py`, то игрок сможет ходить по экрану и врезаться в препятствия

---

# Урок 5.1 – Отделяем ноги
Можно было бы оставить и так, но по причине того, что персонаж не плоский как паук, а высокий, то с учетом перспективы отображения, спрайт персонажа может пересекать спрайт стены на величину тела. Тем самым обработка столкновений будет проводиться по ногам.

В классе `Player` создадим высоту для ног

    class Player:
        def __init__(self, controller):
            self.step = 16
            ...

Теперь внесем поправки в функции расчета столкновений класса `Controller`, чтобы расчет шел не от головы игрока, а от ног:

    def collisions_obstacles(self, dx, dy):
        ...
        r1 = max((self.player.y + self.player.height - self.player.step) // self.tile - 1, 0)
        ...
        for y ...
            for x ...
                player_sprite.rect = pygame.Rect(self.player.x, self.player.y + self.player.height - self.player.step,
                                                 self.player.width, self.player.height)
                ...
                if pygame.sprite.collide_rect ...
                    if dy < 0:
                        self.player.y = top + self.tile - self.player.height + self.player.step

Теперь если запустить `main.py` все должно заработать в приятной глазу картинке.

---

### Работа над ошибками

Если заметили, то когда мы рисуем спрайт игрока и сравниваем его со спрайтом стены, то высоту надо задавать уже по высоте ног, а не полной высоты игрока:

    player_sprite.rect = pygame.Rect(self.player.x, self.player.y + self.player.height - self.player.step,
                                     self.player.width, self.player.step)
                