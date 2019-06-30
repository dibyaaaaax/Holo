import pygame, sys
from pygame.locals import *
from win32api import GetSystemMetrics


pygame.init()

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
w= (width - height)//2

print("h1= ", round(height*0.026458333, 2))
print("h2= ", round(width*0.1*0.026458333, 2))

black = (0, 0, 0)
white = (255, 255, 255)
green = (50, 255, 50)

cactusImg = pygame.image.load('cactus.png')
cactusHeight= 160
cactusWidth= 91
bubbleWidth = 75
cactusImg = pygame.transform.scale(cactusImg, (cactusWidth, cactusHeight))
bubble1 = pygame.image.load('bubble1.png')
bubble1 = pygame.transform.scale(bubble1, (bubbleWidth, bubbleWidth))

cactus_pos=[[width//2-cactusWidth//2, height//2-cactusHeight*2],
			[width//2-2*cactusHeight, height//2-cactusWidth//2],
			[width//2-int(0.5*cactusWidth), height//2+cactusHeight], 
			[width//2+cactusHeight, height//2-cactusWidth//2]]

gameDisplay = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption('Bubbles')

clock = pygame.time.Clock()


def boundaries(wr):
	
	# pygame.draw.line(gameDisplay, white, (w,0), (width-w, height), 3)
	# pygame.draw.line(gameDisplay, white, (w,height), (width-w, 0), 3)
	# pygame.draw.line(gameDisplay, white, (w,0), (w, height), 3)
	# pygame.draw.line(gameDisplay, white, (width-w,0), (width-w, height), 3)

	pygame.draw.rect(gameDisplay,(42, 43, 46),((width//2-wr//2),(height//2-wr//2),wr,wr), 1)

def bubble(img, x, y):
	gameDisplay.blit(img, (x, y))


def cactus1(img, x_move, y_move):
	x=cactus_pos[0][0]
	y=cactus_pos[0][1]
	cactus_pos[0][0]+=x_move
	cactus_pos[0][1]+=y_move
	gameDisplay.blit(img, (x+x_move, y+y_move))

def cactus2(img, x_move, y_move):
	x=cactus_pos[1][0]
	y=cactus_pos[1][1]
	cactus_pos[1][0]+=x_move
	cactus_pos[1][1]+=y_move
	img = pygame.transform.rotate(img, 90)
	gameDisplay.blit(img, (x+x_move, y+y_move))

def cactus3(img, x_move, y_move):
	x=cactus_pos[2][0]
	y=cactus_pos[2][1]
	cactus_pos[2][0]+=x_move
	cactus_pos[2][1]+=y_move
	img = pygame.transform.rotate(img, 180)
	gameDisplay.blit(img, (x+x_move,y+y_move))

def cactus4(img, x_move, y_move):
	x=cactus_pos[3][0]
	y=cactus_pos[3][1]
	cactus_pos[3][0]+=x_move
	cactus_pos[3][1]+=y_move
	img = pygame.transform.rotate(img, 270)
	gameDisplay.blit(img, (x+x_move,y+y_move))

def area(p1, p2, p3):
	area=abs((p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))/2)
	return area

def isInside(p, p1, p2, p3):
	A= area(p1, p2, p3)
	A1= area(p, p2, p3)
	A2= area(p1, p, p3)
	A3= area(p1, p2, p)
	return (A==A1+A2+A3)


mainLoop = True

x_move=0
y_move=0
while mainLoop:
	cactus1_x=cactus_pos[0][0]
	cactus1_y=cactus_pos[0][1]
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			mainLoop = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				mainLoop = False

		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_move = -3
			elif event.key == pygame.K_RIGHT:
				x_move = 3
			elif event.key == pygame.K_UP:
				
					y_move = -3
				
			elif event.key == pygame.K_DOWN:
				y_move = 3
			
		if event.type == pygame.KEYUP:
			x_move=0
			y_move=0
			

	if (not isInside([cactus1_x+x_move, cactus1_y+y_move], [w, 0], [width-w, 0], [width//2, height//2])
	or not isInside([cactus1_x+cactusWidth+x_move, cactus1_y+y_move], [w, 0], [width-w, 0], [width//2, height//2])
	or not isInside([cactus1_x+x_move, cactus1_y+cactusHeight+y_move], [w, 0], [width-w, 0], [width//2, height//2])
	or not isInside([cactus1_x+cactusWidth+x_move, cactus1_y+cactusHeight+y_move], [w, 0], [width-w, 0], [width//2, height//2])):
		x_move=0
		y_move=0

	gameDisplay.fill(black)
	
	boundaries(int(0.1*width))

	#bubble(bubble1, 400, 100)

	cactus1(cactusImg, x_move, y_move)
	cactus2(cactusImg, y_move, -x_move)
	cactus3(cactusImg, -x_move , -y_move)
	cactus4(cactusImg, -y_move, x_move)
	
	pygame.display.update()
	clock.tick(60)

pygame.quit()