print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")
import list_ops
def get_list_from_user():
    while True:
        try:
            cont = int(input("Nhap so phan tu trong danh sach: "))
            if cont <= 0:
                print("Vui long nhap so nguyen duong.")
                continue
            break
        except ValueError:
            print("Gia tri khong hop le. Vui long thu lai.")
    my_list = []
    print("Nhap cac gia tri so ngyuen hoac so thuc:")
    for i in range(cont):
        while True:
            try:
                value = float(input(f"Gia tri thu {i+1}: "))
                my_list.append(value)
                break
            except ValueError:
                print("Gia tri khong hop le. Vui long nhap lai.")
    return my_list

#1.nhap danh sach 
data_list = get_list_from_user()
#2.Su dumg model de tim min,max
min_val,max_val = list_ops.find_min_max(data_list)
#su dung modelu de tim vi tri cua min,max
min_index, max_index = list_ops.find_min_max_index(data_list, min_val, max)
#3.in ket qua
print(f"dand sach da nhap: {data_list} ")
if min_val is not None and max_val is not None:
    print(f"Gia tri nho nhat: {min_val} tai vi tri {min_index}")
    print(f"Gia tri lon nhat: {max_val} tai vi tri {max_index}")