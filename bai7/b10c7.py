print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")
import re  # Thư viện cho biểu thức chính quy

def find_longest_words(file_path):
    """Tìm và in ra những từ có độ dài lớn nhất trong tệp."""
    longest_length = 0
    longest_words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Tách nội dung thành các từ, loại bỏ dấu câu - chuyển hết về chữ thường
        words = re.findall(r'\b\w+\b', content.lower())
        if not words:
            print("Tệp không chứa từ nào.")
            return
        for word in words:
            word_length = len(word)

            # Nếu tìm thấy từ dài hơn → reset danh sách
            if word_length > longest_length:
                longest_length = word_length
                longest_words = [word]

            # Nếu bằng độ dài max → thêm vào danh sách
            elif word_length == longest_length:
                if word not in longest_words:  # tránh trùng lặp
                    longest_words.append(word)

        print(f"Độ dài của từ dài nhất là: {longest_length} ký tự.")
        print("Các từ dài nhất là:")
        for word in longest_words:
            print(f"- {word}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ dùng
find_longest_words("c.txt")
