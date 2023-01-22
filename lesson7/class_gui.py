import pygame
from class_camera import *


class Gui:
    def __init__(self, controller):
        pygame.init()
        self.controller = controller
        display = (controller.width * controller.tile, controller.height * controller.tile)
        self.screen = pygame.display.set_mode(display)

        pygame.display.set_caption("Last Android")

        self.background = pygame.Surface(display)
        self.background.fill(pygame.Color("#ffffff"))

        self.camera = Camera(camera_configure)

    def update(self):
        self.screen.blit(self.background, (0, 0))

        for y in range(len(self.controller.level['back'])):
            for x in range(len(self.controller.level['back'][y])):
                tile_sprite = self.controller.back_tiles[y][x]
                if not tile_sprite:
                    continue

                self.screen.blit(tile_sprite.image, self.camera.apply(tile_sprite))

        self.screen.blit(self.controller.player.sprite.image, self.camera.apply(self.controller.player.sprite))

        for y in range(len(self.controller.level['front'])):
            for x in range(len(self.controller.level['front'][y])):
                tile_sprite = self.controller.front_tiles[y][x]
                if not tile_sprite:
                    continue
                self.screen.blit(tile_sprite.image, self.camera.apply(tile_sprite))


        hud = self.controller.get_hud()
        f1 = pygame.font.Font(None, 14)
        for item in hud:
            text = f1.render(item[2], True, (255, 255, 255))
            self.screen.blit(text, (item[0], item[1]))

        pygame.display.update()
