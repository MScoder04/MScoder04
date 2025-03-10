from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("Humans can walk.")

class snake(animal):
    def move(self):
        print("Snakes can slither.")

class kangaroo(animal):
    def move(self):
        print("Kangaroos can hop.")

obj=human()
obj.move()

obj=snake()
obj.move()

obj=kangaroo()
obj.move()