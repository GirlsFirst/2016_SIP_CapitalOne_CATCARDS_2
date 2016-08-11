import pygame
import random
from PIL import Image


BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED =(255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

speed = 2

screen_width = 800
screen_height = 600


#character animation frame lists
wiz_list = ["WIZ.png", "WIZ2.png"]
foe_list=["foe.png","foe2.png"]
firey_list=["fiery1.png", "fiery2.png"]
watery_list=["watery1.png", "watery2.png"]
icy_list=["icy1.png","icy2.png"]
speed=2


class Card(pygame.sprite.Sprite):
	def __init__(self,image,width, height, color):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		#self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.rect.x = screen_width
		self.rect.y = screen_height
		
		
	def update(self):
		self.rect = self.image.get_rect()
		screen.blit(self.image, self.rect)
		
class Elem(pygame.sprite.Sprite):
	def __init__(self,image):
		super().__init__()
		#self.image = pygame.Surface([width, height])
		#self.image.fill(color)
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.rect.x = screen_width
		self.rect.y = screen_height
		
		

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


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
 
pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])

card = Card("dot.png", 75, 125, BLACK)

elem_pics = ["watercard_final.png", "firecard_final.png", "icecard_final.png"]

black_card = pygame.sprite.Group()
white_card = pygame.sprite.Group()
all_elem = pygame.sprite.Group()


black_card_list = []
white_card_list = []
all_elem_list = []

texts = []

elem_track = []

text_loc = []																														#move text stuff

def make_cards():
	current_width = 40
	for i in range(7):
		card_num_rand = random.randint(1,3)
		elem_pic = elem_pics[random.randint(1,3) - 1]
		if elem_pic == "firecard_final.png":
			elem_track.append("fire")
		elif elem_pic == "watercard_final.png":
			elem_track.append("water")
		elif elem_pic == "icecard_final.png":
			elem_track.append("ice")
		
		card = Card("dot.png", 80, 125,BLACK)
		white = Card("dot.png", 65, 110, WHITE)
		elem = Elem(elem_pic)
		
		card.rect.x = current_width + 15
		card.rect.y = screen_height - screen_height//3
		
		white.rect.x = card.rect.x + 7
		white.rect.y = card.rect.y + 7
		
		elem.rect.x = card.rect.x - 40
		elem.rect.y = card.rect.y - 62
		
		font = pygame.font.Font("C:\Windows\Fonts\ARDELANEY.TTF", 25)
		text = font.render(str(card_num_rand), True, BLACK)
		location = [(white.rect.x + 50),(card.rect.y + 7)]
		
		current_width +=100
		
		black_card.add(card)
		white_card.add(white)
		all_elem.add(elem)
		
		black_card_list.append(card)
		white_card_list.append(white)
		all_elem_list.append(elem)
		
		texts.append(text)
		text_loc.append(location)
		
		
		
		
		
	
def card_attatch():
	for i in range(7):
		x_base = black_card_list[i].rect.x
		y_base = black_card_list[i].rect.y
		
		white_card_list[i].rect.x = x_base + 7
		white_card_list[i].rect.y = y_base + 7
		
		if elem_track[i]== "fire":
			all_elem_list[i].rect.x = x_base - 50
			all_elem_list[i].rect.y = y_base - 30
			
		elif elem_track[i] == "water":
			all_elem_list[i].rect.x = x_base - 30
			all_elem_list[i].rect.y = y_base - 5
			
		else:
			all_elem_list[i].rect.x = x_base - 30
			all_elem_list[i].rect.y = y_base - 10

		
		text_loc[i] = [(x_base + 57),(y_base + 7)]
		
		
		
done = False

clock = pygame.time.Clock()

make_cards()

can_restart = False

print (all_elem_list[1])
print (elem_track)



while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(WHITE)
	
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

	
	black_card.draw(screen)
	white_card.draw(screen)
	all_elem.draw(screen)
	#pygame.draw.rect(screen, WHITE, all_card.rect)
	
	card_attatch()
	
	
	
	for i in range(7):
		screen.blit(texts[i-1], text_loc[i-1])
	
	
	
	pygame.display.flip()
 
	# Limit to 60 frames per second
	clock.tick(60)

pygame.quit()
exit()