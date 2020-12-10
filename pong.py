""" Import Modules """
import os, sys, random
# Disable pygame Message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import (KEYDOWN, KEYUP, K_DOWN, K_UP, QUIT, K_w, K_s)
from cmyui import (log, Ansi)

""" Initialize pygame """
pygame.init()
fps = pygame.time.Clock()

""" Global Variables """
# Window Resolution
WIDTH  = 600
HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Audio
PAD_SOUND   = pygame.mixer.Sound("./audio/pad.mp3")
WALL_SOUND  = pygame.mixer.Sound("./audio/wall.mp3")
SCORE_SOUND = pygame.mixer.Sound("./audio/score.mp3")
MUSIC_SOUND = pygame.mixer.Sound("./audio/music.mp3")
MUSIC_SOUND.set_volume(0.1)

# Ball Measurements
BALL_RADIUS = 10

# Pad Measurements
PAD_WIDTH       = 8
PAD_HEIGHT      = 80
PAD_WIDTH_HALF  = PAD_WIDTH//2
PAD_HEIGHT_HALF = PAD_HEIGHT//2

# Ball Position And Velocity
ball_pos = [0, 0]
ball_vel = [0, 0]

# Pad Position And Velocity
pad1_pos = [0, 0]
pad2_pos = [0, 0]
pad1_vel = 0
pad2_vel = 0

# Score
left_score  = 0
right_score = 0

""" Window Declaration """
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("pong.py")

