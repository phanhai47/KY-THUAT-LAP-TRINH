print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def dem_chu_cai_va_chu_so():
    cau = input("Nhap cau o: ")

    so_chu_cai = 0
    so_chu_so = 0

    for ky_tu in cau:
        if ky_tu.isalpha():
            so_chu_cai += 1
        elif ky_tu.isdigit():
            so_chu_so += 1
    
    print("So chu cai trong cau la:", so_chu_cai)
    print("So chu so trong cau la:", so_chu_so)

dem_chu_cai_va_chu_so()