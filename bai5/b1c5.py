print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import mymath
import mymath as mt

values = [2,4,6,8,10]

print("dung modelu mymath")
print('squares:')
for v in values:
    print(f'square({v}) = {mymath.squae(v)}')

print('\n cubes:')
for v in values:
    print(f'cube({v}) = {mymath.cube(v)}')

print('\n average:'+str(mymath.aveage(values)) )
print('\n--- Dung module alias (mt)---')
print('squares of 2:', mt.squae(2))
print('cubes of 3:', mt.cube(3))