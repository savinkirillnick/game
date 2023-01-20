import pygame


class Gui:
    def __init__(self):
        # Инициируем модуль
        pygame.init()
        # Задаем размеры окна
        pygame.display.set_mode(320, 240)

    def update(self):
        # Перехватываем события (нажатия клавиш)
        for e in pygame.event.get():
            # Если срабатывает событие закртытия окна, то выходим из игры
            if e.type == pygame.QUIT:
                exit()
        # Обновляем картинку
        pygame.display.update()
