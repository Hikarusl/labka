
import pygame
import random

def crash_border(x1, y1, border):
    x_cell = int(x1//20)
    y_cell = int(y1//20)
    if [x_cell, y_cell] in border:
        return True
    else:
        return False
    
def draw_border(border, dis):
    for i in border:
        pygame.draw.rect(dis, (173, 135, 98), [(i[0]-1)*20, (i[1]-1)*20, 20, 20])
        
def read_border():
    b = []
    #x = random.randint(1, 3)
    #s = 'borders/'  + str(x) + '.txt'
    with open('borders/1.txt') as f:
        c = f.readline()
        for line in f:
            if line != '\ufeff':
                a = line.split()
                a = [int(a[0]), int(a[1])]
                b.append(a)
    return b

