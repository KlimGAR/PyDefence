#    def __init__(self, pos, way):
#        self.hp = 20
#        super().__init__(pos, way, self.hp)
#        self.im = (
#            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Green/Green slime 4.png'),
#            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Green/Green slime 3.png'),
#            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Green/Green slime 1.png')
#        )
#        self.im = [pygame.transform.scale(i, self.size) for i in self.im]
#        self.cost = 1
#        self.speed = 40
#        window_surface.blit(self.im[self.direction], (self.pos[0] - self.size[0] // 2, self.pos[1] - self.size[1] // 2))
#        pygame.draw.line(window_surface, 'red', (self.pos[0] - self.size[0] // 2, self.pos[1] - self.size[1] // 2 - 10),
#                         (self.pos[0] - self.size[0] // 2 + self.hp, self.pos[1] - self.size[1] // 2 - 10), 5)