# -*- coding: utf-8 -*-
"""
@author: ksy19
"""

import pygame
import random
import sys

from caption.caption import Caption

pygame.init()
 
#white = (255, 255, 255)
#yellow = (255, 255, 102)
#black = (0, 0, 0)
#red = (213, 50, 80)
#green = (0, 255, 0)
#blue = (50, 153, 213)

rules_color = (100, 13, 100)
mode_color = (0, 13, 140)
food_color = (155, 40, 50)
gameover_color = (130, 10, 130)

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
rules_font = pygame.font.SysFont("bahnschrift", 15)
 

def Show_rules():
    rules = '''Eat red apples without touching walls or your own tail! Use arrows to start moving!'''
    value = rules_font.render(rules, True, rules_color)
    dis.blit(value, [4, dis_height-120])
    sn_color = "Press S to change Snake's Head color."
    value = rules_font.render(sn_color, True, rules_color)
    dis.blit(value, [4, dis_height-90])
    
 
    
def Your_mode(killing):
    if killing:
        mes = "Mode: Walls will kill you, to change mode press W."
    else:
        mes ="Mode: Now you can get throught the walls, to change mode press W."
    value = rules_font.render(mes, True, mode_color)
    dis.blit(value, [4, dis_height-30])
    
#function drawing snakes from gradient blocks
def our_snake(snake_block, snake_list, snake_color=[0,0,0]):
    i1=snake_color[0]
    i2=snake_color[1]
    i3=snake_color[2]
    for x in snake_list[::-1]:
        pygame.draw.rect(dis, (i1, i2, i3), [x[0], x[1], snake_block, snake_block])
        i1+=8
        i2+=8
        i3+=8
        if i1>200: i1 = 200
        if i2>200: i2 = 200
        if i3>200: i3 = 200
    
 
# function showing message at the end of game 
def message(msg, color, x_mess, y_mess):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x_mess, y_mess])
 
#main function for game
def gameLoop():
    global bg_color
    global record 
    global level
    global killing_walls
    global snake_color
    snake_speed = 5*level
    game_over = False
    game_close = False

    border = [[2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [20, 1], [20, 2], [20, 3]]
    #border = read_border()
 
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
            message("You Lost! Press C-Play, or Q-Quit", gameover_color, dis_width/6+10, dis_height/3)
            message("Press B-change background color", gameover_color, dis_width/5-10, dis_height/3*2)
            Caption.Your_score(Length_of_snake - 1)
            if Length_of_snake - 1 > record:
                record = Length_of_snake - 1 
            Caption.Your_record(record)
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
                elif x1_change == 0 and y1_change == 0:
                    if event.key == pygame.K_1:
                        level = 1
                        Caption.Your_level(level)
                    elif event.key == pygame.K_2:
                        level = 2
                        Caption.Your_level(level)
                    elif event.key == pygame.K_3:
                        level = 3
                        Caption.Your_level(level)
                    elif event.key==pygame.K_w:
                        killing_walls = not killing_walls
                        Caption.Your_mode(killing_walls)
                    elif event.key==pygame.K_s:
                        snake_color = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
                        our_snake(snake_block, snake_List, snake_color)
                    snake_speed = 5*level
 
    
        x1 += x1_change
        y1 += y1_change

        # bounds check
        if crash_border(x1, y1, border):
            game_close = True
        elif (x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0) and killing_walls:
            game_close = True
        else:
            x1 = (x1 + dis_width) % dis_width
            y1 = (y1 + dis_height) % dis_height

        dis.fill(bg_color)
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block], border_radius=snake_block//2)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List, snake_color)
        Caption.Your_score(Length_of_snake - 1)
        Caption.Your_record(record)
        
        if x1_change == 0 and y1_change == 0:
            Show_rules()
            Caption.Your_level(level)
            Your_mode(killing_walls)

        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
            snake_speed += 0.25
 
        clock.tick(snake_speed)
 
    pygame.quit()
    sys.exit()
 
#initial parameters for global vars    
bg_color = (255, 200, 245)
record = 0
level = 1
killing_walls = True
snake_color=[0,0,0]

gameLoop()
