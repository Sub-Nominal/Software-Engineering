import random
import math
import time

class Fighter:
    def __init__(self, name, health, weapon, shield):
        self.name = name
        self.__health = health
        self.weapon = weapon
        self.shield = shield
        
    def random_atk(self):
        attack_power = random.randint(math.floor(self.weapon/2), self.weapon*2)
        return attack_power
    
    def skill_atk(self):
        attack_power = random.randint(math.floor(self.weapon/2), self.weapon)
        target = random.randint(2,6)
        print(f"Hit enter in exactly {target} seconds")
        tic = time.time()
        input()
        toc = time.time()
        timetaken = toc-tic
        mult = 3- abs(target-timetaken)
        if mult <2:
            mult = 0
        print(f"Attack Power: {math.floor(attack_power)}")
        print(f"Multiplier: {math.floor(mult)}")
        return attack_power*mult
    
    def defend(self, attackpower):
        damage = attackpower - self.shield
        if damage >0:
            self.__health -= damage
            print(f"Damage: {math.floor(damage)}")
        else:
            print("No Damage")
    
    def report(self):
        print(f"{self.name}: Health: {math.floor(self.__health)}")
    
    def isdead(self):
        if self.__health <=0:
            return True
        else:
            return False
        
you = Fighter("Jim", 100, 50, 10)
troll = Fighter("Troll", 200, 25, 20)
while True:
    print('You attack the Troll')
    troll.defend(you.skill_atk())
    troll.report()
    time.sleep(2)
    if troll.isdead():
        print('You Win')
        break
    print(" ")
    print('The Troll attacks You')
    you.defend(troll.random_atk())
    you.report()
    time.sleep(2)
    if you.isdead():
        print('Troll Wins')
        break
    print(" ")
    
    