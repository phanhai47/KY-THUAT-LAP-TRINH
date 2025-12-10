print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import numpy as np
#dinh nghia kieu du lieu (dtype) cho mang cau truc
#S15: chuoi toi da 15 ky tu, int: so nguyen (lop), float: so thuc(chieu cao)
data_type = np.dtype([('name', 'S15'), ('calss', 'int'), ('height', 'float')])
#du lieu chi tiet cua sinh vien
student_details= [('Phan Dinh Hai', 4, 1.75),
                  ('Nguyen Van A', 5, 1.80),
                    ('Le Thi B', 5, 1.65),
                    ('Tran Van C', 4, 1.70)]
student = np.array(student_details, dtype=data_type)
print("original array: ")
print(student)
#sap xep theo 2 truong 'class' cap 1 va 'height' cap 2
print("\nsorted by class and height:")
sorted_student = np.sort(student, order=['calss', 'height'])
print(sorted_student)