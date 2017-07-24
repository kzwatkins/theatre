from constants.constants import *
from spritesheet.spritesheetmatrix import SpritesheetMatrix
from theatre.theatre import Theatre

theatre = Theatre("Theatre")
ssm = SpritesheetMatrix("../images/npc_gwendolyn__x1_idle_png_1354832938.png", 10, 8, BLACK, int(min(WIDTH, HEIGHT)/10))
theatre.add_sprite_from_spritesheet_matrix(ssm)
theatre.run()


