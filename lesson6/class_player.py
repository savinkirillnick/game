import pygame
import json

class Player:
    def __init__(self, controller):
        self.controller = controller
        self.speed = 3
        self.dx = 0
        self.dy = 0
        self.x = 0
        self.y = 0
        self.jump_power = 5
        self.onGround = False
        self.z = 0
        self.dz = 0
        self.g = 0.35
        # Создадим хранилице данных в виде словаря
        self.player_data = dict()
        with open("data/player.json") as file:
            self.player_data = json.load(file)
        # теперь назначение характеристик спрайта берем из словаря
        self.width = self.player_data['width']
        self.height = self.player_data['height']
        self.step = self.player_data['step']
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface((self.width, self.height))
        self.sprite.image.fill(pygame.Color("#00FF19"))
        self.sprite.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.sprite.image = pygame.image.load(self.player_data['player'])

    def move(self, move_left, move_right, move_up, move_down, move_jump):

        if move_left:
            self.dx = -self.speed
        if move_right:
            self.dx = self.speed
        if not (move_left or move_right):
            self.dx = 0
        if move_up:
            self.dy = -self.speed
        if move_down:
            self.dy = self.speed
        if not (move_up or move_down):
            self.dy = 0

        if self.onGround and move_jump:
            self.dz = -self.jump_power
        if not self.onGround:
            self.dz += self.g

        self.x += self.dx
        self.controller.collisions_obstacles(self.dx, 0)
        self.sprite.rect.x = self.x

        self.y += self.dy
        self.controller.collisions_obstacles(0, self.dy)
        self.sprite.rect.y = self.y + self.z

        self.z += self.dz
        if self.z >= 0:
            self.z = 0
            self.dz = 0
            self.onGround = True
        else:
            self.onGround = False
