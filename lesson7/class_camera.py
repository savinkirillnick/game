import pygame


class Camera(object):
    def __init__(self, camera_func, width=0, height=0):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def size(self, width, height):
        self.state.width = width
        self.state.height = height

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target, _width, _height):
        self.state = self.camera_func(self.state, target.rect, _width, _height)


def camera_configure(camera, target_rect, win_width, win_height):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + win_width / 2, -t + win_height / 2

    l = min(0, l)
    l = max(-(camera.width - win_width), l)
    t = max(-(camera.height - win_height), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)
