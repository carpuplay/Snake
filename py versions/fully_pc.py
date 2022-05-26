# Créé par acarp, le 26/04/2022 avec EduPython
#serpiente taca taca
from pygame import mixer
import time
from pygame.locals import *
import pygame
import random
from os import path

pygame.init()
mixer.init()
mixer.music.set_volume(100)
#color definition
black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)
white = pygame.Color(255,255,255)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
violet= pygame.Color(255,0,255)

#display settings
display=pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
x,y=display.get_size()
print(x,y)
dis_width=x
dis_height=y

pygame.display.update()
pygame.display.set_caption('Snake by Carpu')
logo = pygame.image.load('logeo.jpg')
pygame.display.set_icon(logo)

starttime=time.time()
  #run clock
clock=pygame.time.Clock()

snake_block=10  #snake
snake_speed=120

# message system
font_style = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

#score display
def Your_score(score):                                                            #show score
    value = font_style.render("Your Score: " + str(score), True, white )
    display.blit(value, [0, 0])
#messages display
def message(msg,color,x,y):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x, y])
#image display
def img_disp(img,x,y):
    imag=pygame.image.load(img)
    display.blit(imag,[x,y])


def message_p(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width/4, dis_height/2])
#save the best score in a txt file
with open(".\scorelog.txt","r") as f:
    highscore = f.read()

def show_highscore(x,y,score):
    with open(".\scorelog.txt","r") as f:
        highscore = f.read()
    Hiscore_text = font_style.render('Best Score :' + str(highscore),True,(255,0,0))
    display.blit (Hiscore_text,(x,y))

def gameLoop():  # creating a function
    game_over = False #when the game is in progress, the game is not stopped or closed
    game_close = False
    run=True 
    while not game_over: 
        game_over = False #when the game is in progress, the game is not closed
        game_close = False #when the game is in progress, the game is not stopped
        game_pause = False #when the game is in progress, the game is not in pause
        x1 = dis_width / 2 #initials coordinates of the snake in the middle of the game area.
        y1 = dis_height / 2
        fscore=[] #score list
        snake_List=[] #position of all part of the snake
        Lenght_of_snake=1 #initil lenght of the snake
        maz=0 #

        pygame.display.update()
        sre=8 #variables
        ml=10
        mlt=10
        x1_change = 0 #initial movememt of the snake. he don't moove
        y1_change = 0
        
        #The coordinates of the food that appear randomly in the game area
        foodx = round(random.randrange(0, dis_width - snake_block)/10)*10 
        foody = round(random.randrange(0, dis_height - snake_block)/10)*10
        foodx2 = round(random.randrange(0, dis_width - snake_block)/10)*10
        foody2 = round(random.randrange(0, dis_height - snake_block)/10)*10
        while not game_over:
            while game_close==True: #while loop when the player 
                display.fill(black) #black screen display
                message("You Lost! Press Q-Quit or C-Play Again", red,640,360) #lost message display
                img_disp('100.jpg',825,200) #lost image display
                Your_score(maz) #scpore display
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN: 
                        if event.key == pygame.K_q: #if the player press "q" key, the game is closed
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c: #if the player press "c"key, the game loop in lauched and anothe game begins.
                            gameLoop()

            if game_close == True: 
                fscore.append(maz)

            for event in pygame.event.get():              # keys to keyboard
                if event.type==QUIT:
                        game_over==True
                if event.type == pygame.KEYDOWN: #if the keydow is pressed, the snake goes down
                    if event.key == pygame.K_DOWN:
                       x1_change=0
                       y1_change=(snake_block-sre)
                    elif event.key == pygame.K_UP: #if the keyup is pressed, the snake goes up
                        x1_change=0
                        y1_change=-(snake_block-sre)
                    elif event.key == pygame.K_RIGHT: #if the keyright is pressed, the snake goes right
                        x1_change=(snake_block-sre)
                        y1_change=0
                    elif event.key == pygame.K_LEFT: #if the keyleft is pressed, the snake goes left
                        x1_change=-(snake_block-sre)
                        y1_change=0
                    elif event.key == pygame.K_p: #if the key "p" is pressed, the game is paused.
                            game_pause = True
           
          #while loop when the game is paused
            while game_pause == True:
                clock.tick(0) #the mouvement stops
                display.fill(black) #black screen display
                message_p("You paused the game// press 'P' to continue or 'Q' to quit", red) #pause message display
                Your_score(maz)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p: #if the player press "p" key a counter of 3 secpond is launched to have time to get ready
                            display.fill(black)
                            message_p("3", red)
                            pygame.display.update()
                            pygame.time.wait(1000)
                            display.fill(black)
                            message_p("2", red)
                            pygame.display.update()
                            pygame.time.wait(1000)
                            display.fill(black)
                            message_p("1", red)
                            pygame.display.update()
                            pygame.time.wait(1000)
                            game_pause = False
                        elif event.key == pygame.K_q: #but if the player press "q" key, the game is closed
                            pygame.quit()

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #if the snake touches the edges of the area, the player loses
                game_close = True

            x1+=x1_change #mouvement of the snake
            y1+=y1_change
            display.fill(black)
            
            #food and snake display which were not graphic elements
            pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
            pygame.draw.rect(display, green, [x1, y1, snake_block, snake_block])
            pygame.draw.rect(display, violet, [foodx2, foody2, snake_block, snake_block])
            snake_Head=[]
            snake_Head.append(x1) #elongation of the snake
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List)>Lenght_of_snake:
                del snake_List[0]
            #when the head of the snake touches his body, the game is lost
            for x in snake_List[:-1]: 
                if x == snake_Head:
                    game_close = True
            our_snake(snake_block,snake_List)
            Your_score(maz)
            pygame.display.update()
            
            #when the snake's head touches the food, the lenght of the snake increase by 10 and the score increase by 1
            if abs(x1-foodx) <=7 and abs(y1-foody) <=7 :
                foodx = round(random.randrange(0, dis_width - snake_block)/ml)*mlt
                foody = round(random.randrange(0, dis_height - snake_block)/ml)*mlt
                Lenght_of_snake+=8
                maz+=1

            if abs(x1-foodx2) <=7 and abs(y1-foody2) <=7 :
                foodx2 = round(random.randrange(0, dis_width - snake_block)/mlt)*mlt
                foody2 = round(random.randrange(0, dis_height - snake_block)/mlt)*mlt
                Lenght_of_snake+=8
                maz+=1
            
            #if the player loses, the lost music is played
            if game_close==True:
                pygame.mixer.music.load('dark.mp3')
                pygame.mixer.music.play(start=0.2)
            if game_pause==False and game_close==False: #if the game is in progress, a music is played
                pygame.mixer.music.load('halo.mp3')
                pygame.mixer.music.play(start=4.0)


            clock.tick(60) #the fps
    pygame.quit()
    quit()
gameLoop()








