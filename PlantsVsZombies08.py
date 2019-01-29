import pygame
from pygame.locals import *
import sys
import time
import random

from Bullet import Bullet
from FlagZombie import FlagZombie
from Peashooter import Peashooter
from Sun import Sun
from SunFlower import SunFlower
from WallNut import WallNut

# 初始化pygame
from Zombie import Zombie

pygame.init()

# for font in pygame.font.get_fonts():
#     print(font)

size = (1200, 600)

# 设置屏幕宽高
screen = pygame.display.set_mode(size)
# 设置屏幕标题
pygame.display.set_caption("植物大战僵尸")

# logo = pygame.image.load('material/images/logo.jpg').convert_alpha()
# pygame.display.set_icon(logo)

backgroundImg = pygame.image.load('material/images/background1.jpg').convert_alpha()
sunbackImg = pygame.image.load('material/images/SeedBank.png').convert_alpha()
flower_seed = pygame.image.load("material/images/Sunflower.gif")
wallNut_seed = pygame.image.load("material/images/WallNut.gif")
peashooter_seed = pygame.image.load("material/images/Peashooter.gif")
sunFlowerImg = pygame.image.load('material/images/SunFlower_00.png').convert_alpha()
wallNutImg = pygame.image.load('material/images/WallNut_00.png').convert_alpha()
peashooterImg = pygame.image.load('material/images/Peashooter_00.png').convert_alpha()

score = '500'
myfont = pygame.font.SysFont('arial', 20)
txtImg = myfont.render(score, True, (0, 0, 0))

nameList = ['刘无敌 ', '刘国臣 ', '邸家兴 ', '陶倩', '大汉 ', '张新杰', '李彪 ', '纪勇博', ' 张榕', '楠姐 ', '天昊 ']

peashooterList = pygame.sprite.Group()
sunFlowerList = pygame.sprite.Group()
wallNutList = pygame.sprite.Group()
bulletList = pygame.sprite.Group()

sunList = pygame.sprite.Group()
zombieList = pygame.sprite.Group()
flagZombieList = pygame.sprite.Group()

index = 0
clock = pygame.time.Clock()

GENERATOR_SUN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GENERATOR_SUN_EVENT, 100)

GENERATOR_ZOMBIE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(GENERATOR_ZOMBIE_EVENT, 5000)

GENERATOR_PEASHOOTER_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(GENERATOR_PEASHOOTER_EVENT, 2000)

GENERATOR_FLAGZOMBIE_EVENT = pygame.USEREVENT + 4
pygame.time.set_timer(GENERATOR_FLAGZOMBIE_EVENT, 10000)

choose = 0

