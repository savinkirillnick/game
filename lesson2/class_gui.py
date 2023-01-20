import pygame


class Gui:
    def __init__(self, controller):
        pygame.init()
        self.controller = controller
        display = (controller.width * controller.tile, controller.height * controller.tile)
        self.screen = pygame.display.set_mode(display)

        pygame.display.set_caption("Last Android")

        self.background = pygame.Surface(display)
        self.background.fill(pygame.Color("#ffffff"))

    def update(self):
        self.screen.blit(self.background, (0, 0))
        # Отрисовка стен
        # пробегаемся по двумерному массиву по строкам и столбцам
        for y in range(len(self.controller.level['obstacles'])):
            for x in range(len(self.controller.level['obstacles'][y])):
                # Высчитываем координаты для каждого тайла
                coord_x = x * self.controller.tile
                coord_y = y * self.controller.tile

                # Если на план-карте уровня по конкретному ряду и столбцу стоит единица (1), значит там препятствие (стена)
                if self.controller.level['obstacles'][y][x] == 1:
                    # Создаем поверхность по размерам тайла и синего цвета
                    tile = pygame.Surface((self.controller.tile, self.controller.tile))
                    tile.fill(pygame.Color("#6262FF"))
                    # и размещаем тайл на экране по расчитанным координатам х и у
                    self.screen.blit(tile, (coord_x, coord_y))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

        pygame.display.update()
