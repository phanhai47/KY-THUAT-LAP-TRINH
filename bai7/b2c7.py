print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def count_file_stats(file_path):
    char_count=0
    word_count=0
    line_count=0
    try:
        with open(file_path,'r') as f:
            for line in f:
                line_count +=1
                char_count +=len(line)
                words = line.strip().split()
                word_count +=len(words)
        print(f"so ky tu bao gom khong trang va xuong giong la:{char_count}")
        print(f"so tu la: {word_count}")
        print(f"so dong la : {line_count}")
    except FileNotFoundError:
        print(f" khong tin thay file")
    except Exception as e:
        print(f"da xay ra loi: {e}")
file_duong_dan="a.txt"
count_file_stats(file_duong_dan)