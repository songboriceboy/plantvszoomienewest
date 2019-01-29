import pygame
from pygame.locals import *
import sys

# import os

# rootPath = os.getcwd()
# backgroundPath = os.path.join(rootPath, 'material/images/background2.jpg')
# sunbackPath = os.path.join(rootPath, 'material/images/SunBack.png')
# 初始化pygame
pygame.init()

size = (1200, 600)

# 设置屏幕宽高
screen = pygame.display.set_mode(size)
# 设置屏幕标题
pygame.display.set_caption("植物大战僵尸")

backgroundImg = pygame.image.load('material/images/background1.jpg').convert_alpha()
sunbackImg = pygame.image.load('material/images/SunBack.png').convert_alpha()

myfont = pygame.font.SysFont('arial', 30)
txtImg = myfont.render("1000", True, (0, 0, 0))

while True:

    # 启动消息队列，获取消息并处理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(backgroundImg, (0, 0))
    screen.blit(sunbackImg, (250, 30))
    screen.blit(txtImg, (300, 33))

    pygame.display.update()
