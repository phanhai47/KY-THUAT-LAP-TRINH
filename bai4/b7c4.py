print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

S = input("Nhap chuoi co lan so ")
S_moi =""

for ch in S:
    if not ch.isdigit():
        S_moi += ch
print("Chuoi moi la: ", S_moi)