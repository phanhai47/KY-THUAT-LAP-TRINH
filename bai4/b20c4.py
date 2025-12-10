print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def tam_giac_pascal(n):
    if n <= 0:
        return []
    dong_truoc = [1]
    print(dong_truoc)
    for i in range(1, n):
        dong_hien_tai = [1]
        for j in range(1, len(dong_truoc)):
            dong_hien_tai.append(dong_truoc[j-1] + dong_truoc[j])
        dong_hien_tai.append(1)
        print(dong_hien_tai)
        dong_truoc = dong_hien_tai
try:
    n = int(input("Nhap so dong cua tam giac Pascal: "))
    tam_giac_pascal(n)  
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")

