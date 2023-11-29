import sys
import pygame
from pygame.locals import *
import random

pygame.init()
SCREEN = pygame.display.set_mode((600, 600))
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 72)


light_img = pygame.image.load("light.png")
man_img = pygame.image.load("man.png")
L_size = light_img.get_size()
m_size = man_img.get_size()

game_over = False
m_x, m_y = 250, 480

L_x = []
L_y = []

cnt = 0

while True:

    if game_over :
        break
    SCREEN.fill((0, 0, 0))

    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        if m_x > 0 :
            m_x -= 5
    if key_event[pygame.K_RIGHT]:
        if m_x < 500 :
            m_x += 5
    SCREEN.blit(man_img, (m_x,m_y))
    cnt += 1
    if cnt >= 20:
        cnt = 0
        L_x.append(random.randint(0,600))
        L_y.append(0)

    for i in range(len(L_x)) :
        L_y[i] += 5
        SCREEN.blit(light_img, (L_x[i],L_y[i]))
        if L_y[i]>= 550 :
            L_x.remove(L_x[i])
            L_y.remove(L_y[i])
            break
    for i in range(len(L_x)) :
        if L_x[i] + L_size[0] >= m_x and m_x + m_size[0] >= L_x[i]:
            if L_y[i] - L_size[1] >= m_y :
                msg = sysfont.render("Game Over!", True, (255, 0, 0))
                SCREEN.blit(msg, (160, 250))
                game_over = True
                
    pygame.display.update()
    CLOCK.tick(60)


        
