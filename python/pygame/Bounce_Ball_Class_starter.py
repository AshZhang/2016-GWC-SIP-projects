"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
 



pygame.init()




# Set the width and height of the screen [width, height]
WIDTH = 700
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]


# BOUNCING BALL CLASS CODE  

class BouncingBall(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, colors, screen_width, screen_height):

        ball_color = random.choice(colors) # This is outside because of variable scoping.

        if self.x_location >= WIDTH - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= HEIGHT - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)

ball1 = BouncingBall(200, 200,random.randint(-10,10), random.randint(-10,10), 20)
ball2 = BouncingBall(200, 200,random.randint(-10,10), random.randint(-10,10), 20)
ball3 = BouncingBall(200, 200,random.randint(-10,10), random.randint(-10,10), 20)
ball4 = BouncingBall(200, 200,random.randint(-10,10), random.randint(-10,10), 20)
ball5 = BouncingBall(200, 200,random.randint(-10,10), random.randint(-10,10), 20)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN) 
    
    # --- Drawing code should go here
    ball1.flashBounce(screen, possible_ball_colors, WIDTH, HEIGHT)
    ball2.flashBounce(screen, possible_ball_colors, WIDTH, HEIGHT)
    ball3.flashBounce(screen, possible_ball_colors, WIDTH, HEIGHT)
    ball4.flashBounce(screen, possible_ball_colors, WIDTH, HEIGHT)
    ball5.flashBounce(screen, possible_ball_colors, WIDTH, HEIGHT)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


