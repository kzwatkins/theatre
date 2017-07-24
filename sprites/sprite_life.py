import sys
from sprites.sprite_class import SpriteClass
from constants.constants import *


class SpriteLife(object):

    def __init__(self, walk_left_filename, walk_right_filename, colorkey = None, scale = 1, walk_left_end_filename = None, walk_right_end_filename = None,
                 idle_filename = None, spawn_filename = None, shrink_filename = None):
        self.walk_left = SpriteClass(walk_left_filename, colorkey, scale)
        self.walk_right = SpriteClass(walk_right_filename, colorkey, scale)




