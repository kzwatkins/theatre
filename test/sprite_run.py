from constants.constants import *
from sprites.sprite_class import SpriteClass
from theatre.theatre import Theatre

theatre = Theatre("Sprite in Theatre")
theatre.add_sprite_by_filename("../images/npc_gwendolyn__x1_iconic_png_1354832927.png", BLACK, int(min(WIDTH, HEIGHT)/10))
theatre.run()