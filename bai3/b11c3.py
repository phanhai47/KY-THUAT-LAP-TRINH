print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def benefit(t, n, k):
    lai_suat_thap_phan = t / 100.0
    tong_tien_nhan_duoc = n * ((1 + lai_suat_thap_phan) ** k)
    return tong_tien_nhan_duoc


def nhap_du_lieu(ten_bien, kieu):
    while True:
        try:
            gia_tri = kieu(input(f"Nhap {ten_bien}: "))

            if gia_tri < 0 and ten_bien != "lai suat t (% thang)":
                print(f"{ten_bien} phai la so duong. Vui long nhap lai!")
                continue

            if ten_bien == "so thang gui k" and gia_tri != int(gia_tri):
                print(f"{ten_bien} phai la so nguyen. Vui long nhap lai!")
                continue
            
            return gia_tri
        
        except ValueError:
            print(f"Gia tri khong hop le. Vui long nhap lai!")

t_lai_suat = nhap_du_lieu("lai suat t (% thang)", float)
n_so_tien_gui = nhap_du_lieu("so tien gui n (VND)", float)
k_so_thang_gui = nhap_du_lieu("so thang gui k", float)

tong_tien = benefit(t_lai_suat, n_so_tien_gui, k_so_thang_gui)
tien_lai = tong_tien - n_so_tien_gui

print("\n" + "=" * 40)
print("KET QUA TIEN GUI TIET KIEM")
print(f"Von ban dau(n): {n_so_tien_gui:,.0f} VND")
print(f"Lai suat thang(t): {t_lai_suat:.2f} %")
print(f"So thang gui(k): {k_so_thang_gui:.0f} thang")
print("=" * 40)
print(f"Tong tien nhan duoc: {tong_tien:,.0f} VND")
print(f"So tien lai nhan duoc: {tien_lai:,.0f} VND")
print("=" * 40)
