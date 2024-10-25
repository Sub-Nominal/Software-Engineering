class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    def speak(self):
        print("I don't know")
class cat(Pet):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print('Meow')
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
class dog(Pet):
    def speak(self):
        print('Bark')
d = dog('Jim', 4)
c = cat('Bob', 12, 'Blue')
d.show()
c.show()