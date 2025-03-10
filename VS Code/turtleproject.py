import turtle
turtle.Screen().bgcolor("pink")
sc=turtle.Screen()
sc.setup(400,300)
turtle.title("Turtle Project")
t=turtle.Turtle()

t.begin_fill()
t.fillcolor("blue")
t.color("blue")
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.forward(150)
t.pendown()

t.begin_fill()
t.fillcolor("purple")
t.color("purple")
for i in range(6):
    t.forward(100)
    t.left(60)
t.end_fill()
turtle.done()