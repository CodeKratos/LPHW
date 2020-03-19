class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printu(self):
        print("Hello my name is:" +self.name)

class Games:
    def __init__(self,game,protagonist):
        self.game = game
        self.protagonist = protagonist
    def message(self):
        print(f" In {self.game}, {self.protagonist} is my favourit character")

        
p1 = Person("Akshay", 25) # p1 is a object whi
p1.printu()

g = Games("God of War","Kratos")
g.message()