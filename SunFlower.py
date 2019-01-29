import pygame


class SunFlower(pygame.sprite.Sprite):
    def __init__(self, lasttime):
        super(SunFlower, self).__init__()
        self.image = pygame.image.load('material/images/SunFlower_00.png').convert_alpha()
        self.images = [pygame.image.load('material/images/SunFlower_{:02d}.png'.format(i)).convert_alpha() for i in
                       range(0, 13)]
        self.rect = self.images[0].get_rect()
        self.lasttime = lasttime
        # self.rect.top = 380
        # self.rect.left = 250

    def update(self, *args):
        self.image = self.images[args[0] % len(self.images)]
