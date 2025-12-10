print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import search_module
def get_list_and_item():
    #1.nhap danh sach
    data_input = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
    try :
        #chuyen doi chuoi nhap thanh danh sach so nguyen
        dlist = [int(x.strip()) for x in data_input.split(',')]
    except ValueError:
        print("Gia tri khong hop le. Vui long nhap lai.")
        return None, None
    #2.nhap gia tri can tim
    while True:
        try:
            item = int(input("Nhap gia tri can tim trong danh sach: "))
            break
        except ValueError:
            print("Gia tri khong hop le. Vui long nhap lai.")
    return dlist, item
#chuong trinh chinh

dlist, item = get_list_and_item()
if dlist is not None and item is not None:
    found_status, position = search_module.Sequential_Search(dlist, item)
    print(f"Danh sach da nhap: {dlist}")
    print(f"Gia tri can tim: {item}")
    if found_status:
        print(f"Tim thay {item} tai vi tri {position+1} trong danh sach.")
    else:
        print(f"Khong tim thay {item} trong danh sach.")