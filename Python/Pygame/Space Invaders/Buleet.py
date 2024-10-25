import pygame
BLACK = (0,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xspeed = 0
        self.yspeed = -8
        self.width = 10
        self.height = 20
        self.color = WHITE
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.width, self.height])
    def move(self):
        self.y = self.y +self.yspeed