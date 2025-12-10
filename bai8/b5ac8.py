print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import tkinter as tk
# 1. Xây dựng cửa sổ gốc (root)
root = tk.Tk()
root.title("Radio Button Demo")
# 2. Tạo một biến kiểm soát (Control Variable) để lưu trữ lựa chọn
v = tk.IntVar()
# Khởi tạo giá trị ban đầu là 1 (tương ứng với Python)
v.set(1)
# 3. Định nghĩa danh sách các lựa chọn (text và value)
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]
# 4. Phương thức xử lý sự kiện (command)
def ShowChoice():
    """In ra giá trị (value) của Radio Button hiện đang được chọn."""
    # Lấy giá trị hiện tại của biến kiểm soát v
    print(f"Giá trị đã chọn: {v.get()}")
# 5. Thêm Label tiêu đề
tk.Label(
    root,
    text="Chọn ngôn ngữ lập trình yêu thích của bạn:",
    justify=tk.LEFT,      # Căn lề trái
    padx=20               # Đệm theo trục x là 20px
).pack()
# 6. Tạo và đóng gói các Radio Button trong một vòng lặp
for text, val in languages:
    tk.Radiobutton(
        root,
        text=text,            # Tên hiển thị trên nút
        padx=20,              # Đệm theo trục x
        variable=v,           # Liên kết với biến kiểm soát chung
        command=ShowChoice,   # Gọi hàm khi nút được chọn
        value=val             # Giá trị gán cho nút này khi được chọn
    ).pack(anchor=tk.W)       # Hiển thị nút và căn lề trái (West)
# 7. Vòng lặp chính để hiển thị cửa sổ
root.mainloop()