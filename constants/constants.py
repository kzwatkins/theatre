WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Some set info
WIDTH = 650  # cinema_rect[2] # * cinema_scale
HEIGHT = 650  # cinema_rect[3] # * cinema_scale
FPS = 30  # frames per second setting
OFFSET_X = 5
OFFSET_Y = 10
SPRITE_ROWS = 3
SPRITE_COLS = 4

MIN_POSITION = WIDTH/5
MAX_POSITION = WIDTH - MIN_POSITION * 2

INCREMENT_SIZE = 7
MESSAGE_CHANGE = FPS * 3
MOVEMENT_CHANGE = int(FPS / 3)
INTRO_MESSAGES = ["Welcome to the Theatre!!", "\"Juju Bandit\" Image by Tiny Speck", "Get Ready for an Adventure!", "Created with Python and Pygame", "Pull Up a Seat!"]
