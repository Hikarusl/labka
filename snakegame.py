# -*- coding: utf-8 -*-
"""
@author: ksy19
"""
import pygame
import random
import sys


from work_with_borders import crash_border, draw_border, read_border
from constants import food_color, gameover_color, snake_block
from constants import dis_width, dis_height, gameover_text, background_text
from messages import Your_score, Your_level, Your_mode, Your_record, Show_rules, message


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

#returns food coordinates checked on not crossing the walls
def food_coordinates(dis_width, dis_height, snake_block, border):
    foodx = round(random.randrange(0, dis_width - snake_block) // snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) // snake_block) * snake_block
    while [foodx//snake_block, foody//snake_block] in border:
        foodx = round(random.randrange(0, dis_width - snake_block) // snake_block) * snake_block
        foody = round(random.randrange(0, dis_height - snake_block) // snake_block) * snake_block
    return foodx, foody
 
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

    border = read_border()
    
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx, foody = food_coordinates(dis_width, dis_height, snake_block, border)
    foodx1, foody1 = food_coordinates(dis_width, dis_height, snake_block, border)
    while foodx==foodx1 and foody==foody1:
        foodx1, foody1 = food_coordinates(dis_width, dis_height, snake_block, border)
    
    while not game_over:
 
        while game_close == True:
            dis.fill(bg_color)
            message(gameover_text, gameover_color, dis_width/6+10, dis_height/3, dis)
            message(background_text, gameover_color, dis_width/5-10, dis_height/3*2, dis)
            Your_score(Length_of_snake - 1, dis)
            if Length_of_snake - 1 > record:
                record = Length_of_snake - 1 
            Your_record(record, dis)
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
                if event.key == pygame.K_LEFT and ((x1_change!=snake_block) ):
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and ((x1_change!=-snake_block)):
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and ( y1_change!=snake_block):
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and ( y1_change!=-snake_block):
                    y1_change = snake_block
                    x1_change = 0
                elif x1_change == 0 and y1_change == 0:
                    if event.key == pygame.K_1:
                        level = 1
                        Your_level(level, dis)
                    elif event.key == pygame.K_2:
                        level = 2
                        Your_level(level, dis)
                    elif event.key == pygame.K_3:
                        level = 3
                        Your_level(level, dis)
                    elif event.key==pygame.K_w:
                        killing_walls = not killing_walls
                        Your_mode(killing_walls, dis)
                    elif event.key==pygame.K_s:
                        snake_color = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
                        our_snake(snake_block, snake_List, snake_color)
                    snake_speed = 5*level
 
    
        x1 += x1_change
        y1 += y1_change

        # bounds check
        if crash_border(x1, y1, border) and killing_walls:
            game_close = True
        elif (x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0) and killing_walls:
            game_close = True
        else:
            x1 = (x1 + dis_width) % dis_width
            y1 = (y1 + dis_height) % dis_height

        dis.fill(bg_color)
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block], border_radius=snake_block//2)
        pygame.draw.rect(dis, food_color, [foodx1, foody1, snake_block, snake_block], border_radius=snake_block//2)
        draw_border(border, dis)

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
        Your_score(Length_of_snake - 1, dis)
        Your_record(record, dis)
        
        if x1_change == 0 and y1_change == 0:
            Show_rules(dis)
            Your_level(level, dis)
            Your_mode(killing_walls, dis)

        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx, foody = food_coordinates(dis_width, dis_height, snake_block, border)
            while foodx==foodx1 and foody==foody1:
                foodx, foody = food_coordinates(dis_width, dis_height, snake_block, border)
            Length_of_snake += 1
            snake_speed += 0.25
        if x1 == foodx1 and y1 == foody1:
            foodx1, foody1 = food_coordinates(dis_width, dis_height, snake_block, border)
            while foodx==foodx1 and foody==foody1:
                foodx1, foody1 = food_coordinates(dis_width, dis_height, snake_block, border)
            Length_of_snake += 1
            snake_speed += 0.25
 
        clock.tick(snake_speed)
 
    pygame.quit()
    sys.exit()


pygame.init()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game') 
clock = pygame.time.Clock()

#initial parameters for global vars  
bg_color = (255, 200, 245)
record = 0
level = 1
killing_walls = True
snake_color=[0,0,0]

gameLoop()
