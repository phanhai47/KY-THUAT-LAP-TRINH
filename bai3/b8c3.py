print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import math

pos = [0, 0]

while True:
    s = input().strip()
    if s == "":
        break

    try:
        direction, step = s.split()
        direction = direction.upper()
        step = int(step)
    except:
        continue

    if direction == "UP":
        pos[1] += step
    elif direction == "DOWN":
        pos[1] -= step
    elif direction == "LEFT":
        pos[0] -= step
    elif direction == "RIGHT":
        pos[0] += step

distance = math.sqrt(pos[0]**2 + pos[1]**2)
print(round(distance))
