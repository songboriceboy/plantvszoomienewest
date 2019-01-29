import pygame
import random


class Sun(pygame.sprite.Sprite):
    def __init__(self, rect):
        super(Sun, self).__init__()
        self.image = pygame.image.load('material/images/Sun_1.png').convert_alpha()
        self.images = [pygame.image.load('material/images/Sun_{}.png'.format(i)).convert_alpha() for i in
                       range(1, 18)]
        self.rect = self.images[0].get_rect()
        offsetTop = random.randint(-50, 50)
        offsetLeft = random.randint(-50, 50)

        self.rect.top = rect.top + offsetTop
        self.rect.left = rect.left + offsetLeft

        self.is_click = False
        self.times = 5
        self.scale = 10

    # 更新精灵的位置
    def update(self, *args):
        self.image = self.images[args[0] % len(self.images)]
        if self.is_click:
            self.rect.left -= (self.rect.left - 250) / self.times
            self.rect.top -= (self.rect.top - 30) / self.times

            self.image = pygame.transform.smoothscale(self.image, (self.rect.width // self.times * self.scale, self.rect.height // self.times * self.scale))
            if self.scale > 1:
                self.scale -= 1

            print(self.rect.left)
            if self.rect.left <= 250 and self.rect.top <= 30:
                self.kill()
