# Adapted from https://pygame.org/wiki/Spritesheet

import pygame
from spritesheet.spritesheet import Spritesheet

class SpritesheetMatrix(Spritesheet):
    def __init__(self, filename, rows=3, cols=4, colorkey=None, scale=1):
        super(SpritesheetMatrix, self).__init__(filename)
        self.colorkey = colorkey
        self.scale = scale
        self.sprite_tuples = []
        self.images = []
        self.rows = int(rows)
        self.cols = int(cols)
        self.num_imgs = int(self.rows * self.cols)

        self.set_dimensions()
        self.create_rects()


        for row in range(0, self.rows):
            self.images.append([])
            self.images[row] = super(SpritesheetMatrix, self).images_at(self.sprite_tuples[row], colorkey, scale)

    def set_dimensions(self):
        """Determine the width and height of each individual sprite assuming they are equal size"""
        # dimensions = Spritesheet.spritesheet_size()
        dimensions = super(SpritesheetMatrix, self).spritesheet_size()
        self.sprite_width = int(dimensions[0] / self.cols)
        self.sprite_height = int(dimensions[1] / self.rows)

    def create_rects(self):
        """Create the rectangles for all sprites"""
        for row in range(0, self.rows):
            self.sprite_tuples.append([])

            for col in range(0, self.cols):
                self.sprite_tuples[row].append((col * self.sprite_width, row * self.sprite_height, self.sprite_width, self.sprite_height))

    def get_rect(self):
        return pygame.Rect((0, 0, self.sprite_width, self.sprite_height))

    def get_num_images(self):
        return self.num_imgs

    def load_strip_matrix(self, colorkey = None, scale = 1):
        """Load the strips into a matrix"""
        self.strip_matrix = []
        for row in range(0, self.rows):
            self.matrix.append([])
            self.matrix[row].append([self.load_strip(sprite_tuple, self.cols, colorkey, scale) for sprite_tuple in self.sprite_tuples[row]])

    def get_sprite(self, row, col):
        """Get a particular sprite """
        if row in range (0,self.rows) and col in range (0, self.cols):
            return self.sprites[row][col]

        return None

    def get_image(self, row, col):
        """Get a particular sprite """
        if row in range (0,self.rows) and col in range (0, self.cols):
            return self.images[row][col]

        return None

    def get_images(self):
        return self.images

    def get_sprite_width(self):
        return self.sprite_width

    def get_sprite_height(self):
        return self.sprite_height

    def get_num_sprites(self):
        return int(self.rows * self.cols)

    def get_forward_sprites(self):
        return self.sprites[0::self.cols]

    def get_backward_sprites(self):
        return self.sprites[2::self.cols]

    def get_right_sprites(self):
        return self.sprites[1::self.cols]

    def get_left_sprites(self):
        return self.sprites[3::self.cols]