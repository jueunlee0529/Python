import sys
import pygame
from pygame.locals import *

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
CLOCK = pygame.time.Clock()
# R, G, B

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

while True:
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    #화면을 하얀색으로 채운
    SURFACE.fill(WHITE)

    #사각형의 정의(좌변의 x 좌표, 위쪽 끝 y 좌표, 폭 : 60, 높이)
    rec = Rect(20, 10, 60, 40)

    #사각형 그리기(화면, 색상, 위치 및 크기)
    pygame.draw.rect(SURFACE, RED, rec)

    #원 그리기(화면, 색상, 중심 좌표, 반지름)
    pygame.draw.circle(SURFACE, GREEN, (120, 50),10)

    #삼각형 그리기(화면, 색상, 점의 리스트)
    pygame.draw.polygon(SURFACE, BLUE, [[50, 50], [0, 100], [100, 100]])

    #선 그리기(화면, 색상, 시작점, 도착점)
    pygame.draw.line(SURFACE, BLACK, [120, 0], [120, 100])

    pygame.display.update()
    CLOCK.tick(1)
