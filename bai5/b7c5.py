print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import numpy as np
#dinh nghia kieu du kieu(dtype)cho mang co cau truc
#s15: chuoi so co toi da 15 ky tu int ,float 
data_type=[('name','S15'),('class','int'),('height','float')]

#du lieu chi tiet cua sinh vien 
student_details = [
    ('james', 5, 55.9),
    ('nail', 6, 51.7),
    ('paul', 5, 45.8),
    ('pit', 5, 40.5)]
#tao mang co cau truc
students=np.array(student_details,dtype=data_type)
print("original array:")
print(students)
#sap xep mang theo chieu tang dan cua truong height
print("sorted array by height:")
sorted_by_height = np.sort(students, order='height')
print(sorted_by_height) 