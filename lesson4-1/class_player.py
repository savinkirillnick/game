import pygame


class Player:
    def __init__(self):
        self.speed = 3
        self.dx = 0
        self.dy = 0
        self.x = 0
        self.y = 0
        # Сила прыжка
        self.jump_power = 5
        # состояние нахождения на земле или в воздухе. Чтобы нельзя было сделать двойной прыжок (прыжок во время прыжка)
        self.onGround = False
        # нахождение игрока в координатах оси z
        self.z = 0
        # Изменение по оси z
        self.dz = 0
        # сила гравитации (при падении координата игрока по оси z меняется с заданной скоростью)
        self.g = 0.35
        self.width = 40
        self.height = 48
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface((self.width, self.height))
        self.sprite.image.fill(pygame.Color("#00FF19"))
        # Создаем прямоугольник, который мы будем видеть
        self.sprite.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, move_left, move_right, move_up, move_down, move_jump):

        if move_left:
            self.dx = self.speed
        if move_right:
            self.dx = -self.speed
        if not (move_left or move_right):
            self.dx = 0
        if move_up:
            self.dy = self.speed
        if move_down:
            self.dy = -self.speed
        if not (move_up or move_down):
            self.dy = 0

        # Первым делом проверяем в прыжке наш игрок или нет:
        if self.onGround and move_jump:
            # Ели игрок стоит на земле и выполняет прыжок, то изменение dz будет отрицательное и равным силе прыжка
            self.dz = -self.jump_power
        if not self.onGround:
            # Если игрок в воздухе, то его значение dz меняется на величину гравитации
            self.dz += self.g

        self.x += self.dx
        # Меняем отображение игрока по оси x
        self.sprite.rect.x = self.x

        self.y += self.dy
        # Так как у нас проекция с видом сверху, то изменение прыжка будет отражаться в координатах оси y
        self.sprite.rect.y = self.y + self.z

        # И не забываем обновить координату z
        self.z += self.dz
        # Проверяем, если она будет больше 0 (уровень пола),
        # то ставим флажок, что игрок стоит на полу, иначе оставляем его в состоянии прыжка
        if self.z >= 0:
            self.z = 0
            self.dz = 0
            self.onGround = True
        else:
            self.onGround = False
