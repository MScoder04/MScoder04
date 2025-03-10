class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("My name is {}".format(self.name),"and I am {} years old".format(self.age))
    def makeSound(self):
        print("Meow")

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("My name is {}".format(self.name),"and I am {} years old".format(self.age))
    def makeSound(self):
        print("Bark")

obj1=cat("Fluffy", 5)
obj2=dog("Rufus", 4)
for animal in (obj1,obj2):
    animal.info()
    animal.makeSound()