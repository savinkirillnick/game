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

        for y in range(len(self.controller.level['obstacles'])):
            for x in range(len(self.controller.level['obstacles'][y])):
                coord_x = x * self.controller.tile
                coord_y = y * self.controller.tile

                if self.controller.level['obstacles'][y][x] == 1:
                    tile = pygame.Surface((self.controller.tile, self.controller.tile))
                    tile.fill(pygame.Color("#6262FF"))
                    self.screen.blit(tile, (coord_x, coord_y))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

        # Рисуем персонажа и объекты
        self.screen.blit(self.controller.player.sprite.image, self.controller.player.sprite)

        pygame.display.update()
