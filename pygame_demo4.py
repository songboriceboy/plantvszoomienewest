import pygame
from pygame.locals import *
import sys
import math
import random

# 初始化pygame

pygame.init()

size = (800, 600)

# 设置屏幕宽高
screen = pygame.display.set_mode(size)
# 设置屏幕标题
pygame.display.set_caption("my first game")

spaceImg = pygame.image.load("space.png").convert_alpha()
earthImg = pygame.image.load("planet2.png").convert_alpha()
weight, height = earthImg.get_size()

ship = pygame.image.load("military.png").convert_alpha()
ship_weight, ship_height = earthImg.get_size()
ship = pygame.transform.smoothscale(ship, (ship_weight, ship_height+400))
black = 0, 0, 0
while True:

    # 启动消息队列，获取消息并处理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(black)  # 填充背景
    screen.blit(spaceImg, (0, 0))
    screen.blit(earthImg, ((800-weight)/2, (600-height)/2))

    screen.blit(ship, (50, 50))
    pygame.display.update()
