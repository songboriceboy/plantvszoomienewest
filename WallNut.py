import pygame


class WallNut(pygame.sprite.Sprite):
    def __init__(self):
        super(WallNut, self).__init__()
        self.image = pygame.image.load('material/images/WallNut_00.png').convert_alpha()
        self.images = [pygame.image.load('material/images/WallNut_{:02d}.png'.format(i)).convert_alpha() for i in
                       range(0, 13)]
        self.rect = self.images[0].get_rect()
        self.zombies = set()
        self.energy = 5 * 15
        # self.rect.top = 280
        # self.rect.left = 250

    def update(self, *args):
        for zoobie in self.zombies:
            if not zoobie.isAlive:
                continue
            self.energy -= 1
            if self.energy <= 0:
                for zoobie in self.zombies:
                    zoobie.isMeetWallNut = False
                self.kill()

        self.image = self.images[args[0] % len(self.images)]
