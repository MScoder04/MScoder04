class rectangle:
    def __init__(self,name):
        self.name=name
    def info(self):
        print("The formula for a {}".format(self.name),"is:")
    def formula(self):
        print("length x width")

class square:
    def __init__(self,name):
        self.name=name
    def info(self):
        print("The formula for a {}".format(self.name),"is:")
    def formula(self):
        print("length x width")

obj1=rectangle("rectangle")
obj2=square("square")
for animal in (obj1,obj2):
    animal.info()
    animal.formula()