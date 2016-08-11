import pygame
import random
from PIL import Image



logo= pygame.image.load("logo-1.png")

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
tips=["danger1.png","danger2.png","danger3.png","danger4.png"]


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
		self.rect.x += 16
	def move_left (self):
		self.rect.x-=16	
		
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
pygame.display.set_caption("Cat Cards")
pygame.display.set_icon(logo)

screen = pygame.display.set_mode([screen_width, screen_height])


elem_pics = ["watercard_final.png", "firecard_final.png", "icecard_final.png"]

black_card = 0
white_card = 0
all_elem = 0

black_card_bad = 0
white_card_bad = 0
all_elem_bad = 0

black_card_list = []
white_card_list = []
all_elem_list = []

texts = []
text_num = []

elem_track = []

text_loc = []																														#move text stuff

card_start_loc = []




def make_cards():
	global black_card
	global white_card
	global all_elem

	global black_card_bad
	global white_card_bad
	global all_elem_bad

	global black_card_list
	global white_card_list
	global all_elem_list

	global texts
	global text_num

	global elem_track

	global text_loc																														#move text stuff

	global card_start_loc
	
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
	text_num = []

	elem_track = []

	text_loc = []																														#move text stuff

	card_start_loc = []
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
		text_num.append(card_num_rand)
		
		card_start_loc.append([card.rect.x,card.rect.y])
		
		
	card_num_rand_bad = random.randint(1,3)                                                #init enemy card
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
	text = font.render(str(card_num_rand_bad), True, BLACK)
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
	text_num.append(card_num_rand_bad)
		
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
	
def bad_set_attack():
	elem = elem_track[7]
	global fire_foe
	global water_foe
	global ice_foe
	print(elem)
	if elem == "fire":
		fire_foe = True
		f_fire.rect.x = 600
		f_fire.rect.y =60
	elif elem == "water":
		water_foe = True
		f_water.rect.x =600
		f_water.rect.y =130
	elif elem == "ice":
		ice_foe = True
		f_ice.rect.x = 600
		f_ice.rect.y =60
	
def tie_breaker():
	global tie_display
	tie_display = True
	
def card_move_back():
	global bad_show
	print("In this function")
	
	black_card_list[which_one].rect.x = card_start_loc[which_one][0]
	black_card_list[which_one].rect.y = card_start_loc[which_one][1]
	
	card_num_rand = random.randint(1,3)
	font = pygame.font.Font("C:\Windows\Fonts\ARDELANEY.TTF", 25)
	text = font.render(str(card_num_rand), True, BLACK)
	texts[which_one] = text
	text_num[which_one] = card_num_rand
	
	elem_pic = elem_pics[random.randint(1,3) - 1]
	if elem_pic == "firecard_final.png":
		elem_track[which_one] = "fire"
		
	elif elem_pic == "watercard_final.png":
		elem_track[which_one] = "water"
		
	elif elem_pic == "icecard_final.png":
		elem_track[which_one] = "ice"
	all_elem_list[which_one].image =  pygame.image.load(elem_pic)
	print(card_num_rand)
	print(elem_track[which_one])
	
	
	black_card_list[7].rect.x = card_start_loc[7][0]
	black_card_list[7].rect.y = card_start_loc[7][1]
	
	card_num_rand_bad = random.randint(1,3)
	font = pygame.font.Font("C:\Windows\Fonts\ARDELANEY.TTF", 25)
	text = font.render(str(card_num_rand_bad), True, BLACK)
	texts[7] = text
	text_num[7] = card_num_rand_bad
	
	elem_pic = elem_pics[random.randint(1,3) - 1]
	if elem_pic == "firecard_final.png":
		elem_track[7] = "fire"
		
	elif elem_pic == "watercard_final.png":
		elem_track[7] = "water"
		
	elif elem_pic == "icecard_final.png":
		elem_track[7] = "ice"
	all_elem_list[7].image =  pygame.image.load(elem_pic)
	print(card_num_rand_bad)
	print(elem_track[7])
	bad_show = False
	
def bad_card_move():
	global bad_moving
	black_card_list[7].rect.y -=1
	if black_card_list[7].rect.y == 50:
		bad_moving =False
		who_wins()
		
