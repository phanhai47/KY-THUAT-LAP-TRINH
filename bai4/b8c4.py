print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

ds = input("Danh sach cac tu").split()

tu_dai_nhat = ds[0]

for tu in ds[1:]:
    if len(tu) > len(tu_dai_nhat):
        tu_dai_nhat = tu
print("Tu dai nhat la:", tu_dai_nhat)