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

        # Рисуем передний фон аналогично слою back
        for y in range(len(self.controller.level['front'])):
            for x in range(len(self.controller.level['front'][y])):
                tile_sprite = self.controller.front_tiles[y][x]
                if not tile_sprite:
                    continue
                self.screen.blit(tile_sprite.image, (tile_sprite.rect.x, tile_sprite.rect.y))

        pygame.display.update()
