class dad:
    def __init__(self,eye,personality):
        self.eye=eye
        self.personality=personality
    def display(self):
        print("Your eye color is", self.eye)
        print("Your personality is", self.personality)

class son(dad):
    def __init__(self,eye,personality,name, age):
        self.name=name
        self.age=age
        super().__init__(eye, personality)

obj=son("brown","nice","Bob",15)
obj.display()