def who_wins():
	bad_elem = elem_track[7]
	good_elem = elem_track[which_one]
	bad_num = text_num[7]
	good_num = text_num[which_one]
	if bad_elem == "fire":
		if good_elem == "ice":
			bad_set_attack()
			print(str(bad_num), str(good_num))
		elif good_elem == "water":
			set_attack()
			print(str(bad_num), str(good_num))
		elif good_elem == "fire":
			if bad_num > good_num: 
				bad_set_attack()
				print(str(bad_num), str(good_num))
			elif bad_num < good_num:
				set_attack()
				print(str(bad_num), str(good_num))
			else:
				print(str(bad_num), str(good_num))
				tie_breaker()
	if bad_elem == "water":
		if good_elem == "fire":
			bad_set_attack()
			print(str(bad_num), str(good_num))
		elif good_elem == "ice":
			set_attack()
			print(str(bad_num), str(good_num))
		elif good_elem == "water":
			if bad_num > good_num: 
				bad_set_attack()
				print(str(bad_num), str(good_num))
			elif bad_num < good_num:
				set_attack()
				print(str(bad_num), str(good_num))
			else:
				print(str(bad_num), str(good_num))
				tie_breaker()
	if bad_elem == "ice":
		if good_elem == "water":
			bad_set_attack()
			print(str(bad_num), str(good_num))
		elif good_elem == "fire":
			set_attack()
			print(str(bad_num), str(good_num))
		elif good_elem == "ice":
			if bad_num > good_num: 
				bad_set_attack()
				print(str(bad_num), str(good_num))
			elif bad_num < good_num:
				set_attack()
				print(str(bad_num), str(good_num))
			else:
				print(str(bad_num), str(good_num))
				tie_breaker()
	
				
done = False

clock = pygame.time.Clock()

make_cards()

can_restart = False


start= pygame.image.load("startscreen.png")
background =pygame.image.load ("bg.png")
instructions=pygame.image.load("howto.png")
win= pygame.image.load("win.png")
lose=pygame.image.load("lose.png")
tippy=pygame.image.load(tips[random.randint(0,len(tips)-1)])
thank_you = pygame.image.load("friends.png")
tiny_logo = pygame.image.load("playlogo.png")

bad_show = False

fires=False
waters=False
icies=False
fire_foe=False
water_foe=False
ice_foe=False

score = 0
enemy_score = 0
for num in text_num:
	print(num)

tie_count = 0
tie_display = False
	
howto=False
start_game = False
tips_screen=False
start_screen = True
you_win = False
you_lose = False
thanks = False
click_delay = 0
	
