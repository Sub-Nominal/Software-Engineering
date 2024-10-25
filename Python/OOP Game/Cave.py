class Cave:
    def __init__(self, cavname):
        self.name = cavname
        self.description = None
        self.links = {}
        self.character = None
        self.item = None
    def getdes(self):
        return self.description

    def linkcaves(self, linkedcave, direction):
        self.links[direction] = linkedcave
    
    def setdes(self, cavedescript):
        self.description = cavedescript
    
    def describe(self):
        print(self.description)
        
    def getname(self):
        return self.name
        
    def getlinks(self):
        for direction in self.links:
            cave = self.links[direction]
            print("The " + cave.getname() + ' is ' +direction)
        print(self.getdes())
    
    def move(self, direction):
        if direction in self.links:
            return self.links[direction]
        else:
            print("You can't go that way")
            return self
    
    def setchar(self, character):
        self.character=character
    
    def getchar(self):
        return self.character
    
    def getitem(self):
        return self.item
    
    def setitem(self, item):
        self.item = item