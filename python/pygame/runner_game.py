import pygame
import random
from city_scroller import Scroller 
from city_scroller import Building
from city_scroller import front_building_list
from city_scroller import middle_building_list
from city_scroller import back_building_list
from city_scroller import SCREEN_WIDTH
from city_scroller import SCREEN_HEIGHT
from city_scroller import screen

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

done = False
		
front_building_list = []
middle_building_list = []
back_building_list = []
sprite_list = []

front_scroller = Scroller(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT, BLACK, 3)
middle_scroller = Scroller(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT, BLUE, 2)
back_scroller = Scroller(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT, CYAN, 1)

class RunnerSprite(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.color = color
		self.width = width
		self.height = height
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect[0] -= 5
	
		if self.rect[0] < 0:
			self.rect[0] = SCREEN_WIDTH
		elif self.rect[0] > SCREEN_WIDTH:
			self.rect[0] = 0
		
		if self.rect[1] < 0:
			self.rect[1] = SCREEN_HEIGHT
		elif self.rect[1] > SCREEN_HEIGHT:
			self.rect[1] = 0
all_sprites_list = pygame.sprite.Group()
good_sprites_list = pygame.sprite.Group()

for i in range(20):
	bread = RunnerSprite(YELLOW, 25, 25)
	bread.rect[0] = SCREEN_WIDTH + random.randint(0, 100)
	good_sprites_list.add(bread)

player = RunnerSprite(GREEN, 50, 50)
all_sprites_list.add(player)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill(WHITE)

	back_scroller.add_buildings()
	back_scroller.draw_buildings()
	back_scroller.move_buildings()
	
	middle_scroller.add_buildings()
	middle_scroller.draw_buildings()
	middle_scroller.move_buildings()
	
	front_scroller.add_buildings()
	front_scroller.draw_buildings()
	front_scroller.move_buildings()
	
	player.rect = pygame.mouse.get_pos()
	all_sprites_list.draw(screen)
	for i in good_sprites_list:
		i.update()
	
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
exit()