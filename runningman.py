import pygame, sys
from pygame import *
from random import randint
import time

# set up the window
pygame.init()


FPS = 60 #frames per second setting
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Coin Jump')

white = (255,255,255)
black = (0,0,0)
green = (0, 255, 0)
blue = (0, 0, 128)
navyblue = (60,60,100)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Score', True, black, white)
textRectObj = textSurfaceObj.get_rect()
textRectObj.topleft = (20, 20)

manImg = pygame.image.load('stickman.png')
manx = 400
many = 350
direction = 'right'
spacePressed = 1
dist = 1
score = 0

# run the game loop
                                         
while True:

    DISPLAYSURF.fill(white)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.draw.rect(DISPLAYSURF,navyblue,(0,75, 999, 724), 4)

    if direction == 'right':
        manx += dist
    elif direction == 'down':
        many += dist
    elif direction == 'left':
        manx -= dist
    elif direction == 'up':
        many -= dist

    if(manx >= 970 or manx <= 0 or many >= 770 or many <= 75):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load('lose.mp3')
        pygame.mixer.music.play(0,0.01)
        time.sleep(2)
        print("YOU LOSE!")
        pygame.quit()
        sys.exit()
    
    DISPLAYSURF.blit(manImg, (manx, many))
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space is pressed")
                randInt = randint(0,3)
                if randInt == 0:
                    direction = 'right'
                elif randInt == 1:
                    direction = 'down'
                elif randInt == 2:
                    direction = 'left'
                elif randInt == 3:
                    direction = 'up'
                spacePressed += 1
                if(spacePressed%10 == 0):
                    dist += 1

    score += 1
    textSurfaceObj = fontObj.render(str(score*dist), True, black, white)
    pygame.display.update()
    fpsClock.tick(FPS)
