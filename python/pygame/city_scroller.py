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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)

#------------! ***** ATTENTION!  READ ME! ***** !------------#
#------! IMPORTANT NOTES ABOUT CITY_SCROLLER TEMPLATE !------#

#	SCROLLER CLASS:
#		Building speeds are hardcoded at 3 (front), 2 (middle), and 1 (back).
#		When using city_scroller, ALWAYS set scroller speeds at 3, 2, and 1.
#
#	BUILDING LISTS:
#		Building lists must ALWAYS be named: "front_building_list"
#											 "middle_building_list"
#											 "back_building_list"

front_building_list = []
middle_building_list = []
back_building_list = []

class Building():

	def __init__(self, x_point, y_point, width, height, color):
		self.x_point = x_point
		self.y_point = y_point
		self.width = width
		self.height = -height
		self.color = color

	def draw(self):
	
		pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height))
		
	def move(self, speed):
		
		# move the buildings left.
		# if the building has moved out of window, delete it from correct array.
		
		self.x_point -= speed
		
		if self.x_point+self.width < 0:
			if speed == 3:
				front_building_list.remove(self)
			elif speed == 2:
				middle_building_list.remove(self)
			else:
				back_building_list.remove(self)
	
	def get_width(self):
		return self.width

class Scroller(object):
	
	def __init__(self, width, height, base, color, speed):
		self.width = width
		self.height = height
		self.base = base
		self.color = color
		self.speed = speed
	
	def add_buildings(self):
		
		# depending on scroller speed/foreground background level:
		# if there are 0 buildings in array, add a building.
		# if the last building created has moved out of the way, add a building.
		
		if self.speed == 3:
			if len(front_building_list) < 1:
				self.add_building(self.width)
			elif front_building_list[-1].x_point + front_building_list[-1].width < SCREEN_WIDTH:
				self.add_building(self.width)
		elif self.speed == 2:
			if len(middle_building_list) < 1:
				self.add_building(self.width)
			elif middle_building_list[-1].x_point + middle_building_list[-1].width < SCREEN_WIDTH:
				self.add_building(self.width)
		else:
			if len(back_building_list) < 1:
				self.add_building(self.width)
			elif back_building_list[-1].x_point + back_building_list[-1].width < SCREEN_WIDTH:
				self.add_building(self.width)
	def add_building(self, x_location):
				
		# make a building.
		# put the building in the right array, depending on scroller speed.
		if self.speed == 3:
			building_height = 0
		elif self.speed == 2:
			building_height = 200
		else:
			building_height = 400
		
		building = Building(x_location, self.height, random.randint(50, 100), random.randint(100, 250)+building_height, self.color)
		
		if self.speed == 3:
			front_building_list.append(building)
		elif self.speed == 2:
			middle_building_list.append(building)
		else:
			back_building_list.append(building)

	def draw_buildings(self):
		
		if self.speed == 3:
			for i in front_building_list:
				i.draw()
		elif self.speed == 2:
			for i in middle_building_list:
				i.draw()
		else:
			for i in back_building_list:
				i.draw()
	def move_buildings(self):
		
		if self.speed == 3:
			for i in front_building_list:
				i.move(self.speed)
		elif self.speed == 2:
			for i in middle_building_list:
				i.move(self.speed)
		else:
			for i in back_building_list:
				i.move(self.speed)

