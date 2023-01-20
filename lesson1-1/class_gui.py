import pygame


class Gui:
    def __init__(self, controller):
        pygame.init()
        self.controller = controller
        # Задаем размеры окна, которые берем из объекта класса Controller
        display = (controller.width * controller.tile, controller.height * controller.tile)
        # Создаем переменную screen нашего объекта Gui, чтобы в дальнейшем выводить в нее изображение
        self.screen = pygame.display.set_mode(display)

        # Записываем название игры
        pygame.display.set_caption("Last Android")

        # Заливаем задний фон белым цветом: Создаем прямоугольную поверхность под размер окна закрашиваем
        self.background = pygame.Surface(display)
        self.background.fill(pygame.Color("#ffffff"))

    def update(self):
        # выводим на экран наш белый прямоугольник
        self.screen.blit(self.background, (0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

        pygame.display.update()
