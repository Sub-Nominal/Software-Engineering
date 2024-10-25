'''class ContactInformation:
    def __init__(self, First, Last, Email, Pn, ):
        self.first = First
        self.last = Last
        self.email = Email
        self.phone = Pn
        self.country = None
p1 = ContactInformation("Jim", 'Jones', 'jj@mail.com', 12345)
p2 = ContactInformation('John', 'Paul', 'jp@jones.com', 11776)'''

'''class rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def changeposition(x2, y2):
        rectangle.x = x2
        rectangle.y = y2
    def getposition(x, y):
        print(x, y)

    def area(x, y):
        a = x*y
        print(a)'''

'''class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception('Member Not In Group')
        
    def getmembers(self):
        return sorted(self.members)
    
    def merge(self, obj2):
        g3 = self.members + obj2.members
        return g3
    
g1 = Group('a',['jim','John'])
g2 = Group('b',['amy','sam'])
print(g1.merge(g2))'''


'''class employee:
    num = 0
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.avage = age
        self.avsal = salary

    @classmethod
    def averagesalary(cls):
        avsal = e1.salary +e2.salary
        avsal = avsal/2
        return avsal

    @classmethod
    def averageage(cls):
        avage = e1.age + e2.age
        avage = avage/2
        return avage
    
e1 = employee('Sarah', 23, 6000)
e2 = employee('jim', 26, 8000)
print(employee.averageage())
print(employee.averagesalary())'''

class Temperature:
    def __init__(self, kelvin):
        self.kelivn = kelvin
        self.mintemp = 0
        self.maxtemp = 1000
        if self.mintemp > self.maxtemp:
            raise Exception('Invalid Temperature')
        if self.mintemp> kelvin >self.maxtemp:
            raise Exception('Invalid Temperature')

    def updatemin(self, newmin):
        self.mintemp = newmin
        if self.mintemp > self.maxtemp:
            raise Exception('Invalid Temperature')
        return self.mintemp
    
    def updatemax(self, newmax):
        self.maxtemp = newmax
        if self.mintemp > self.maxtemp:
            raise Exception('Invalid Temperature')
        return self.maxtemp
t = Temperature(86)
t.updatemax(800)
t.updatemin(50)

'''class Animal:
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height

class Mammal(Animal):
    def __init__(self, age, weight, height, sex):
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        
        


class reptile(Animal):
    def __init__(self, age, weight, height, legs):
        self.age = age
        self.weight = weight
        self.height = height
        self.legs = 4

class monkey(reptile):
    def __init__(self, age, weight, height, colour):
        self.age = age
        self.weight = weight
        self.height = height
        self.fingers = 5
        self.colour = colour

class lizard(monkey):
    def __init__(self, age, weight, height, colour):
        self.age = age
        self.weight = weight
        self.height = height
        self.colour = colour
        self.tail = True'''