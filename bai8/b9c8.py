print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")
import tkinter as tk
from tkinter import ttk, messagebox
# Hàm xử lý khi nút bấm được nhấn
def show_radio_choice():
    """Lấy giá trị từ Radio Button đang chọn và hiển thị ra hộp thoại."""
    # Lấy giá trị hiện tại của biến kiểm soát 'v'
    choice = v.get()
    # Hiển thị thông tin lựa chọn
    message = f"Thông tin nút radio button đang lựa chọn: {choice}"
    messagebox.showinfo("Lựa Chọn", message)
def create_radio_button_form():
    global v
    # Khởi tạo cửa sổ
    root = tk.Tk()
    root.title("Welcome")
    # Khung (Frame) để giữ các widget cùng nhau
    radio_frame = ttk.Frame(root)
    radio_frame.pack(padx=10, pady=10)
    # Biến kiểm soát (Control Variable) cho Radio Button
    v = tk.IntVar()
    v.set(1)   # Đặt giá trị mặc định là 1 (First)
    # Định nghĩa các lựa chọn (text hiển thị và value số)
    choices = [("First", 1), ("Second", 2), ("Third", 3)]
    # Tạo và đặt các Radio Button
    for text, val in choices:
        ttk.Radiobutton(
            radio_frame,
            text=text,
            variable=v,
            value=val
        ).pack(side=tk.LEFT, padx=5)  # side=tk.LEFT để đặt các nút theo hàng ngang
    # Nút "Click Me"
    click_me_btn = ttk.Button(radio_frame, text="Click Me", command=show_radio_choice)
    click_me_btn.pack(side=tk.LEFT, padx=10)
    root.mainloop()
if __name__ == "__main__":
    create_radio_button_form()
