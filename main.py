""" Import Modules """
import sys, random, pygame
from pygame.locals import (color, Color, Rect)
from typing import (Tuple, List)
from cmyui import log

""" Initialize pygame """
pygame.init()
fps = pygame.time.Clock()

""" Globals """
# Window Resolution
WIDTH:  int = 600
HEIGHT: int = 400

# Colors
WHITE: tuple = tuple[255, 255, 255]
RED:   tuple = tuple[255, 0, 0]
GREEN: tuple = tuple[0, 255, 0]
BLACK: tuple = tuple[0, 0, 0]

# Ball Measurements
BALL_RADIUS: int = 20

# Pad Measurements
PAD_WIDTH:       int = 8
PAD_HEIGHT:      int = 80
PAD_WIDTH_HALF:  int = PAD_WIDTH//2
PAD_HEIGHT_HALF: int = PAD_HEIGHT//2

# Ball Position And Velocity
ball_pos: list = list[0, 0]
ball_vel: list = list[0, 0]

# Pad Position And Velocity
pad1_pos: int = 0
pad2_pos: int = 0
pad_vel:  int = 0

# Score
left_score:  int = 0
right_score: int = 0

""" Window Declaration """
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("pong.py")

""" Initialize Ball """
# Spawns A Ball.
# If Right Is True: Spawn Right
# If Right Is False: Spawn Left
def init_ball(right: bool) -> None:
    # Get Our Globals
    global ball_pos, ball_vel

    # Set Ball Position
    ball_pos = List[WIDTH//2, HEIGHT//2]

    # Get A Random Vertical and Horizontal Value
    vert: int = random.randrange(1, 3)
    horz: int = random.randrange(2, 4)

    # Spawn On The Left If Right Is False
    if not right:
        horz = -horz

    # Set Velocity
    ball_vel = List[horz, -vert]

""" Initialize """
def init() -> None:
    # Get Our Globals
    global pad1_pos, pad2_pos
    
    # Set Pad Positions
    pad1_pos = List[PAD_WIDTH_HALF-1, HEIGHT//2]
    pad2_pos = List[WIDTH+1-PAD_WIDTH_HALF, HEIGHT//2]

    # Ball Spawns Right
    if random.randrange(0, 2) == 0:
        init_ball(True)
    
    # Ball Spawns Left
    else:
        init_ball(False)

""" Draw Window """
def draw(window) -> None:
    # Get Our Globals
    global pad1_pos, pad2_pos, ball_pos, ball_vel

    # Set Window Background To Black
    window.fill(BLACK)
    pygame.draw.line(window, WHITE, [WIDTH//2, 0],[WIDTH//2, HEIGHT], 1)
    pygame.draw.line(window, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(window, WHITE, [WIDTH-PAD_WIDTH, 0],[WIDTH-PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(window, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)


""" Main Loop """
def main() -> None:
    while True:
        # Draw Window
        draw(window)

        # Update Display
        pygame.display.update()

        # Set FPS
        fps.tick(60)




