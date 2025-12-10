print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def reverse_file_contents(file_path):
    #doc va in noi dung tung dong theo thu tu dao nguoc
    try:
        with open(file_path, 'r') as input_file:
            for line in input_file:
                reversed_line = line.rstrip('\n')[::-1]
                print(reversed_line)  
    except FileNotFoundError:
        print(f"loi ko tin thay file tai duong dan")
    except Exception as e:
        print(f"da xay ra loi: {e}")
file_duong_dan ="a.txt"
reverse_file_contents(file_duong_dan) 