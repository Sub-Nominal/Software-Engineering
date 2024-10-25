class jar:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        if capacity <= 0: 
            raise ValueError()
    
    def __str__(self):
        return str(self.count*'🍪')
    
    def deposit(self, newcount):
        self.count +=newcount
        if self.count > self.capacity:
            raise ValueError("HEY, Can I have some??")
    
    def withdraw(self, withdrawl):
        self.count -= withdrawl
        if withdrawl > self.count:
            raise ValueError("Where are you getting all those cookies from??")
    
    def cap(self):
        return self.capacity
    
    def size(self):
        return self.count

j1 = jar(5)
print(j1.cap())
j1.deposit(3)
print(j1.__str__())
print(j1.size())
j1.withdraw(7)