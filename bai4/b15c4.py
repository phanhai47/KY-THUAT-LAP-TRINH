print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

chuoi_nhap=input("Nhap chuoi cac tu tieng anh: ")
ds_tu=chuoi_nhap.split()

ds_tu.sort()

print(",".join(ds_tu))