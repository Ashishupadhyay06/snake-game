import pygame
from pygame.locals import*
import time
import random

pygame.init()
red = (201,18,18)
black = (0,0,0)
white = (255,255,255)
green = (41,240,26)
yellow = (239,250,32)

root_width = 600
root_height = 400
rootdow = pygame.display.set_mode((root_width,root_height))
# time.sleep(5)
pygame.display.set_caption("Snake Game")
time.sleep(2)

snake = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("calibri",26)
score_font = pygame.font.SysFont("comicsansms",30)

def user_score(score):
    number = score_font.render("Score :" + str(score),True, yellow)
    rootdow.blit(number,[0,0])

def game_snake(snake,snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(rootdow, green, [x[0],x[1],snake,snake])
    

def message(msg):
    msg = font_style.render(msg,True, red)
    rootdow.blit(msg,[root_width/17,root_height/4])

def game_loop():
    gameOver = False
    gameClose = False

    x1 = root_width/2
    y1 = root_height/2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0,root_width - snake)/10.0)*10.0
    foody = round(random.randrange(0,root_height - snake)/10.0)*10.0

    while not gameOver:

        while gameClose == True:
            rootdow.fill(white)
            message("you lost! press P to play again and Q to quit the game")
            user_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = True

                    if event.key == pygame.K_p:
                        game_loop()    


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0

                if event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0

                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake

                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake    

        if x1 > root_width or x1 < 0 or y1 > root_height or y1 < 0:
            gameClose = True
        x1 += x1_change
        y1 += y1_change
        rootdow.fill(black)
        pygame.draw.rect(rootdow,red,[foodx,foody,snake,snake])              
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_length_list.append(snake_size)
        if len(snake_length_list)>snake_length:
            del snake_length_list[0]

        game_snake(snake,snake_length_list)    
        user_score(snake_length - 1) 

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,root_width - snake)/10.0)*10.0
            foody = round(random.randrange(0,root_height - snake)/10.0)*10.0
            snake_length += 1

        clock.tick(snake_speed)    


    pygame.quit()
    quit()

game_loop()


