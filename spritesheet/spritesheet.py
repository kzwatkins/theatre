import pygame


class Spritesheet(object):
    """Adapted from https://pygame.org/wiki/Spritesheet"""

    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename)
            self.rect = self.sheet.get_rect()
            self.sheet = self.sheet.convert()

        except:
            print("Unable to load spritesheet img: " + filename)
            raise SystemExit('Problem opening file')

    def image_at(self, rectangle, colorkey = None, scale = 1):
        """Loads image from x,y,x+offset,y+offset"""

        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        self.set_colorkey(image, colorkey)
        image = self.rescale(image, scale)

        return image

    def set_colorkey(self, image, colorkey = None):
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)

    def rescale(self, image, scale = 1):
        if scale is not 1:
            image = pygame.transform.scale(image, (scale, scale))

        return image

    def images_at(self, rects, colorkey = None, scale = 1):
        """Loads multiple images, supply a list of coordinates"""

        return [self.image_at(rect, colorkey, scale) for rect in rects]

    def load_strip(self, rect, image_count, colorkey = None, scale = 1):
        """Loads a strip of images and returns them as a list"""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey, scale)

    def spritesheet_size(self):
        return self.rect.size

    def spritesheet_center(self):
        return self.rect.center