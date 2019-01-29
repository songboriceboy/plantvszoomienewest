import pygame
from pygame.locals import *
import sys

#初始化pygame
pygame.init()
# 设置屏幕宽高
screen = pygame.display.set_mode((600, 400))
# 设置屏幕标题
pygame.display.set_caption("my first game")

# 设置字体类型及大小
myfont = pygame.font.SysFont('arial', 100)

white = 255, 255, 255
black = 0, 0, 0
# 创建要显示的文字
txtImage = myfont.render("hello world", True, white)
color = 255, 255, 0
speedX = 0.1
xPos = 50



while True:
    # 启动消息队列，获取消息并处理
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill(black)  # 填充背景
    # screen.blit(txtImage, (100, 100))  #贴上文字
    # pygame.draw.line(screen, color, (0, 0), (100, 100), 3)
    # pygame.draw.circle(screen, color, (100, 100), 30, 1)

    if xPos >= (600 - 50):
        speedX = -speedX
    if xPos <= 0:
        speedX = -speedX

    pygame.draw.rect(screen, color, (xPos, 50, 50, 50), 0)
    pygame.display.update()
    xPos += speedX





