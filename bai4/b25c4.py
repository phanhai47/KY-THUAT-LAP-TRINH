print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def loc_so_le():
    chuoi_so = input("Nhap chuoi so nguyen: ")
    ds_chuoi_so = chuoi_so.split()
    ds_so_le = []

    for chuoi_so_hien_tai in ds_chuoi_so:
        try:
            so = int(chuoi_so_hien_tai)
            if so % 2 != 0:
                ds_so_le.append(so)
        except ValueError:
            continue
    print("Cac so le trong chuoi la:", ds_so_le)

loc_so_le()