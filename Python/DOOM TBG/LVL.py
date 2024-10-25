class Level:
    def __init__(self, lvlnum, roomnum, descript, lvlname):
        self.name = lvlname
        self.lvlnum = lvlnum
        self.roomnum = roomnum
        self.description = descript
        self.moves = {}
        self.pickup = None
        self.character = None
    def getname(self):
        return self.name
    def getlvlnum(self):
        return self.lvlnum
    def describe(self):
        print(self.description)
    def move(self, direction):
        if direction in self.moves:
            return self.moves[direction]
        else:
            print("Blocked")
            return self
    def setmoves(self, nextroom, direction):
        self.moves[direction] = nextroom
        
    def getmoves(self):
        for direction in self.moves:
            room = self.moves[direction]
            print(f"{room.getname()} is {direction}")
        
    def setpickup(self, pickup):
        self.pickup = pickup
    def getpickup(self):
        return self.pickup
    def setchar(self, character):
        self.character = character
    def getchar(self):
        return self.character