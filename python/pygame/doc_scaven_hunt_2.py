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
GREY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("DocScaven")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Circle():
	
	def __init__ (self, color, mouse_position, x_speed, y_speed, radius):
		self.x_pos = mouse_position[0]
		self.y_pos = mouse_position[1]
		self.x_speed = x_speed
		self.y_speed = y_speed
		self.color = color
		self.radius = radius
		
	def draw(self):
		pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)
	
	def move(self):
		# move circle by x and y speed
		# if circle reaches window edge, turn speed around
	
		self.x_pos += self.x_speed
		self.y_pos += self.y_speed
		
		if self.x_pos > SCREEN_WIDTH or self.x_pos < 0:
			self.x_speed *= -1
		if self.y_pos > SCREEN_HEIGHT or self.y_pos < 0:
			self.y_speed *= -1

circle_list = []
		
# -------- Main Program Loop -----------
while not done:

	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	mouse_pos = pygame.mouse.get_pos()
	

	if pygame.mouse.get_pressed()[0]:
		print("Here!")
		
		# color, mouse position, random x speed, random y speed, radius
		my_circle = Circle(CYAN, mouse_pos, random.randint(-10, 10), random.randint(-10, 10), 20)
		circle_list.append(my_circle)
	
		# random.randint(0, 255), 
		# random.randint(20, 80)

	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.

	# --- Drawing code should go here
	
	screen.fill(WHITE)
	
	for i in circle_list:
		i.draw()
		i.move()



	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
