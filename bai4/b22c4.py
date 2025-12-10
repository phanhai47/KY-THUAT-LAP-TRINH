print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def kiem_tra_tat_ca_so_chan(n):
    chuo_so = str(so)
    for chu_so in chuo_so:
        if int(chu_so) % 2 != 0:
            return False
    return True
ds_ket_qua = []
for so in range(1000, 3001):
    if kiem_tra_tat_ca_so_chan(so):
        ds_ket_qua.append(str(so))
print(",".join(ds_ket_qua)) 