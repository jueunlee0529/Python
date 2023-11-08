import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.disply.set_mode((400, 300))
pygame.display.set_caption("Tick Tock Timer")
CLOCK = pygame.time.Clock()
sysfont = pygame.font.Sysfont(None, 36)

timer = 0

while True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

timer += 1
screen.fil((255, 255, 255))
cnt_txt = sysfont.render("Timer : %d" % timer, True, (0, 0, 0))
screen.blit(cnt_txt, (140, 140))
pygame.display.update()
CLOCK.tick(1)

