print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import turtle

window = turtle.Screen()
window.bgcolor("lightblue")
# Tạo con rùa để vẽ
painter = turtle.Turtle()
painter.color('red', 'yellow')
painter.pensize(2)
# Hàm vẽ hình vuông
def drawsq(t, s):
    t.begin_fill()
    for i in range(4):
        t.forward(s)
        t.left(90)
    t.end_fill()

for i in range(18):
    painter.left(20)
    drawsq(painter, 100)
window.mainloop()
