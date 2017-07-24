import pygame, sys
from pygame.locals import *
from constants.constants import *
from sprites.sprite_class import SpriteClass
from spritesheet.spritesheetmatrix import SpritesheetMatrix

class Theatre(object):

    def __init__(self, caption):

        pygame.init()

        self.fps_clock = pygame.time.Clock()
        self.fps_count = 1
        self.sprites = []
        self.DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(caption)
        self.cinema_sprite = SpriteClass("../images/cinematheatre.png", BLACK, int(min(WIDTH, HEIGHT)))
        self.cinema = self.cinema_sprite.get_image()
        self.sprite_rects = []
        # self.cinema = pygame.image.load("../images/cinematheatre.png")
        # self.cinema_rect = self.cinema.get_rect()
        # self.cinema = self.cinema.convert()
        # self.cinema.set_colorkey(BLACK, pygame.RLEACCEL)
        # self.cinema_scale = int(min(WIDTH, HEIGHT))
        # self.cinema = pygame.transform.scale(self.cinema, (self.cinema_scale, self.cinema_scale))
        self.image_scale_factor = int(min(WIDTH, HEIGHT) / 8)
        self.DISPLAYSURF_RECT = self.DISPLAYSURF.get_rect()
        self.DISPLAYSURF_CENTERX = self.DISPLAYSURF_RECT.centerx
        self.DISPLAYSURF_CENTERY = self.DISPLAYSURF_RECT.centery
        # self.cinema_rect = self.cinema.get_rect() # Redo after resize!

    def add_sprite_by_filename(self, filename, colorkey = None, scale = 1):
        sprite = SpriteClass(filename, colorkey, scale)
        self.sprites.append([])
        self.sprite_rects.append([])
        sprites_len = len(self.sprites)
        self.sprites[sprites_len - 1].append(sprite.convert())
        self.sprite_rects[sprites_len - 1].append(sprite.get_rect)

    def add_sprite_from_spritesheet_matrix(self, spritesheet_matrix):
        sprites_matrix = spritesheet_matrix.get_images()
        sprites_matrix_rect = spritesheet_matrix.get_rect()
        rows = len(sprites_matrix)
        for row in range(0, rows):
            self.sprites.append([])
            self.sprite_rects.append([])
            self.sprites[row] = sprites_matrix[row]
            # self.sprite_rects[row] = []
            # self.sprite_rects[row].append([])

            cols = len(sprites_matrix[row])
            # self.sprite_rects[row] = []
            for col in range(0, cols):
                self.sprite_rects[row].append(sprites_matrix_rect)

    def run(self):
        indices = []
        positions = []
        directions = []
        rows = len(self.sprites)
        for row in range(0, rows):
            indices.append(0)
            positions.append(WIDTH/10)
            directions.append("right")

        while True:
            self.DISPLAYSURF.fill(WHITE)
#            self.cinema_rect = self.cinema.get_rect()

            self.cinema_rect = self.cinema_sprite.get_rect()
            self.fps_count = (self.fps_count + 1) % FPS

            self.DISPLAYSURF.blit(self.cinema, (self.DISPLAYSURF_CENTERX - self.cinema_rect.centerx, 0))

            for row in range(0, rows):
                sprites = self.sprites[row]
                sprite_len = len(self.sprites[row])
                sprite_rects = self.sprite_rects[row]
                if self.fps_count is 0:
                    indices[row] = (indices[row] + 1) % sprite_len
                    self.get_new_direction(positions, directions, row)
                    self.get_new_position(positions, directions, row)

                sprite = self.pick_sprite(sprites, indices, row)
                sprite_rect = self.pick_sprite_rect(sprite_rects, indices, row)

                # sprite = sprite.convert()
                self.DISPLAYSURF.blit(sprite, (self.DISPLAYSURF_CENTERX - sprite_rect.centerx, self.DISPLAYSURF_CENTERY - sprite_rect.centery))

            self.check_update()

    def get_new_direction(self, positions, directions, row):
        if positions[row] + OFFSET_X >= WIDTH - WIDTH/10:
            directions[row] = "left"
        elif positions[row] - OFFSET_X <= WIDTH/10:
            directions[row] = "right"

    def get_new_position(self, positions, directions, row):
        if directions[row] is "right":
            positions[row] = positions[row] + OFFSET_X
        elif directions[row] is "left":
            positions[row] = positions[row] - OFFSET_X

    def pick_sprite(self, sprites, indices, row):
        sprite = sprites[indices[row]]
        return sprite

    def pick_sprite_rect(self, sprite_rects, indices, row):
        sprite_rect = sprite_rects[indices[row]]
        return sprite_rect





    def check_update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()