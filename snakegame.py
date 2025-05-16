import pygame 
import time 
import random 


#intializing the pygame 

pygame.init()

#colors 

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
yellow = (0, 255, 0)
blue = (50, 153, 213)


#screen sizes
dis_width = 800
dis_height = 600

#create the game window

dis = pygame.dispaly.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

#turning a clock to slowdown the snake

dis = pygame.time.Clock()

#Snake avatar settings

snake_block = 10
snake_speed = 15


font_style = pygame.font.SysFont("bahnschrift", 25)

#function to display the score
def Your_Score(score)
	value = fonot_Style.render("Your Score: " + str(score), True, white)
	dis.bliit(Value, [0, 0])

#function to draw a snake

def our_snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(dis, yellow, [x[0], x[1], snake_block,snake_block])


#function loop for game 

def gameLoop():
	game_over = False
	game_close = False

	x1 = dis_width / 2
	y1 = dis_height / 2

	x1_change = 0
	y1_change = 0

	snake_List = []
	Length_of_snake = 1

	foodx = round(random.randrange(0, dis_width - snake_block)/ 10.0)* 10.0
	foody = round(random.randrange(0, dis_height - snake_block)/ 10.0)* 10.0

	Whilenot game_over:
		While game_close:
		dis.fill(black)
		message = font_style.render("GAME OVER! Please press Q-QUIT or C-PLAY AGAIN", True, red)

		dis_blit(message, [dis_width / 6, dis_height/3])
		Your_Score(Length_of_snake  - 1)
		pygame.display.update()
	
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					game_over = True
					game_close = False


			if event.key == pygame.K_c:
				gameLoop()



for event in pygame.event.get():
	if event.type == pygame.QUIT:
		game_over = True
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x1_change = -snake_block
			y1_change = 0
	elif event.key == pygame.K_RIGHT:
			x1_change = snake_block
			y1_change = 0
	elif event.key == pygame.K_UP:
			y1_change = -snake_block
			x1_change = 0
	elif event.key == pygame.K_DOWN:
			y1_change = snake_block
			x1_change = 0


	if x1 >= dis_width or x1 < 0 or y1 >= dis-height or y1 < 0:
		game_close == True 

		x1 += x1_change 
		y1 += y1_change
		dis.fill(black)

	pygame.draw.rect(dis, blue,[foodx, foody, snake_block, snake_block])
	snake_Head = []
	snake_Head.append(x1)
	snake_Head.append(y1)
	snake_list.append(snake_Head)

		if len(snake_List) > Length_of_snake:
			del snake_List[0]
		for x in snake_List[:-1]:
			if x == snake_Head:
				game_close = True 

		our_snake(snake_block, snake_List)	
		Your_Score(Length_of_snake -1)

	pygame.display.update()

	if x1 == foodx and y1 == foody:
		foodx = 
		foody = 
		length_of_snake += 1

clock.tick(snake_speed)

pygame.quit()
quit()


# to start the game 

gameLoop()
