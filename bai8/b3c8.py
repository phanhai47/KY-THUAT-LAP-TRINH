print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import turtle
window = turtle.Screen()
window.bgcolor("white")
window.title("hoa van hinh tron")

painter = turtle.Turtle()
painter.pensize(2)
painter.speed(0)

colors = ["red","green","blue"]

angle_per_circle = 360/18

for i in range(18):
    current_color=colors[i%3]
    painter.pencolor(current_color)
    painter.circle(80)
    painter.left(angle_per_circle)
window.mainloop()