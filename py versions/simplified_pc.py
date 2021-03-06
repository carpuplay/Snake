# Créé par acarp, le 26/04/2022 avec EduPython
#serpiente taca taca
from logging import makeLogRecord
import time
from pygame.locals import *
import pygame
import random
from os import path
#from setings import *


pygame.init()

black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)
white = pygame.Color(255,255,255)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
violet= pygame.Color(255,0,255)

#display settings

display=pygame.display.set_mode((1280,720))
x,y=display.get_size()
print(x,y)
dis_width=x
dis_height=y

pygame.display.update()
pygame.display.set_caption('Snake by Carpu')

starttime=time.time()
  #run clock
clock=pygame.time.Clock()

snake_block=20  #snake
snake_speed=120

# message system
font_style = pygame.font.SysFont(None, 50)

def update_fps():
    fps=str(int(clock.get_fps()))
    fps_txt= font_style.render(fps, 1, pygame.Color("coral"))
    return fps_txt

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

def Your_score(score):                                                            #show score
    value = font_style.render("Your Score: " + str(score), True, white )
    display.blit(value, [0, 0])

def message(msg,color,x,y):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x, y])

def img_disp(img,x,y):
    imag=pygame.image.load(img)
    display.blit(imag,[x,y])


def message_p(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width/7, dis_height/2])

def gameLoop():  # creating a function
    game_over = False
    game_close = False

    while not game_over:
        game_over = False
        game_close = False
        game_pause = False
        x1 = dis_width / 2
        y1 = dis_height / 2
        fscore=[]
        snake_List=[]
        Lenght_of_snake=1
        maz=0

        pygame.display.update()

        x1_change = 0
        y1_change = 0
        ml=10
        mlt=10
        sre=18
        foodx = round(random.randrange(0, dis_width - snake_block)/ml)*mlt
        foody = round(random.randrange(0, dis_height - snake_block)/ml)*mlt
        foodx2 = round(random.randrange(0, dis_width - snake_block)/ml)*mlt
        foody2 = round(random.randrange(0, dis_height - snake_block)/ml)*mlt
        print(foodx,foody,foodx2,foody2)
        while not game_over:
            while game_close==True:
                run = False
                display.fill(black)
                message("You Lost! Press Q-Quit or C-Play Again", red,320,360)
                Your_score(maz)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            if game_close == True:
                fscore.append(maz)

            for event in pygame.event.get():              # keys to keyboard
                if event.type==QUIT:
                        game_over==True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                       x1_change=0
                       y1_change=(snake_block-sre)
                    elif event.key == pygame.K_UP:
                        x1_change=0
                        y1_change=-(snake_block-sre)
                    elif event.key == pygame.K_RIGHT:
                        x1_change=(snake_block-sre)
                        y1_change=0
                    elif event.key == pygame.K_LEFT:
                        x1_change=-(snake_block-sre)
                        y1_change=0
                    elif event.key == pygame.K_p:
                            game_pause = True

            while game_pause == True:
                clock.tick(0)
                display.fill(black)
                message_p("You paused the game// press 'P' to continue or 'Q' to quit", red)
                Your_score(maz)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
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
                        elif event.key == pygame.K_q:
                            pygame.quit()

            if x1 >= dis_width or x1 <= 0 or y1 >= dis_height or y1 <=0:
                game_close = True
        
            x1+=x1_change
            y1+=y1_change
            display.fill(black)

            pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
            pygame.draw.rect(display, green, [x1, y1, snake_block, snake_block])
            pygame.draw.rect(display, violet, [foodx2, foody2, snake_block, snake_block])
            snake_Head=[]
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List)>Lenght_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
            our_snake(snake_block,snake_List)
            Your_score(maz)
            pygame.display.update()

            if abs(x1-foodx) <=15 and abs(y1-foody) <=15 :
                foodx = round(random.randrange(0, dis_width - snake_block)/ml)*mlt
                foody = round(random.randrange(0, dis_height - snake_block)/ml)*mlt
                Lenght_of_snake+=10
                maz+=1
                
            if abs(x1-foodx2) <=15 and abs(y1-foody2) <=15 :
                foodx2 = round(random.randrange(0, dis_width - snake_block)/mlt)*mlt
                foody2 = round(random.randrange(0, dis_height - snake_block)/mlt)*mlt
                Lenght_of_snake+=10
                maz+=1
            print(snake_List)
        
            clock.tick(60)
    pygame.quit()
    quit()
gameLoop()








