import pygame, sys, random
from pygame.locals import *
from constants.constants import *
from sprites.sprite_class import SpriteClass
from spritesheet.spritesheetmatrix import SpritesheetMatrix

class Theatre(object):

    def __init__(self, caption):

        pygame.init()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', int(MIN_POSITION/7))

        self.fps_clock = pygame.time.Clock()
        self.fps_count = 1
        self.sprites = []
        self.DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(caption)
        self.cinema_sprite = SpriteClass("../images/cinematheatre.png", BLACK, int(min(WIDTH, HEIGHT)))
        self.cinema = self.cinema_sprite.get_image()
        self.sprite_rects = []
        self.image_scale_factor = int(min(WIDTH, HEIGHT) / 8)
        self.DISPLAYSURF_RECT = self.DISPLAYSURF.get_rect()
        self.DISPLAYSURF_CENTERX = self.DISPLAYSURF_RECT.centerx
        self.DISPLAYSURF_CENTERY = self.DISPLAYSURF_RECT.centery

    def add_sprite_by_filename(self, filename, colorkey = None, scale = 1):
        sprite = SpriteClass(filename, colorkey, scale)
        self.sprites.append([])
        self.sprite_rects.append([])
        sprites_len = len(self.sprites)
        self.sprites[sprites_len - 1] = []
        self.sprite_rects[sprites_len - 1] = []

        self.sprites[sprites_len - 1].append(sprite.get_image().convert())
        self.sprite_rects[sprites_len - 1].append(sprite.get_rect())

    def add_sprite_from_spritesheet_matrix(self, spritesheet_matrix):
        sprites_matrix = spritesheet_matrix.get_images()
        sprites_matrix_rect = spritesheet_matrix.get_rect()
        len_sprites = len(self.sprites)
        rows = len(sprites_matrix)
        for row in range(0, rows):
            self.sprites.append([])
            self.sprite_rects.append([])
            self.sprites[len_sprites] = sprites_matrix[row]

            cols = len(sprites_matrix[row])
            for col in range(0, cols):
                self.sprite_rects[len_sprites].append(sprites_matrix_rect)


    def run(self):
        indices = []
        positions = []
        directions = []
        msg_index = 1
        movement_index = 1
        msg_movement_index = 1

        rows = len(self.sprites)
        for row in range(0, rows):
            indices.append(0)
            positions.append(MIN_POSITION)
            directions.append("right")

        while True:
            self.DISPLAYSURF.fill(WHITE)
#            self.cinema_rect = self.cinema.get_rect()

            self.cinema_rect = self.cinema_sprite.get_rect()
            self.fps_count = (self.fps_count + 1) % FPS

            self.DISPLAYSURF.blit(self.cinema, (self.DISPLAYSURF_CENTERX - self.cinema_rect.centerx, 0))

            textsurface = self.myfont.render("Created by Kera Z. Watkins", False, BLACK)
            self.DISPLAYSURF.blit(textsurface, (self.DISPLAYSURF_CENTERX - int(textsurface.get_width() / 2), self.DISPLAYSURF_CENTERX - textsurface.get_height() * 6))

            textsurface = self.myfont.render("Supported by Watkins Proactive Research LLC", False, BLACK)
            self.DISPLAYSURF.blit(textsurface, (self.DISPLAYSURF_CENTERX - int(textsurface.get_width() / 2), self.DISPLAYSURF_CENTERX - textsurface.get_height() * 5))

            textsurface = self.myfont.render(INTRO_MESSAGES[msg_index], False, BLACK)
            self.DISPLAYSURF.blit(textsurface, (self.DISPLAYSURF_CENTERX - int(textsurface.get_width() / 2), self.DISPLAYSURF_CENTERX - textsurface.get_height() * 4))

            for row in range(0, rows):
                sprites = self.sprites[row]
                sprite_len = len(self.sprites[row])
                # TODO Fix issue with empty matrices
                if sprite_len < 1: continue

                sprite_rects = self.sprite_rects[row]

                if self.fps_count is 0:
                    self.get_new_direction(positions, directions, row)
                    self.get_new_position(positions, directions, row)

                if movement_index is 0:
                    indices[row] = (indices[row] + 1) % sprite_len

                sprite = self.pick_sprite(sprites, indices, directions[row], row)
                sprite_rect = self.pick_sprite_rect(sprite_rects, indices, row)

                self.DISPLAYSURF.blit(sprite, (positions[row], self.DISPLAYSURF_CENTERY - sprite_rect.centery))

            movement_index = (movement_index + 1) % MOVEMENT_CHANGE
            msg_movement_index = (msg_movement_index + 1) % MESSAGE_CHANGE
            if msg_movement_index is 0:
                msg_index = random.randrange(0, len(INTRO_MESSAGES))

            self.check_update()

    def get_new_direction(self, positions, directions, row):
        if positions[row] + OFFSET_X >= MAX_POSITION:
            directions[row] = "left"
        elif positions[row] - OFFSET_X <= MIN_POSITION:
            directions[row] = "right"

    def get_new_position(self, positions, directions, row):
        if directions[row] is "right":
            positions[row] = positions[row] + OFFSET_X
        elif directions[row] is "left":
            positions[row] = positions[row] - OFFSET_X

    def pick_sprite(self, sprites, indices, direction, row):
        sprite = sprites[indices[row]]
        if(direction == "left"):
            sprite = pygame.transform.flip(sprite, True, False)
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