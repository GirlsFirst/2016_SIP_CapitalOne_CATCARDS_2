import pygame
import random
from PIL import Image

moving = False
bad_moving = False

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED =(255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

speed = 2

screen_width = 800
screen_height = 600

good_final_x = 300								#enter final x
good_final_y = 200								#enter final y

#character animation frame lists
wiz_list = ["WIZ.png", "WIZ2.png"]
foe_list=["foe.png","foe2.png"]
firey_list=["fiery1.png", "fiery2.png"]
watery_list=["watery1.png", "watery2.png"]
icy_list=["icy1.png","icy2.png"]
foe_fire=["foefiery1.png","foefiery2.png"]
foe_water=["foewatery1.png","foewatery2.png"]
foe_ice=["foeicy1.png","foeicy2.png"]


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
		
	def move(self):
		good_final_x = 200								#enter final x
		good_final_y = 50	
		#print("loopy")
		#self.rect = self.image.get_rect()
		global moving
		global elem_in_play
		global bad_show
		global bad_moving
		if self.rect.x < good_final_x:
			self.rect.x += 1
		elif self.rect.x > good_final_x:
			self.rect.x -=1
			
		if self.rect.y < good_final_y:
			self.rect.y += 1
		elif self.rect.y > good_final_y:
			self.rect.y -= 1
		
		if self.rect.y == good_final_y and self.rect.x == good_final_x:
			moving = False
			#set_attack()
			bad_show = True
			bad_moving = True
			
		
		
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
	def move_left (self):
		self.rect.x-=8		
		
#Makes the character images
cat= character(wiz_list[0])
foe= character(foe_list[0])
count =1
fire= attack(firey_list[0],-100,-100)          #player attacks
water=attack(watery_list[0],-100,-100)
ice=attack(icy_list[0],-100,-100)

f_fire=attack(foe_fire[0],-100,-100)         #foe attacks
f_water=attack(foe_water[0],-100,-100)
f_ice=attack(foe_ice[0],-100,-100)

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
		
pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])


elem_pics = ["watercard_final.png", "firecard_final.png", "icecard_final.png"]

black_card = pygame.sprite.Group()
white_card = pygame.sprite.Group()
all_elem = pygame.sprite.Group()

black_card_bad = pygame.sprite.Group()
white_card_bad = pygame.sprite.Group()
all_elem_bad = pygame.sprite.Group()

black_card_list = []
white_card_list = []
all_elem_list = []

texts = []

elem_track = []

text_loc = []																														#move text stuff

card_start_loc = []




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
		
		card_start_loc.append([card.rect.x,card.rect.y])
		
		
	card_num_rand = random.randint(1,3)                                                #init enemy card
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
	
	card.rect.x = 550
	card.rect.y = 200
	
	white.rect.x = card.rect.x + 7
	white.rect.y = card.rect.y + 7
		
	elem.rect.x = card.rect.x - 40
	elem.rect.y = card.rect.y - 62
		
	font = pygame.font.Font("C:\Windows\Fonts\ARDELANEY.TTF", 25)
	text = font.render(str(card_num_rand), True, BLACK)
	location = [(white.rect.x + 50),(card.rect.y + 7)]
		
	current_width +=100
		
	black_card_bad.add(card)
	white_card_bad.add(white)
	all_elem_bad.add(elem)
		
	black_card_list.append(card)
	white_card_list.append(white)
	all_elem_list.append(elem)
		
	texts.append(text)
	text_loc.append(location)
		
	card_start_loc.append([card.rect.x,card.rect.y])
		
def card_attatch():
	for i in range(8):
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
	
which_one = 0
		
def which_card():
	#print("lala")
	mouse_pos = pygame.mouse.get_pos()                             #mouse_pos is a list of [x,y]
	# if mouse_pos[0] < x_max and mouse_pos[0] > x_min:
		# if mouse_pos[1] < y_max and mouse_pos[1] > y_min:
			# which_one = i
			# move = True
	global which_one
	for i in range(7):
		
		#mouse_pos = pygame.mouse.get_pos()                             #mouse_pos is a list of [x,y]
		x_min = black_card_list[i].rect.x
		y_min = black_card_list[i].rect.y
		x_max = x_min + 80
		y_max = y_min + 125
		
		if mouse_pos[0] < x_max and mouse_pos[0] > x_min:
			if mouse_pos[1] < y_max and mouse_pos[1] > y_min:
				which_one = i
				return (True)
				# if moving == True:
					# print ("fire")

def set_attack():
	elem = elem_track[which_one]
	global fires
	global waters
	global icies
	print(elem)
	if elem == "fire":
		fires = True
		fire.rect.x = 0
		fire.rect.y =60
	elif elem == "water":
		waters = True
		water.rect.x =0
		water.rect.y =130
	elif elem == "ice":
		icies = True
		ice.rect.x = 0
		ice.rect.y =75
	
