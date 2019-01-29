import pygame
from pygame.locals import *
import sys
from Peashooter import Peashooter
from SunFlower import SunFlower
from WallNut import WallNut

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

peashooter = Peashooter()
sunFlower = SunFlower()
wallNut = WallNut()


index = 0
clock = pygame.time.Clock()
while True:
    if index > 100:
        index = 0

    clock.tick(15)
    # 启动消息队列，获取消息并处理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(backgroundImg, (0, 0))
    screen.blit(sunbackImg, (250, 30))
    screen.blit(txtImg, (300, 33))

    screen.blit(peashooter.images[index % 13], peashooter.rect)
    screen.blit(sunFlower.images[index % 13], sunFlower.rect)
    screen.blit(wallNut.images[index % 13], wallNut.rect)

    index += 1

    pygame.display.update()
