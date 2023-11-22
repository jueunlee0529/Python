import sys
import pygame
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((300,300))
CLOCK = pygame.time.Clock()

sysfont = pygame.font.SysFont(None, 36)
txt = sysfont.render("0", True, (0, 0, 0))
n = 0
BLACK = ( 0, 0, 0)
while True:
    SCREEN.fill((255, 255, 255))

    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP :
                n+=10
                txt = sysfont.render("(%d)" % (n), True, BLACK)
            if event.key == K_DOWN :
                n-=10
                txt = sysfont.render("(%d)" % (n), True, BLACK)
            if event.key == K_RIGHT :
                n/=10
                txt = sysfont.render("(%d)" % (n), True, BLACK)
            if event.key == K_LEFT :
                n*=10
                txt = sysfont.render("(%d)" % (n), True, BLACK)
            if event.key == K_ESCAPE :
                pygame.quit()
                sys.exit()

    txt = sysfont.render('%d' % n, True, (0, 0, 0))
    SCREEN.blit(txt, (100, 120))
    pygame.display.update()
    CLOCK.tick(60)
