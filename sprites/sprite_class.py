import pygame
# from constants.constants import *


class SpriteClass(object):

    def __init__(self, filename, colorkey = None, scale = 1):
        self.image = pygame.image.load(filename)
        self.set_color(colorkey)
        self.set_scale(scale)
        self.image_rect = self.image.get_rect()
        self.image = self.image.convert()

    def set_scale(self, scale = 1):
        if scale is not 1:
            self.image_scale = int(scale)
            self.image = pygame.transform.scale(self.image, (scale, scale))

    def set_color(self, colorkey = None):
        if colorkey is not None:
            if colorkey is -1:
                colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey, pygame.RLEACCEL)

    def get_size(self):
        return self.image_rect.size

    def get_image(self):
        return self.image

    def get_rect(self):
        return self.image_rect



