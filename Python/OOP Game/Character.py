class Character():
    def __init__(self, chname, des):
        self.name = chname
        self.description = des
        self.conversation = None
    
    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)
    
    def setconvo(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation is not None:
            print(f"{self.name} says {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")
    
    def fight(self, weapon):
        print(f"{self.name} doesn't want to fight with you")
        return True
    
class Enemy(Character):
    enemiestodefeat=0
    def __init__(self, chname, des):
        super().__init__(chname, des)
        self.weakness = None
        Enemy.enemiestodefeat =Enemy.enemiestodefeat +1
        
        
    def setweak(self, weakness):
        self.weakness = weakness 
    
    def getweak(self):
        print(self.weakness)
        
    def fight(self, weapon):
        if weapon == self.weakness:
            print(f"You fend {self.name} off with the {weapon}")
            Enemy.enemiestodefeat = Enemy.enemiestodefeat-1
            return True
        else:
            print(f"{self.name} swallows you, little wimp")
            return False
    
    def steal(self):
        print(f"You steal from {self.name}")
        
class Friend(Character):
    def __init__(self, chname, des):
        super().__init__(chname, des)
        self.feeling = None
    
    def pat(self):
        print(f"{self.name}  pats you back!")
