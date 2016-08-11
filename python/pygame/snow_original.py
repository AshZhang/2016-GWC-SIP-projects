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
from PIL import Image

bg = pygame.image.load("images/winter.jpg")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
WIDTH = 700
HEIGHT = 500

pygame.display.set_caption("Snow")


class SnowFlake():
	'''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
	'''
	def __init__(self, size, position, speed, wind = False):
		self.size = size
		self.position = position
		self.speed = speed
		self.wind = wind
    
	def fall(self):
		self.position[1] += self.speed
		
		if self.wind == True:
			self.position[0] += self.speed//2
		"""
        Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
        A positive integer will have the snowflake falling down the screen. 
        A negative integer will have the snowflake falling up the screen. 
        
        If wind = True
            - the x direction of the snowflake changes
		"""
		if self.position[1] > HEIGHT:
			self.position[1] = 0
		
		if self.position[0] > WIDTH:
			self.position[0] = 0
		
	def draw(self):
		global screen
		global WHITE
		pygame.draw.circle(screen, WHITE, self.position, self.size)
		
		"""
        Uses pygame and the global screen variable to draw the snowflake on the screen
		"""
		
		
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
#speed = 5


#INITIALIZE YOUR SNOWFLAKE HERE! 

# Snow List
snow_list = []

for i in range (random.randint(10, 20)):
	snowflake = SnowFlake(5, [random.randint(0, WIDTH), 0], random.randint(1, 10), True)
	snow_list.append(snowflake)

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
	screen.blit(bg, (0, 0))

    # --- Drawing code should go here
    # Begin Snow
	
	
	for i in snow_list:
		i.fall()
		i.draw()



    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
