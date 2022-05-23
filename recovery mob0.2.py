﻿# CrÃ©Ã© par acarp, le 26/04/2022 avec EduPython
#serpiente taca taca
import time
from pygame.locals import *
import pygame
import random
from os import path



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

pygame.display.update()
pygame.display.set_caption('Snake by Carpu')

starttime=time.time()
  #run clock
clock=pygame.time.Clock()

snake_block=30  #snake
snake_speed=60

# message system
font_style = pygame.font.SysFont(None, 50)




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

direction='none'

def gameLoop():  # creating a function
    game_over = False
    game_close = False
    while not game_over:
        game_close = False
        game_pause = False
        x1 = dis_width / 2
        y1 = dis_height / 2
        fscore=[]
        snake_List=[]
        Lenght_of_snake=1
        ml=10
        sre=8
        #up=pygame.draw.rect(display, green, [dis_width/2,400,80,80])
        #down=pygame.draw.rect(display, green, [dis_width/2,400,80,80])
        #left=pygame.draw.rect(display, green, [490,400,80,80])
        #right=pygame.draw.rect(display, green, [590,400,80,80])
        #pause_bt=pygame.draw.rect(display,red,[650,400,80,80])
        #pygame.display.update()

        x1_change = 0
        y1_change = 0

        foodx = round(random.randrange(0, dis_width - snake_block)/ml)*ml
        foody = round(random.randrange(0, 1450 - snake_block)/ml)*ml
        foodx2 = round(random.randrange(0, dis_width - snake_block)/ml)*ml
        foody2 = round(random.randrange(0, 1450 - snake_block)/ml)*ml
        while not game_over:
            while game_close==True:
                display.fill(black)
                message("You Lost! Press Q-Quit or C-Play Again", red,320,360)
                Your_score(Lenght_of_snake-1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            if game_close == True:
                fscore.append(Lenght_of_snake)

            for event in pygame.event.get():              # keys to keyboard
                if event.type==QUIT:
                        game_over==True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                       x1_change=0
                       y1_change=(snake_block-sre)
                    elif event.key == pygame.K_w:
                        x1_change=0
                        y1_change=-(snake_block-sre)
                    elif event.key == pygame.K_d:
                        x1_change=(snake_block-sre)
                        y1_change=0
                    elif event.key == pygame.K_a:
                        x1_change=-(snake_block-sre)
                        y1_change=0

            while game_pause == True:
                clock.tick(0)
                display.fill(black)
                pause_bt=pygame.draw.rect(display,green,[660,600,30,30])
                quit_bt=pygame.draw.rect(display,red,[600,600,30,30])
                message_p("You paused the game// press green to continue or red to quit", red)
                Your_score(Lenght_of_snake-1)
                pygame.display.update()


                if pause_bt.collidepoint(mouse_pos):
                            direction = 'pause'
                if quit_bt.collidepoint(mouse_pos):
                            direction = 'quit'

                if direction == 'pause':
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
                if direction == 'quit':
                    pygame.quit()

            if x1 >= dis_width or x1 < 0 or y1 >= 1450 or y1 < 0:
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
            Your_score(Lenght_of_snake-1)
            pygame.display.update()

            if abs(x1-foodx) <=7  and abs(y1-foody) <=7:
                foodx = round(random.randrange(0, dis_width - snake_block)/30)*30
                foody = round(random.randrange(0, 1450 - snake_block)/30)*30
                Lenght_of_snake+=1
            if abs(x1-foodx2) <=7  and abs(y1-foody2) <=7:
                foodx2 = round(random.randrange(0, dis_width - snake_block)/30)*30
                foody2 = round(random.randrange(0, 1450 - snake_block)/30)*30
                Lenght_of_snake+=1

            clock.tick(30)
    pygame.quit()
    quit()
gameLoop()