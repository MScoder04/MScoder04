class student:
    name = "Misha"
    grade = 9
    def intro(self):
        print("Hi I am a student")
    def details(self):
        print("My name is", self.name)
        print("I am in", self.grade, "th grade")
obj1=student()
obj1.intro()
obj1.details()
obj2=student()
obj2.intro()
obj2.details()
class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def intro(self):
        print("Hi I am a student")
    def details(self):
        print("My name is", self.name)
        print("I am in", self.grade, "th grade")
obj1=student("Misha", 9)
obj1.intro()
obj1.details()
obj2=student("Nyra", 3)
obj2.intro()
obj2.details()