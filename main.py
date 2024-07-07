# pygame demo 0 - Mouse Face Click

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 60
ROCKET_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - ROCKET_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - ROCKET_WIDTH_HEIGHT

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s), etc.
image = pygame.image.load("rat-face.png")

# Get the dimensions of the image
image_width, image_height = image.get_size()

# 5 - Initialize variables
rockX = random.randrange(MAX_WIDTH)
rockY = random.randrange(MAX_HEIGHT)
rockRect = pygame.Rect(rockX,rockY, ROCKET_WIDTH_HEIGHT, ROCKET_WIDTH_HEIGHT)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        # See if user clicked
        if event.type == pygame.MOUSEBUTTONUP:
            #  mouseX, mouseY = event.pos   #  Could do this if we needed it
            
            # Check if the click was in the rect of the ball
            # If so, choose a random new location
            if rockRect.collidepoint(event.pos):
                rockX = random.randrange(MAX_WIDTH)
                rockY = random.randrange(MAX_HEIGHT)
                rockRect = pygame.Rect(rockX, rockY, ROCKET_WIDTH_HEIGHT, ROCKET_WIDTH_HEIGHT)
                
    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(WHITE)  # Clear the window with a black background
    
    # 10 - Draw all window elements
    window.blit(image, (rockX, rockY))
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)