import pygame
import random

class FlagZombie(pygame.sprite.Sprite):
    def __init__(self):
        super(FlagZombie, self).__init__()
        self.image = pygame.image.load('material/images/FlagZombie_0.png').convert_alpha()
        self.images = [pygame.image.load('material/images/FlagZombie_{}.png'.format(i)).convert_alpha() for i in
                       range(0, 12)]
        self.dieimages = [pygame.image.load('material/images/ZombieDie_{}.png'.format(i)).convert_alpha() for i in
                          range(0, 10)]
        self.attackimages = [pygame.image.load('material/images/FlagZombieAttack_{}.png'.format(i)).convert_alpha() for i in
                             range(0, 11)]
        self.rect = self.images[0].get_rect()
        self.rect.top = 25 + random.randrange(0, 4) * 125
        self.rect.left = 1000
        self.speed = 4
        self.energy = 6
        self.dietimes = 0
        self.isMeetWallNut = False  # 僵尸是否遇到了坚果

    def update(self, *args):
        if self.energy > 0:
            if self.isMeetWallNut:
                self.image = self.attackimages[args[0] % len(self.attackimages)]
            else:
                self.image = self.images[args[0] % len(self.images)]

            if self.rect.left > 250 and not self.isMeetWallNut:
                self.rect.left -= self.speed
        else:
            if self.dietimes > 9:
                if self.dietimes > 24:
                    self.kill()
                else:
                    self.dietimes += 1
            else:
                self.image = self.dieimages[self.dietimes]
                self.dietimes += 1
