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
