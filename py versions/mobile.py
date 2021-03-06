#Created by Carpu

#import all the modules used
import time
from pygame.locals import *
import pygame
import random
from os import path

#run pygame
pygame.init()

#color definition
black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)
white = pygame.Color(255,255,255)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
violet= pygame.Color(255,0,255)

#display settings
display=pygame.display.set_mode((2400,1080))
x,y=display.get_size()
print(x,y)
dis_width=x
dis_height=y

#setting captoin name
pygame.display.update()
pygame.display.set_caption('Snake by Carpu')

#clock settings
starttime=time.time()
clock=pygame.time.Clock()

#snake definition
snake_block=30  #snake
snake_speed=120

# font feature
font_style = pygame.font.SysFont(None, 50)

#snake draw and display feature
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

#score display feature
def Your_score(score):                                                            #show score
    value = font_style.render("Your Score: " + str(score), True, white )
    display.blit(value, [0, 0])

#on screen general purpose displaying feature
def message(msg,color,x,y):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x, y])

#specific pause message display
def message_p(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width/7, dis_height/2])

direction='none'   #variable used for tactile controls

def gameLoop():  # creating a function
    game_over = False      #when the game is in progress, the game is not stopped or closed
    game_close = False
    while not game_over:   #main gameover loop
        game_close = False    #when the game is in progress, the game is not stopped or closed
        game_pause = False    
        x1 = dis_width / 2   #when the game is in progress, the game is not stopped or closed
        y1 = dis_height / 2
        snake_List=[]        #list with all snake positions in screen
        Lenght_of_snake=1    #initial length of the snake
        maz=0
        ml=10
        sre=25
        
        #up=pygame.draw.rect(display, green, [dis_width/2,400,80,80])           #tactile controls, but discarted because of 
        #down=pygame.draw.rect(display, green, [dis_width/2,400,80,80])
        #left=pygame.draw.rect(display, green, [490,400,80,80])                    
        #right=pygame.draw.rect(display, green, [590,400,80,80])
        #pause_bt=pygame.draw.rect(display,red,[650,400,80,80])
        #pygame.display.update()

        x1_change = 0        #snake movement variables
        y1_change = 0

        #The coordinates of the food that appear randomly in the game area
        foodx = round(random.randrange(0, dis_width - snake_block)/ml)*ml
        foody = round(random.randrange(0, 1450 - snake_block)/ml)*ml
        foodx2 = round(random.randrange(0, dis_width - snake_block)/ml)*ml
        foody2 = round(random.randrange(0, 1450 - snake_block)/ml)*ml
        while not game_over:
            while game_close==True: #activation of the loop when the player loses
                display.fill(black)
                message("You Lost! Press Q-Quit or C-Play Again", red,320,360)
                Your_score(maz)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:      #if the player press "q" key, the game is closed
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:      #if the player press "c"key, the game loop in lauched and anothe game begins.
                            gameLoop()

            if game_close == True:
                fscore.append(maz)

            for event in pygame.event.get():              # keys to keyboard
                if event.type==QUIT:
                        game_over==True
                if event.type == pygame.KEYDOWN:      
                    if event.key == pygame.K_s:    #if the key s is pressed, the snake goes down
                        x1_change=0
                        y1_change=(snake_block-sre)
                    elif event.key == pygame.K_w:     #if the key w is pressed, the snake goes up
                        x1_change=0
                        y1_change=-(snake_block-sre)
                    elif event.key == pygame.K_d:     #if the key d is pressed, the snake goes right
                        x1_change=(snake_block-sre)
                        y1_change=0
                    elif event.key == pygame.K_a:     #if the keyleft is pressed, the snake goes left
                        x1_change=-(snake_block-sre)
                        y1_change=0
                    elif event.key == pygame.K_p: #if the key "p" is pressed, the game is paused.
                        game_pause = True
            
            while game_pause == True:       #pause loop activation
                clock.tick(0)          #stops the snake movement in order to keep the snake in the same conditions as before the pause
                display.fill(black)
                message_p("You paused the game// press green to continue or red to quit", red)    #pause message display
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
                    elif event.key == pygame.K_q:     #but if the player press "q" key, the game is closed
                        pygame.quit()

            if x1 >= dis_width or x1 < 0 or y1 >= 1450 or y1 < 0:   #compares the position of the head of the snake with the limits of the game
                game_close = True  #when the track limits are exeed, the game is done      

            x1+=x1_change     #updates the new position of the head by adding the movement variable to the position of head. 
            y1+=y1_change
            display.fill(black)
            
            #food and snake display which were not graphic elements
            pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
            pygame.draw.rect(display, green, [x1, y1, snake_block, snake_block])
            pygame.draw.rect(display, violet, [foodx2, foody2, snake_block, snake_block])
            snake_Head=[]
            snake_Head.append(x1)   #new position of the head
            snake_Head.append(y1)
            snake_List.append(snake_Head)    #update of the snake list
            if len(snake_List)>Lenght_of_snake:   #used to solve a bug
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
            our_snake(snake_block,snake_List)
            Your_score(maz)
            pygame.display.update()

            if abs(x1-foodx) <=15  and abs(y1-foody) <=15:
                foodx = round(random.randrange(0, dis_width - snake_block)/30)*30
                foody = round(random.randrange(0, 1450 - snake_block)/30)*30
                Lenght_of_snake+=8
                maz+=1
            if abs(x1-foodx2) <=15  and abs(y1-foody2) <=15:
                foodx2 = round(random.randrange(0, dis_width - snake_block)/30)*30
                foody2 = round(random.randrange(0, 1450 - snake_block)/30)*30
                Lenght_of_snake+=8
                maz+=1

            clock.tick(60)
    pygame.quit()
    quit()
gameLoop()