def card_move_back():
	black_card_list[which_one].rect.x = card_start_loc[which_one][0]
	black_card_list[which_one].rect.y = card_start_loc[which_one][1]
	
	card_num_rand = random.randint(1,3)
	font = pygame.font.Font("C:\Windows\Fonts\ARDELANEY.TTF", 25)
	text = font.render(str(card_num_rand), True, BLACK)
	texts[which_one] = text
	
	elem_pic = elem_pics[random.randint(1,3) - 1]
	if elem_pic == "firecard_final.png":
		elem_track[which_one] = "fire"
		
	elif elem_pic == "watercard_final.png":
		elem_track[which_one] = "water"
		
	elif elem_pic == "icecard_final.png":
		elem_track[which_one] = "ice"
	all_elem_list[which_one].image =  pygame.image.load(elem_pic)
	
def bad_card_move():
	global bad_moving
	black_card_list[7].rect.y -=1
	if black_card_list[7].rect.y == 50:
		bad_moving =False
		

done = False

clock = pygame.time.Clock()

make_cards()

can_restart = False

bad_show = False

fires=False
waters=False
icies=False
fire_foe=False
water_foe=False
ice_foe=False


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(WHITE)
	
	if count < 20: 																							#animates the switching pics
		cat.image = wiz_list[1]
		foe.image= foe_list[1]
		fire.image=firey_list[1]
		water.image=watery_list[1]
		ice.image=icy_list[1]
		f_fire.image=foe_fire[1]
		f_water.image=foe_water[1]
		f_ice.image=foe_ice[1]
		count +=1
	elif count < 40:
		cat.image = wiz_list[0]
		foe.image= foe_list[0]
		fire.image=firey_list[0]
		water.image=watery_list[0]
		ice.image=icy_list[0]
		f_fire.image=foe_fire[0]
		f_water.image=foe_water[0]
		f_ice.image=foe_ice[0]
		count += 1
	if count == 39:
		count = 1	
	
	score=100
	pygame.draw.line(screen,BLACK,[0,SCREEN_HEIGHT/2],[900,SCREEN_HEIGHT/2],1)
	font = pygame.font.SysFont("monospace", 20, True, False)
	text_score = font.render ("Your score:" + str(score), True, BLACK)
	text_enemy_score = font.render ("Enemy score:", True, BLACK)
	
	
	#Controls attacks and resets them for next round~~~~~~~~~~
	# fires=False
	# waters=False
	# icies=False
	# fire_foe=False
	# water_foe=False
	# ice_foe=False
	# card_ele="1"

	# if card_ele== "1": #player fire card wins
		# fires=True
	# elif card_ele=="2": #player water card wins
		# waters=True
	# elif card_ele=="3": #player ice card wins
		# icies=True
	# elif card_ele=="4": #Opponents fire card wins
		# fire_foe=True
	# elif card_ele=="5":  #Opponents water card wins
		# water_foe=True  
	# elif card_ele=="6":   #Opponents ice card wins
		# ice_foe=True    
		
	# else:                #DRAW! or just waiting for move
		# fires=False
		# waters=False
		# icies=False
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Draws characters and attacks if one is made

	cat.draw(cat.image,-50,60)
	foe.draw(foe.image,500,50)
	
	#Stops the animation in the background once it happens
	if fires == True and fire.rect.x <900:						 #cat attacks move
		fire.move()
		fire.draw(fire.image)
		if fire.rect.x > 875:
			card_move_back()
	
	if waters == True and water.rect.x<900:
		water.move()
		water.draw(water.image)
		if water.rect.x > 875:
			card_move_back()
		
	if icies == True and ice.rect.x<900:
		ice.move()
		ice.draw(ice.image)
		if ice.rect.x > 875:
			card_move_back()

		
		
		
	if fire_foe == True and f_fire.rect.x >-100:                                              #foe attacks move
		f_fire.move_left()
		f_fire.draw(f_fire.image)
		
	if water_foe == True and f_water.rect.x>-100:
		f_water.move_left()
		f_water.draw(f_water.image)
		
	if ice_foe ==True and f_ice.rect.x>-100:
		f_ice.move_left()
		f_ice.draw(f_ice.image)
	
	
	
	#----------------------------------------------------------------------------------------
	
	black_card.draw(screen)
	white_card.draw(screen)
	all_elem.draw(screen)
	
	if bad_show == True:
		black_card_bad.draw(screen)
		white_card_bad.draw(screen)
		all_elem_bad.draw(screen)
		screen.blit(texts[7], text_loc[7])
	#pygame.draw.rect(screen, WHITE, all_card.rect)
	
	card_attatch()
	
	if moving == True:
		black_card_list[which_one].move()
		card_attatch()
		black_card_list[which_one].move()
		card_attatch()
		black_card_list[which_one].move()
		card_attatch()
		black_card_list[which_one].move()
		card_attatch()	
		
	if bad_moving == True:
		bad_card_move()
		card_attatch
		bad_card_move()
		card_attatch
		bad_card_move()
		card_attatch
		
		
	
	mouse_pressed = pygame.mouse.get_pressed()
	if mouse_pressed ==(1, 0, 0):
		#print("weee")
		moving = which_card()
	
	for i in range(7):
		screen.blit(texts[i], text_loc[i])
	
	
	screen.blit(text_score, [10,5])
	screen.blit(text_enemy_score, [600,5])
	
	pygame.display.flip()
	
	# Limit to 60 frames per second
	clock.tick(60)

pygame.quit()
exit()