""" Initialize Ball """
# Spawns A Ball.
# If Right Is True: Spawn Right
# If Right Is False: Spawn Left
def init_ball(right: bool) -> None:
    # Log
    log("Spawned ball!", Ansi.LCYAN)

    # Get Our Globals
    global ball_pos, ball_vel

    # Set Ball Position
    ball_pos = [WIDTH//2, HEIGHT//2]

    # Get A Random Horizontal And Vertical Value
    horz = random.randrange(2, 4)
    vert = random.randrange(1, 3)

    # Spawn On The Left If Right Is False
    if not right:
        horz = -horz

    # Set Velocity
    ball_vel = [horz, -vert]

""" Initialize """
def init() -> None:
    # Log
    log("Initializing...", Ansi.LYELLOW)

    # Get Our Globals
    global pad1_pos, pad2_pos
    
    # Set Pad Positions
    pad1_pos = [PAD_WIDTH_HALF-1, HEIGHT//2]
    pad2_pos = [WIDTH+1-PAD_WIDTH_HALF, HEIGHT//2]

    # Ball Spawns Right or Left
    if random.randrange(0, 2) == 0:
        init_ball(True)
    else:
        init_ball(False)
    
    # Log
    log("Finished initializing!", Ansi.LYELLOW)

""" Draw Window """
def draw(window) -> None:
    # Get Our Globals
    global pad1_pos, pad2_pos, ball_pos, ball_vel, left_score, right_score

    # Play Music
    MUSIC_SOUND.play(-1)

    # Set Window Background To Black
    window.fill(BLACK)

    # Draw Gutters
    pygame.draw.line(window, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(window, WHITE, [WIDTH-PAD_WIDTH, 0],[WIDTH-PAD_WIDTH, HEIGHT], 1)

    # Update Pads Vertical Position, Keep Pads On Screen
    if pad1_pos[1] > PAD_HEIGHT_HALF and pad1_pos[1] < HEIGHT - PAD_HEIGHT_HALF:
        pad1_pos[1] += pad1_vel
    elif pad1_pos[1] == PAD_HEIGHT_HALF and pad1_vel > 0:
        pad1_pos[1] += pad1_vel
    elif pad1_pos[1] == HEIGHT - PAD_HEIGHT_HALF and pad1_vel < 0:
        pad1_pos[1] += pad1_vel
    if pad2_pos[1] > PAD_HEIGHT_HALF and pad2_pos[1] < HEIGHT - PAD_HEIGHT_HALF:
        pad2_pos[1] += pad2_vel
    elif pad2_pos[1] == PAD_HEIGHT_HALF and pad2_vel > 0:
        pad2_pos[1] += pad2_vel
    elif pad2_pos[1] == HEIGHT - PAD_HEIGHT_HALF and pad2_vel < 0:
        pad2_pos[1] += pad2_vel

    # TODO: AI/Bot As Pad 2

    # Draw Pads
    pygame.draw.polygon(window, WHITE, [[pad1_pos[0] - PAD_WIDTH_HALF, pad1_pos[1] - PAD_HEIGHT_HALF], [pad1_pos[0] - PAD_WIDTH_HALF, pad1_pos[1] + PAD_HEIGHT_HALF], [pad1_pos[0] + PAD_WIDTH_HALF, pad1_pos[1] + PAD_HEIGHT_HALF], [pad1_pos[0] + PAD_WIDTH_HALF, pad1_pos[1] - PAD_HEIGHT_HALF]], 0)
    pygame.draw.polygon(window, WHITE, [[pad2_pos[0] - PAD_WIDTH_HALF, pad2_pos[1] - PAD_HEIGHT_HALF], [pad2_pos[0] - PAD_WIDTH_HALF, pad2_pos[1] + PAD_HEIGHT_HALF], [pad2_pos[0] + PAD_WIDTH_HALF, pad2_pos[1] + PAD_HEIGHT_HALF], [pad2_pos[0] + PAD_WIDTH_HALF, pad2_pos[1] - PAD_HEIGHT_HALF]], 0)

    # Update And Draw Ball
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])
    pygame.draw.circle(window, WHITE, ball_pos, BALL_RADIUS, 0)

    # Ball Collision Check With Walls
    if int(ball_pos[1]) <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        WALL_SOUND.play(1)
    if int(ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        WALL_SOUND.play(1)

    # Ball Collision Check With Gutters Or Pads
    if int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and int(ball_pos[1]) in range(pad1_pos[1] - PAD_HEIGHT_HALF, pad1_pos[1] + PAD_HEIGHT_HALF, 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
        PAD_SOUND.play(1)
    elif int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:
        right_score += 1
        log(f"Right scored! ({right_score})", Ansi.LBLUE)
        init_ball(True)
        SCORE_SOUND.play(1)
    if int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and int(ball_pos[1]) in range(pad2_pos[1] - PAD_HEIGHT_HALF, pad2_pos[1] + PAD_HEIGHT_HALF, 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
        PAD_SOUND.play(1)
    elif int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
        left_score += 1
        log(f"Left scored! ({left_score})", Ansi.LBLUE)
        init_ball(False)
        SCORE_SOUND.play(1)

    # Update and Draw Scores
    font = pygame.font.SysFont("Comic Sans MS", 20)
    label = font.render(str(left_score), 1, WHITE)
    window.blit(label, (50, 20))
    label = font.render(str(right_score), 1, WHITE)
    window.blit(label, (530, 20))

""" Key Up/Down Events """
def keyup(event) -> None:
    # Get Our Globals
    global pad1_vel, pad2_vel

    # If Keys Are Up Set Pad Velocity To 0
    if event.key in (K_w, K_s):
        pad1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        pad2_vel = 0

def keydown(event) -> None:
    # Get Our Globals
    global pad1_vel, pad2_vel

    # If Keys Are Down Set Pad Velocity To -8, 8
    if event.key == K_w:
        pad1_vel = -8
    elif event.key == K_s:
        pad1_vel = 8
    elif event.key == K_UP:
        pad2_vel = -8
    elif event.key == K_DOWN:
        pad2_vel = 8

""" Main Loop """
def main() -> None:
    # Initialize pong.py
    init()

    # Log
    log("pong.py is now running!", Ansi.LGREEN)

    while True:
        # Draw Window
        draw(window)

        # Handle Events
        for event in pygame.event.get():
            # Key Up Event
            if event.type == KEYUP:
                keyup(event)
            # Key Down Event
            elif event.type == KEYDOWN:
                keydown(event)
            # Quit Event
            elif event.type == QUIT:
                log("Quitting pong.py! Thank you for playing!", Ansi.LRED)
                pygame.quit()
                sys.exit()

        # Update Display
        pygame.display.update()

        # Set FPS
        fps.tick(60)

""" Run pong.py """
if __name__ == "__main__":
    main()
