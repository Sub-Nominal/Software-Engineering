import time
class Player:
    def __init__(self, name, description, hp, atk):
        self.name = name
        self.description = description
        self.hp = hp
        self.atk = atk
        self.pickups = []
    def getname(self):
        return self.name
    def describe(self):
        print(self.description)
    def getatk(self):
        return self.atk
    def setatk(self, newatk):
        self.atk = newatk
    def gethp(self):
        return self.hp
    def setph(self, newhp):
        self.hp = newhp
    def getpickup(self, pickup):
        self.pickups.append(pickup)
        print(F"{self.name} picked up {pickup.name}")
    def healplayer(self, pickup):
        self.hp += pickup.heal
        print(f"{self.name} uses {pickup.name} to heal {pickup.heal} HP")
    def atkboost(self, atkboost):
        self.atk += atkboost.atk

class Enemy(Player):
    def getfightinfo(self, player):
        print(f"Player health is: {player.gethp()}")
        print(f"Player attack is: {player.getatk()}")
        print(f"{self.name} health is: {self.gethp()}")
        print(f"{self.name} attack is: {self.getatk()}")
    def __init__(self, name, description, hp, atk):
        super().__init__(name, description, hp, atk)
    def fight(self, player):
        print(f"{player.name} is fighting {self.name}")
        time.sleep(1)
        while self.hp !=0:
            self.getfightinfo(player)
            self.hp = self.hp -player.atk
            player.hp = player.hp - self.atk
            print(f"Player health is: {player.gethp()}")
            print(f"{self.name} health is: {self.gethp()}")
            time.sleep(1)
        if player.hp <=0:
            print(F"{player.name} died")
            print(F"")
        if self.hp <=0:
            print(f"{player.name} won")
            print(f"{self.name} crawls back to Hell")