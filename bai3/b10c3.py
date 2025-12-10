print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import math
def tinh(R):
    if R < 0:
        return "Ban kinh khong hop le"
    else:
        chuvi = 2 * math.pi * R
        dientich = math.pi * R * R
        return chuvi, dientich
while True:
    try:
        R_input = input("Nhap ban kinh R: ")
        R = float(R_input)
        break
    except ValueError:
        print("Vui long nhap mot so hop le cho ban kinh R.")
ketqua = tinh(R)

if ketqua is not None:
    chuvi, dientich = ketqua
    print("voi ban kinh R =", R)
    print(f"Chu vi hinh tron: {chuvi:.2f}")
    print(f"Dien tich hinh tron: {dientich:.2f}")
    print("_"*30)

