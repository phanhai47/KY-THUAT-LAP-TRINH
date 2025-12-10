print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def write_list_to_file(file_path, data_list):
    try:
        #che do ghi "w"
        with open(file_path, 'w', encoding='utf-8') as f:
            for item in data_list:
                f.write(item + '\n')
        print(f"da ghi {len(data_list)} muc tu danh sach vao tep :{file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            print("\n noi dung da ghi:")
            print(f.read())
    except FileNotFoundError:
        print(f"khong tin thay file tai duong dan")
    except Exception as e:
        print(f"da xay ra loi: {e}")
shopping_list = ["trung","sua tuoi","rau xanh"]
write_list_to_file("shopping_list.txt",shopping_list)