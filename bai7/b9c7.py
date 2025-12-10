print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import shutil
def copy_file_contents(source_path, destination_path):
    #sao chep noi dung tu tep nguon sang tep dich
    try:
        shutil.copyfile(source_path, destination_path)
        print(f"da sao chep thang cong tu:")
        print(f"Nguon : {source_path}")
        print(f"Dich : {destination_path}")
    except FileNotFoundError:
        print("khong tin thay duong dan hop le")
    except Exception as e:
        print(f"da xay ra loi trong qua trinh sao chep: {e}")
copy_file_contents("a.txt","b.txt")