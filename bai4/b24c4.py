print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def dem_chu_hoa_va_chu_thuong(s):
    cau=input("Nhap 1 cau: ")
    chu_hoa = 0
    chu_thuong = 0

    for char in cau:
        if char.isupper():
            chu_hoa += 1
        elif char.islower():
            chu_thuong += 1
    print("So chu hoa:", chu_hoa)
    print("So chu thuong:", chu_thuong)

dem_chu_hoa_va_chu_thuong("")         