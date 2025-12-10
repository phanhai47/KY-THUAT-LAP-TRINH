print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")
from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry("350x100")
# 1. Widget Label để hiển thị thông báo phím bấm
lbl_key = Label(window, text="Bấm phím bất kỳ trên cửa sổ này!", font=("Arial", 12))
lbl_key.grid(column=0, row=0, padx=10, pady=10)
# 2. Hàm xử lý sự kiện phím bấm
def key_pressed(event):
    # event.char là ký tự tương ứng với phím được bấm
    key_info = f"Bạn đã bấm phím: {event.char}"
    lbl_key.configure(text=key_info)
# 3. Gắn sự kiện phím bấm cho cửa sổ
window.bind("<Key>", key_pressed)

window.mainloop()