while True:

    # print(time.time())
    clock.tick(15)
    # 启动消息队列，获取消息并处理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == GENERATOR_SUN_EVENT:
            # 当前是否有太阳花对象，有几个太阳花对象，就生成几个太阳
            if len(sunFlowerList) > 0:
                timeNow = time.time()
                for sunFlower in sunFlowerList:
                    if timeNow - sunFlower.lasttime >= 5:
                        sunFlower.lasttime = timeNow
                        sun = Sun(sunFlower.rect)
                        sunList.add(sun)

        if event.type == GENERATOR_PEASHOOTER_EVENT:
            # 当前是否有太阳花对象，有几个太阳花对象，就生成几个太阳
            if len(peashooterList) > 0:
                for peashooter in peashooterList:
                    bullet = Bullet(peashooter.rect, size)
                    bulletList.add(bullet)

        if event.type == GENERATOR_ZOMBIE_EVENT:
            randomIndex = random.randrange(0, len(nameList))
            nameOfZombie = nameList[randomIndex]
            zombie = Zombie(nameOfZombie)
            zombieList.add(zombie)

        if event.type == GENERATOR_FLAGZOMBIE_EVENT:
            flagZombie = FlagZombie()
            flagZombieList.add(flagZombie)

        if event.type == MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            # 判断是否按下的事鼠标左键
            if mouse_pressed[0]:
                (x, y) = pygame.mouse.get_pos()
                # print(x, y)

                # 判断鼠标是否点中了某个卡片
                if 330 <= x <= 380 and 10 <= y <= 80 and int(score) >= 50:
                    choose = 1
                elif 380 < x <= 430 and 10 <= y <= 80 and int(score) >= 50:
                    choose = 2
                elif 430 < x <= 480 and 10 <= y <= 80 and int(score) >= 100:
                    choose = 3
                elif 250 < x < 1200 and 70 < y < 600:
                    if choose == 1:
                        sunFlower = SunFlower(time.time())
                        sunFlower.rect.top = y
                        sunFlower.rect.left = x
                        sunFlowerList.add(sunFlower)
                        choose = 0

                        # 扣去太阳花相应的分数
                        score = int(score)
                        score -= 50
                        myfont = pygame.font.SysFont('arial', 20)
                        txtImg = myfont.render(str(score), True, (0, 0, 0))
                    if choose == 2:
                        wallNut = WallNut()
                        wallNut.rect.top = y
                        wallNut.rect.left = x
                        wallNutList.add(wallNut)
                        choose = 0

                        # 扣去太阳花相应的分数
                        score = int(score)
                        score -= 50
                        myfont = pygame.font.SysFont('arial', 20)
                        txtImg = myfont.render(str(score), True, (0, 0, 0))
                    if choose == 3:
                        peashooter = Peashooter()
                        peashooter.rect.top = y
                        peashooter.rect.left = x
                        peashooterList.add(peashooter)
                        choose = 0

                        # 扣去太阳花相应的分数
                        score = int(score)
                        score -= 100
                        myfont = pygame.font.SysFont('arial', 20)
                        txtImg = myfont.render(str(score), True, (0, 0, 0))

                for sun in sunList:
                    if sun.rect.collidepoint((x, y)):
                        # sunList.remove(sun)
                        sun.is_click = True
                        score = int(score) + 50
                        myfont = pygame.font.SysFont('arial', 20)
                        txtImg = myfont.render(str(score), True, (0, 0, 0))

    # 如果坚果和僵尸冲突：
    # 1.僵尸要停住，动画要变成吃坚果
    # 2.坚果要掉血（n个僵尸同时吃，要掉n个血）
    # 3.坚果血没后，要kill掉自己
    # 4.坚果吃完后，僵尸要继续向前走
    for zombie in zombieList:
        for wallNut in wallNutList:
            if pygame.sprite.collide_mask(zombie, wallNut):
                zombie.isMeetWallNut = True
                wallNut.zombies.add(zombie)

    for zombie in flagZombieList:
        for wallNut in wallNutList:
            if pygame.sprite.collide_mask(zombie, wallNut):
                zombie.isMeetWallNut = True
                wallNut.zombies.add(zombie)


    for bullet in bulletList:
        for zombie in zombieList:
            if pygame.sprite.collide_mask(bullet, zombie):
                zombie.energy -= 1
                bulletList.remove(bullet)

    for bullet in bulletList:
        for flagZombie in flagZombieList:
            if pygame.sprite.collide_mask(bullet, flagZombie):
                flagZombie.energy -= 1
                bulletList.remove(bullet)


    screen.blit(backgroundImg, (0, 0))
    screen.blit(sunbackImg, (250, 0))
    screen.blit(txtImg, (270, 60))

    screen.blit(flower_seed, (330, 10))
    screen.blit(wallNut_seed, (380, 10))
    screen.blit(peashooter_seed, (430, 10))

    # 根据选中的卡片，将对应的植物图片，显示在当前鼠标的右下角，跟随鼠标移动
    (x, y) = pygame.mouse.get_pos()

    if choose == 1:
        screen.blit(sunFlowerImg, (x, y))
    if choose == 2:
        screen.blit(wallNutImg, (x, y))
    if choose == 3:
        screen.blit(peashooterImg, (x, y))

    # if index % 10 == 0:
    #     bullet = Bullet(peashooter.rect, size)
    #     spriteList.add(bullet)

    sunFlowerList.update(index)
    sunFlowerList.draw(screen)
    sunList.update(index)
    sunList.draw(screen)
    zombieList.update(index)
    zombieList.draw(screen)
    wallNutList.update(index)
    wallNutList.draw(screen)
    peashooterList.update(index)
    peashooterList.draw(screen)
    bulletList.update(index)
    bulletList.draw(screen)
    flagZombieList.update(index)
    flagZombieList.draw(screen)

    for zombie in zombieList:
        yourfont = pygame.font.SysFont('simsunnsimsun', 30)
        headpic = yourfont.render(zombie.name, True, (255, 0, 0))
        screen.blit(headpic, (zombie.rect.left + 60, zombie.rect.top - 20))

    index += 1

    pygame.display.update()
