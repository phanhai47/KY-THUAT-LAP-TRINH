print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")
def read_entire_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"khong tin thay file")
    except Exception as e:
        print(f"xay ra loi :{e}")
file_duong_dan = "a.txt"
read_entire_file(file_duong_dan)