font = pygame.font.SysFont("monospace", 20, True, False)		
text_click_to_continue = font.render ("click anywhere to continue", True, BLACK)
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(WHITE)
	#--------------------------------------------------------------------------------
	
	if start_screen == True:
		screen.blit(start, [0,0])
		mouse_pressed=pygame.mouse.get_pressed()
		if mouse_pressed== (1,0,0):
			howto=True
			start_screen = False
	if howto == True:
		screen.blit(instructions, [0,0])
		screen.blit(text_click_to_continue, [10,570])
		mouse_pressed=pygame.mouse.get_pressed()
		click_delay += 1
		if mouse_pressed== (1,0,0) and click_delay > 10:
			tips_screen=True
			howto=False
			click_delay =0
			print("intros")
	if tips_screen == True:
		screen.blit(tippy, [0,0])
		screen.blit(text_click_to_continue, [10,570])
		mouse_pressed=pygame.mouse.get_pressed()
		click_delay += 1
		if mouse_pressed== (1,0,0) and click_delay > 10:
			tips_screen=False
			start_game = True
			click_delay =0
			print("intros")	
	
	
	
	
	#--------------------------------------------------------------------------------------------
	if start_game == True:                                      #Starts actual game
		screen.blit(background,[0,0])
		screen.blit(tiny_logo,[0,0])
		
		if count < 10: 																							#animates the switching pics
			cat.image = wiz_list[1]
			foe.image= foe_list[1]
			fire.image=firey_list[1]
			water.image=watery_list[1]
			ice.image=icy_list[1]
			f_fire.image=foe_fire[1]
			f_water.image=foe_water[1]
			f_ice.image=foe_ice[1]
			count +=1
		elif count < 20:
			cat.image = wiz_list[0]
			foe.image= foe_list[0]
			fire.image=firey_list[0]
			water.image=watery_list[0]
			ice.image=icy_list[0]
			f_fire.image=foe_fire[0]
			f_water.image=foe_water[0]
			f_ice.image=foe_ice[0]
			count += 1
		if count == 19:
			count = 1	
		
		#pygame.draw.line(screen,BLACK,[0,SCREEN_HEIGHT/2],[900,SCREEN_HEIGHT/2],1)
		font = pygame.font.SysFont("monospace", 20, True, False)
		font_tie = pygame.font.SysFont("monospace", 40, True, False)
		text_score = font.render ("Your score:" + str(score), True, BLACK)
		text_enemy_score = font.render ("Enemy score:" + str(enemy_score), True, BLACK)
		text_tie = font_tie.render ("Tie", True, BLACK)
		
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
				fires = False
				score +=1
		if waters == True and water.rect.x<900:
			water.move()
			water.draw(water.image)
			if water.rect.x > 875:
				card_move_back()
				waters = False
				score +=1
		if icies == True and ice.rect.x<900:
			ice.move()
			ice.draw(ice.image)
			if ice.rect.x > 875:
				card_move_back()
				icies = False
				score +=1
		if fire_foe == True and f_fire.rect.x >-100:                                              #foe attacks move
			f_fire.move_left()
			f_fire.draw(f_fire.image)
			if f_fire.rect.x <-75:
				card_move_back()
				fire_foe = False
				enemy_score +=1
		if water_foe == True and f_water.rect.x>-100:
			f_water.move_left()
			f_water.draw(f_water.image)
			if f_water.rect.x < -75:
				card_move_back()
				water_foe = False
				enemy_score +=1
		if ice_foe ==True and f_ice.rect.x>-100:
			f_ice.move_left()
			f_ice.draw(f_ice.image)
			if f_ice.rect.x < -75:
				card_move_back()
				ice_foe = False
				enemy_score +=1
		
		
		#----------------------------------------------------------------------------------------
		
		black_card.draw(screen)
		white_card.draw(screen)
		all_elem.draw(screen)
		for i in range(7):
			screen.blit(texts[i], text_loc[i])
		
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
			card_attatch()
			bad_card_move()
			card_attatch()
			bad_card_move()
			card_attatch()
			bad_card_move()
			card_attatch()
			bad_card_move()
			card_attatch()
			bad_card_move()
			card_attatch()
			
			
		
		mouse_pressed = pygame.mouse.get_pressed()
		if mouse_pressed ==(1, 0, 0):
			#print("weee")
			moving = which_card()
		
		
		
		
		screen.blit(text_score, [10,5])
		screen.blit(text_enemy_score, [600,5])
		if tie_display == True:
			if tie_count <30:
				screen.blit(text_tie, [400,100])
				tie_count +=1
			elif tie_count>=30:
				print("in false conditional")
				card_move_back()
				tie_display = False
				tie_count = 0
		if score == 10:  																									#lwkjre;lkj;
			start_game = False
			you_win = True
			click_delay = 0
		if enemy_score == 10:
			start_game = False
			you_lose = True
			click_delay = 0
	if you_win == True:
		screen.blit(win, [0,0])
		click_delay += 1
		if click_delay > 60:
			thanks = True
			you_win = False
			click_delay =0
			
	if you_lose == True:
		screen.blit(lose, [0,0])
		click_delay += 1
		if click_delay > 60:
			thanks = True
			you_lose = False
			click_delay =0
	
	if thanks == True:
		screen.blit(thank_you, [0,0])
		mouse_pressed=pygame.mouse.get_pressed()
		click_delay += 1
		if mouse_pressed== (1,0,0) and click_delay > 10:
			thanks = False
			tips_screen=True
			click_delay =0
			score = 0
			enemy_score = 0
			make_cards()
			tippy=pygame.image.load(tips[random.randint(0,len(tips)-1)])
	
	pygame.display.flip()
	
	# Limit to 60 frames per second
	clock.tick(60)

pygame.quit()
exit()