class Item:
    def __init__(self, name):
        self.name = name
        self.description = None
        
    def getname(self):
        return self.name
    
    def setname(self, itname):
        self.name = itname
    
    def getdes(self):
        return self.description
    
    def setdes(self, des):
        self.description = des
    
    def describe(self):
        print(f"The {self.name} is here - {self.description}")