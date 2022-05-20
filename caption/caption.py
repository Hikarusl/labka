import collections
import pygame
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)
record_font = pygame.font.SysFont("bahnschrift", 35)
rules_font = pygame.font.SysFont("bahnschrift", 15)
# functions showing hints
def Your_score(score):
        value = score_font.render("Score: " + str(score), True, mode_color)
        dis.blit(value, [4, 4])

def Your_record(record):
        value = record_font.render("Record: " + str(record), True, mode_color)
        dis.blit(value, [dis_width - 200, 4])

def Your_level(level):
        value = rules_font.render("Your level: " + str(level) + "/3. Press 1, 2 or 3 to change it.", True, (0, 13, 140))
        dis.blit(value, [4, dis_height - 60])