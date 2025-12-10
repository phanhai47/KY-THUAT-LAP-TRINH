print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import turtle
import random

colors = ["red","green","blue","orange","purple","pink","yellow"]

window = turtle.Screen()
window.bgcolor("white")

painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0)
for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)

    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0,0)
window.mainloop()