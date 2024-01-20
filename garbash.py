
class arch(Tower):
    def __init__(self, pos):
        super().__init__(pos)
        self.ammo = pygame.transform.scale(pygame.image.load('C:/TESTpy/PyDefence/pics/effects/Arrow.png'), (30, 10))
        self.image = pygame.image.load('C:/TESTpy/PyDefence/pics/arch.png')
        x, y = self.image.get_size()
        kof_x, kof_y = x / window_size[0], y / window_size[1]
        self.image = pygame.transform.scale(self.image, (x / kof_x - 1770, y / kof_y - 900))
        window_surface.blit(self.image, self.pos)
        pygame.display.flip()
        self.damage = 10
        self.area = 100
        self.speed = 30

    def get_dam(self):
        return self.damage

    def draw(self):
        window_surface.blit(self.image, self.pos)



class magic(Tower):
    def __init__(self, pos):
        super().__init__(pos)
        self.ammo = pygame.transform.scale(pygame.image.load('C:/TESTpy/PyDefence/pics/effects/Magic.png'), (30, 10))
        self.image = pygame.image.load('C:/TESTpy/PyDefence/pics/magic.png')
        x, y = self.image.get_size()
        kof_x, kof_y = x / window_size[0], y / window_size[1]
        self.image = pygame.transform.scale(self.image, (x / kof_x - 1760, y / kof_y - 875))
        window_surface.blit(self.image, self.pos)
        pygame.display.flip()
        self.damage = 25
        self.area = 80
        self.speed = 15

    def get_dam(self):
        return self.damage

    def draw(self):
        window_surface.blit(self.image, self.pos)


class martira(Tower):
    def __init__(self, pos):
        super().__init__(pos)
        # self.area = x
        self.ammo = pygame.transform.scale(pygame.image.load('C:/TESTpy/PyDefence/pics/effects/Shell.png'), (30, 10))
        self.explosion = pygame.transform.scale(pygame.image.load('C:/TESTpy/PyDefence/pics/effects/Explotion.png'),
                                                (160, 170))
        self.image = pygame.image.load('C:/TESTpy/PyDefence/pics/martira.png')
        x, y = self.image.get_size()
        kof_x, kof_y = x / window_size[0], y / window_size[1]
        self.image = pygame.transform.scale(self.image, (x / kof_x - 1770, y / kof_y - 930))
        window_surface.blit(self.image, self.pos)
        pygame.display.flip()
        self.center = pos
        self.damage = 10
        self.area = 100
        self.speed = 20

    def get_dam(self):
        return self.damage

    def draw(self):
        pygame.draw.circle(window_surface, 'red', self.center, self.area, 3)
        window_surface.blit(self.image, self.pos)