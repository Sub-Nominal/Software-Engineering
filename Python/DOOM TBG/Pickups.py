class Pickup:
    def __init__(self, name, des, heal):
        self.name = name
        self.description = des
        self.heal = heal
    def getname(self):
        return self.name
    def getdes(self):
        return self.description
    def describe(self):
        print(f"{self.name}, {self.description}")
class AtkBoost(Pickup):
    def __init__(self, name, des, atk):
        super().__init__(name, des, atk)