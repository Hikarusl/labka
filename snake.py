# -*- coding: utf-8 -*-
"""
Created on Mon May 16 23:04:31 2022

@author: ksy19
"""

import pygame
import random
import sys

pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 20
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)
record_font = pygame.font.SysFont("bahnschrift", 35)
rules_font = pygame.font.SysFont("bahnschrift", 13)
 
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, (0, 13, 140))
    dis.blit(value, [4, 4])

def Your_record(record):
    value = record_font.render("Record: " + str(record), True, (0, 13, 140))
    dis.blit(value, [dis_width-200, 4])
 
def Show_rules():
    rules = "Try to eat red apples without touching walls or your own tail! Use arrows to start moving!"
    value = rules_font.render(rules, True, (0, 13, 140))
    dis.blit(value, [4, dis_height-60])
    
def our_snake(snake_block, snake_list):
    i1=0
    i2=0
    i3=0
    for x in snake_list[::-1]:
        pygame.draw.rect(dis, (i1, i2, i3), [x[0], x[1], snake_block, snake_block])
        i1+=8
        i2+=8
        i3+=8
        if i1>200: i1 = 200
        if i2>200: i2 = 200
        if i3>200: i3 = 200
    
 
 
def message(msg, color, x_mess, y_mess):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x_mess, y_mess])
 

def gameLoop():
    global bg_color
    global record 
    
    snake_speed = 10
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
    
   
    
    x1_change = 0
    y1_change = 0
    
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) // snake_block) * snake_block
    
    foody = round(random.randrange(0, dis_height - snake_block) // snake_block) * snake_block
    
    while not game_over:
 
        while game_close == True:
            dis.fill(bg_color)
            message("You Lost! Press C-Play, or Q-Quit", (130, 10, 130), dis_width/6+10, dis_height/3)
            message("Press B-change background color", (130, 10, 130), dis_width/5-10, dis_height/3*2)
            Your_score(Length_of_snake - 1)
            if Length_of_snake - 1 > record:
                record = Length_of_snake - 1 
            Your_record(record)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_b:
                        r = random.randint(200,255)
                        g = random.randint(200,255)
                        b = random.randint(200,255)
                        bg_color = ((r, g, b))
                        dis.fill(bg_color)
 
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
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(bg_color)
        pygame.draw.rect(dis, (155, 40, 50), [foodx, foody, snake_block, snake_block], border_radius=snake_block//2)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        Your_record(record)
        if x1_change == 0 and y1_change == 0:
            Show_rules()
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
            snake_speed += 0.25
 
        clock.tick(snake_speed)
 
    pygame.quit()
    sys.exit()
 
bg_color = (255, 200, 245)
record = 0

gameLoop()