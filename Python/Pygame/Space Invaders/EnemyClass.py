import pygame, random
BLACK = (0,0,0)
GREEN = (0,255,0)

class Enemy:
    def __init__(self):
        self.x = random.randint(0, 600)
        self.y = 0
        self.xspeed = 0
        self.yspeed = random.randint(1,2)
        self.width = 60
        self.height = 60
        self.color = GREEN
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.width, self.height])
    def move(self):
        self.y = self.y +self.yspeed
    def sensecollide(self, bullet, player):
        if abs(self.x - bullet.x) < 60:
            if abs(self.y - bullet.y) < 60:
                print('COLLIDE')
                self.x = -100
                self.y = -100
                bullet.x = -200
                bullet.y = -200
                player.incrscore()
                print(f"Score: {player.score}")