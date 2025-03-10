class parrot:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
obj1=parrot("pierre", 3)
print(obj1.sing("happy"))