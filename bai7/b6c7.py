print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def read_last_n_nines(file_path, n):
    try:
        #doc tat ca ca dong
        with open(file_path, 'r', encoding='utf-8') as f:
            all_lines=f.readlines()
        #lay n dong cuoi cung
        #neu n lon hon so dong thi lay toang bo
        last_n_line=all_lines[-n:]
        #in cac dong cuoi ra man hinh
        for line in last_n_line:
            print(line,end='')
    except FileNotFoundError:
        print(f"khong tin thay file tai duong dan")
    except Exception as e:
        print(f"da xay ra loi: {e}")
file_duong_dan = "b.txt"
so_dong=3
read_last_n_nines(file_duong_dan,so_dong)