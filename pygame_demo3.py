import pygame
from pygame.locals import *
import sys
import math
import random
#初始化pygame

pygame.init()

size = (1000, 800)

# 设置屏幕宽高
screen = pygame.display.set_mode(size)
# 设置屏幕标题
pygame.display.set_caption("my first game")


white = 255, 255, 255
black = 0, 0, 0

circleHeart = (500, 400)
# print(circleHeart[0])
radius = 80
moving = False
while True:

    # 启动消息队列，获取消息并处理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            print(event.rel)
            if moving:
                moveXY = event.rel
                circleHeart = (circleHeart[0] + moveXY[0], circleHeart[1] + moveXY[1])

        elif event.type == MOUSEBUTTONDOWN:
            length = (circleHeart[0] - event.pos[0]) * (circleHeart[0] - event.pos[0]) + (circleHeart[1] - event.pos[1]) * (circleHeart[1] - event.pos[1])
            length = math.sqrt(length)
            if event.button == 1 and length < radius:#并且判断鼠标按下的位置在圆内
                moving = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                moving = False


    screen.fill(black)  #填充背景

    pygame.draw.circle(screen, white, circleHeart, radius, 3)
    pygame.display.update()






