import pygame
import Space_Hero
import Buleet
import EnemyClass
pygame.init()
BLACK =(0,0,0)
BLUE =(0,0,255)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
hero = Space_Hero.Hero()
enemies = []
bullets = []
for i in range(3): 
    enemy = EnemyClass.Enemy() 
    enemies.append(enemy)
game = True
counter = 0
spawnwait = 120
while game:
    spawnwait = 120-hero.score
    counter +=1
    if spawnwait <60:
        spawnwait = 60
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.setxspeed(-5)
            if event.key == pygame.K_RIGHT:
                hero.setxspeed(5)
            if event.key == pygame.K_SPACE:
                bullet = Buleet.Bullet(x = hero.x+25, y = hero.y)
                bullets.append(bullet)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                hero.setxspeed(0)
    screen.fill(BLACK)
    hero.draw(screen)
    hero.move()
    enemy.draw(screen)
    enemy.move()
    if counter % spawnwait ==0:
        enemy = EnemyClass.Enemy() 
        enemies.append(enemy)
    for e in enemies:
        e.draw(screen)
        e.move()
        for b in bullets:
            e.sensecollide(b, hero)
    for b in bullets:
        b.draw(screen)
        b.move()
        
    pygame.display.flip()
    clock.tick(120)