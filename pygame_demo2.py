import pygame
from pygame.locals import *
import sys
import random
#初始化pygame
pygame.init()
# 设置屏幕宽高
screen = pygame.display.set_mode((600, 400))
# 设置屏幕标题
pygame.display.set_caption("my first game")

# 设置字体类型及大小
myfont = pygame.font.SysFont(None, 100)

white = 255, 255, 255
black = 0, 0, 0

num = 97
char = chr(num-32)
# print(char)


while True:

    # 启动消息队列，获取消息并处理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            print(event.unicode)
            print('键盘被按下')
        elif event.type == KEYUP:
            print('键盘被抬起')
        # elif event.type == MOUSEMOTION:
        #     print(event.pos)
        #     print(event.rel)
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
            print(event.button)


    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    elif keys[num]:
        num = random.randint(97, 122)
        char = chr(num - 32)
        # print(char)
        # 创建要显示的文字

    txtImage = myfont.render(char, True, white)
    screen.fill(black)  #填充背景
    screen.blit(txtImage, (100, 100))  #贴上文字

    pygame.display.update()






