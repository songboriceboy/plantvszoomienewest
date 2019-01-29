import pygame
import random


class Bullet(pygame.sprite.Sprite):
    def __init__(self, rect, bg_size):
        super(Bullet, self).__init__()
        self.image = pygame.image.load('material/images/Bullet_1.png').convert_alpha()
        self.width, self.height = bg_size
        self.rect = self.image.get_rect()

        self.rect.top = rect.top
        self.rect.left = rect.left + 50
        self.speed = 10

    # 更新精灵的位置
    def update(self, *args):
        if self.rect.left <= self.width:
            self.rect.left += self.speed
        else:
            self.kill()
