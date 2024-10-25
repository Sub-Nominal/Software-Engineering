import pygame
BLACK = (0,0,0)
BLUE = (0,0,255)

class Hero:
    def __init__(self):
        self.x = 540
        self.y = 1080
        self.xspeed = 0
        self.yspeed = 0
        self.width = 60
        self.height = 20
        self.score = 0
        self.color = BLUE
    def setxspeed(self, speed):
        self.xspeed = speed
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.width, self.height])
    def incrscore(self):
        self.score +=1
    def move(self):
        self.x = self.x +self.xspeed
        if self.x >1080:
            self.x = 1080
        if self.x <0:
            self.x = 0