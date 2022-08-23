import pygame as py
py.font.init()

py.display.set_caption('AI 2DTrackMania - Vishal Tyagi')
# =================== General constants ==================================
FPS = 30
WIN_WIDTH = 500
WIN_HEIGHT = 800
STARTING_POS = (WIN_WIDTH/2, WIN_HEIGHT-100)
SCORE_VEL_MULTIPLIER = 0.00
BAD_GENOME_TRESHOLD = 200

INPUT_NEURONS = 9
OUTPUT_NEURONS = 4

NEURON_DBG = False

# =================== Car Specs ==================================

CAR_DBG = False
FRICTION = -0.1
MAX_VEL = 10
MAX_VEL_REDUCTION = 1
ACC_STRENGHT = 0.2
BRAKE_STREGHT = 1
TURN_VEL = 2
SENSOR_DISTANCE = 200
ACTIVATION_TRESHOLD = 0.5

# =================== Road Specs ==================================

ROAD_DBG = False
MAX_ANGLE = 1
MAX_DEVIATION = 300
SPACING = 200
NUM_POINTS = 15
SAFE_SPACE = SPACING + 50
ROAD_WIDTH = 200

# =================== Display and Colors ==================================

NODE_RADIUS = 20
NODE_SPACING = 5
LAYER_SPACING = 100
CONNECTION_WIDTH = 1

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

RED = (7, 73, 57)
DARK_RED = (14, 149, 116)
RED_PALE = (21, 225, 175)
DARK_RED_PALE = (16, 174, 135)

GREEN = (8, 141, 129)  # Outer
DARK_GREEN = (12, 217, 198)  # Normal
GREEN_PALE = (14, 255, 248)  # Activate
DARK_GREEN_PALE = (10, 216, 210)

BLUE = (0, 0, 255)
BLUE_PALE = (200, 200, 255)
DARK_BLUE = (100, 100, 150)

NODE_FONT = py.font.SysFont("roboto", 15)
STAT_FONT = py.font.SysFont("roboto", 50)


# =================== Constants for internal use ==================================
GEN = 0

# enumerations
ACC = 0
BRAKE = 1
TURN_LEFT = 2
TURN_RIGHT = 3

INPUT = 0
MIDDLE = 1
OUTPUT = 2
