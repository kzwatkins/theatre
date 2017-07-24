from constants.constants import *
from spritesheet.spritesheetmatrix import SpritesheetMatrix
from sprites.sprite_class import SpriteClass
from theatre.theatre import Theatre

theatre = Theatre("Theatre")
scale = int(min(WIDTH, HEIGHT)/10)
ssm1 = SpritesheetMatrix("../images/npc_juju_bandit_bandana_none_variant_green_x1_walk_png_1354834285.png", 4, 4, BLACK, scale * 2)
theatre.add_sprite_by_filename("../images/npc_gwendolyn__x1_iconic_png_1354832927.png", BLACK, scale)
# ssm2 = SpritesheetMatrix("../images/npc_gwendolyn__x1_talk_png_1354832932.png", 10, 8, BLACK, scale)

theatre.add_sprite_from_spritesheet_matrix(ssm1)
# theatre.add_sprite_from_spritesheet_matrix(ssm2)
theatre.run()


