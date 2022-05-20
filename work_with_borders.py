import pygame
import random
from constants import snake_block, wall_color

def crash_border(x1, y1, border):
    x_cell = int(x1//snake_block)
    y_cell = int(y1//snake_block)
    if [x_cell, y_cell] in border:
        return True
    else:
        return False
    
def draw_border(border, dis):
    for i in border:
        pygame.draw.rect(dis, wall_color, [(i[0])*snake_block, (i[1])*snake_block, snake_block, snake_block])
        
def read_border():
    b = []
    x = random.randint(1, 3)
    s = 'borders/'  + str(x) + '.txt'
    with open(s) as f:
        f.readline()
        for line in f:
            if line != '\ufeff':
                a = line.split()
                a = [int(a[0])-1, int(a[1])-1]
                b.append(a)
    return b

