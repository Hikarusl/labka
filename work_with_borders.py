#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def crash_border(x1, y1, border):
    x_cell = int(x1//20)
    y_cell = int(y1//20)
    if [x_cell, y_cell] in border:
        return True
    else:
        return False
    
def draw_border(border):
    for i in border:
        pygame.draw.rect(dis, (173, 135, 98), [(i[0]-1)*20, (i[1]-1)*20, 20, 20])
        
def read_border():
    b = []
    f = open('map.txt')
    for line in f:
        a = list(map(int, line.split()))
        b.append(a)
    f.close()
    return b

