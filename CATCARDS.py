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
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Cat cards")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#character animation frame lists
wiz_list = ["WIZ.png", "WIZ2.png"]
foe_list=["foe.png","foe2.png"]
firey_list=["fiery1.png", "fiery2.png"]
watery_list=["watery1.png", "watery2.png"]
icy_list=["icy1.png","icy2.png"]
speed=2

class character():
	def __init__(self,image):
		#super()._init_()
		#self.image=pygame.surface([width,height])
		self.image=pygame.image.load (image)
		self.rect=self.image.get_rect()
		# self.width=width
		# self.height=height
		# self.rect.x=X
		# self.rect.y=Y
	def draw(self, image,X,Y):
		self.image=pygame.image.load (image)
		self.rect=self.image.get_rect()
		self.rect.x=X
		self.rect.y=Y
		# self.draw.rect(screen, BLACK, [self.x,self.y, self.width, self.height], 2)
		screen.blit(self.image,self.rect)

class attack():
	def __init__(self,image,X,Y):
		self.image=pygame.image.load (image)
		self.rect=self.image.get_rect()
		self.rect.x=X
		self.rect.y=Y
	def draw(self,image):
		self.image=pygame.image.load (image)
		# self.rect=self.image.get_rect()
		# self.rect.x=
		# self.rect.y=Y
		screen.blit(self.image,self.rect)
	def move(self):                      #Moves animations across the screen
		self.rect.x += 8

#Makes the character images
cat= character(wiz_list[0])
foe= character(foe_list[0])
count =1
fire= attack(firey_list[0],0,60)
water=attack(watery_list[0],0,130)
ice=attack(icy_list[0],0,75)

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
	screen.fill(WHITE)
	#

	#Code responsible for animations
	if count < 20:
		cat.image = wiz_list[1]
		foe.image= foe_list[1]
		fire.image=firey_list[1]
		water.image=watery_list[1]
		ice.image=icy_list[1]
		count +=1
	elif count < 40:
		cat.image = wiz_list[0]
		foe.image= foe_list[0]
		fire.image=firey_list[0]
		water.image=watery_list[0]
		ice.image=icy_list[0]
		count += 1
	if count == 39:
		count = 1

	# --- Drawing code should go here

	pygame.draw.line(screen,BLACK,[0,SCREEN_HEIGHT/2],[900,SCREEN_HEIGHT/2],1)
	#Controls attacks~~~~~~~~~~
	fires=False
	waters=False
	icies=False
	card_ele="1"

	if card_ele== "1": #Fire card wins
		fires=True
		waters=False
		icies=False
	elif card_ele=="2": #water card wins
		fires=False
		waters=True
		icies=False
	elif card_ele=="3": #ice card wins
		fires=False
		waters=False
		icies=True
	else:                #DRAW! or just waiting for move
		fires=False
		waters=False
		icies=False
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Draws characters and attacks if one is made
	if fires==True:
		cat.draw(cat.image,-50,60)
		foe.draw(foe.image,500,50)
		fire.draw(fire.image)
	elif waters==True:
		cat.draw(cat.image,-50,60)
		foe.draw(foe.image,500,50)
		water.draw(water.image)
	elif icies==True:
		cat.draw(cat.image,-50,60)
		foe.draw(foe.image,500,50)
		ice.draw(ice.image)
	else:
		cat.draw(cat.image,-50,60)
		foe.draw(foe.image,500,50)

	fire.move()
	water.move()
	ice.move()


	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
