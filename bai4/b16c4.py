print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

chuoi_nhi_phan = input("Nhap chuoi nhi phan: ")

ds_nhi_phan = chuoi_nhi_phan.split(" ")

ds_thap_phan = []
for so_nhi_phan in ds_nhi_phan:
    try:
        gia_tri_thap_phan = int(so_nhi_phan.strip(), 2)
        ds_thap_phan.append(str(gia_tri_thap_phan))
    except ValueError:
        pass

print("," .join(ds_thap_phan))