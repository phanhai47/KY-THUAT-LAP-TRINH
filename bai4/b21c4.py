print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def kiem_tra_chia_het_cho_5():
    chuoi_nhap = input("Nhap vao mot chuoi nhi phan co 4 chu so: ")
    ds_nhi_phan = chuoi_nhap.split()

    ds_chia_het_5 = []
    for so_nhi_phan in ds_nhi_phan:
        so_nhi_phan_cat = so_nhi_phan.strip()

        if len(so_nhi_phan_cat) != 4 or not all(bit in '01' for bit in so_nhi_phan_cat):
            continue
        gia_tri_thap_phan = int(so_nhi_phan_cat, 2)

        if gia_tri_thap_phan % 5 == 0:
            ds_chia_het_5.append(so_nhi_phan_cat)
    
    print("Cac so nhi phan chia het cho 5 la: ", ' '.join(ds_chia_het_5))
kiem_tra_chia_het_cho_5()
