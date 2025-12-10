print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def tinh_tong_uoc(n):
    tong = 0
    for i in range(1, n ):
        if n % i == 0:
            tong += i
    return tong

def tim_so_co_tong_uoc_lon_hon_chinh_no():
    try:
        n = int(input("Nhap so nguyen duong n: "))
        if n <= 0:
            print("n phai la so nguyen duong!")
            return
    except ValueError:
        print("Vui long nhap mot so nguyen duong.")
        return

    print(f"Cac so <= {n} co tong uoc lon hon chinh no:")
    for so in range(1, n + 1):
        if tinh_tong_uoc(so) > so:
            print(so)

tim_so_co_tong_uoc_lon_hon_chinh_no()
