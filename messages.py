# -*- coding: utf-8 -*-
"""
Created on Fri May 20 21:30:44 2022

@author: ksy19
"""
import pygame 
from constants import mode_color, rules_color, dis_width, dis_height


def Your_score(score, dis):
    score_font = pygame.font.SysFont("bahnschrift", 35)
    value = score_font.render("Score: " + str(score), True, mode_color)
    dis.blit(value, [4, 4])
    
def Your_record(record, dis):
    record_font = pygame.font.SysFont("bahnschrift", 35)
    value = record_font.render("Record: " + str(record), True, mode_color)
    dis.blit(value, [dis_width - 200, 4])
    
def Your_level(level, dis):
    rules_font = pygame.font.SysFont("bahnschrift", 15)
    value = rules_font.render("Your level: " + str(level) + "/3. Press 1, 2 or 3 to change it.", True, (0, 13, 140))
    dis.blit(value, [4, dis_height - 60])

def Show_rules(dis):
    rules_font = pygame.font.SysFont("bahnschrift", 15)
    rules = '''Eat red apples without touching walls or your own tail! Use arrows to start moving!'''
    value = rules_font.render(rules, True, rules_color)
    dis.blit(value, [4, dis_height-120])
    sn_color = "Press S to change Snake's Head color."
    value = rules_font.render(sn_color, True, rules_color)
    dis.blit(value, [4, dis_height-90])
    
def Your_mode(killing, dis):
    rules_font = pygame.font.SysFont("bahnschrift", 15)
    if killing:
        mes = "Mode: Walls will kill you, to change mode press W."
    else:
        mes ="Mode: Now you can get throught the walls, to change mode press W."
    value = rules_font.render(mes, True, mode_color)
    dis.blit(value, [4, dis_height-30])
    
# function showing message at the end of game 
def message(msg, color, x_mess, y_mess, dis):
    font_style = pygame.font.SysFont("bahnschrift", 25)
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x_mess, y_mess])