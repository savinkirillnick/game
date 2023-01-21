import pygame


class Player:
    def __init__(self):
        # Скорость движения игрока
        self.speed = 3
        # Движение по горизонтальной оси x
        self.dx = 0
        # Движение по вертикальной оси y
        self.dy = 0
        self.x = 0
        self.y = 0
        self.width = 40
        self.height = 48
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface((self.width, self.height))
        self.sprite.image.fill(pygame.Color("#00FF19"))

    def move(self, move_left, move_right, move_up, move_down):

        # Обрабатываем горизонтальное движение по оси x
        # Общая логика такая:
        # Если игрок получает сторону движения равной True,
        # то мы меняем его значение dx или dy (изменения координаты) равной значению скорости
        # значение устанавливается положительное, если движемся по оси в сторону увеличения координат
        # значение отрицательное, если движемся, если движемся по оси в сторону уменьшения координат

        # если мы получаем False для обеих сторон движения по оси, то обнуляем значение изменения координат
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

        self.x += self.dx
        self.y += self.dy
