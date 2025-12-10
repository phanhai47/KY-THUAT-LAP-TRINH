print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")
from tkinter import *
from tkinter import messagebox
# --- Định nghĩa các phương thức xử lý sự kiện ---
def OpenFile():
    messagebox.showinfo("Chức năng File", "Thực hiện chức năng Mở/Tạo File mới!")
def Exit():
    if messagebox.askyesno("Thoát", "Bạn có chắc chắn muốn thoát ứng dụng không?"):
        root.quit()
def InsText():
    messagebox.showinfo("Chèn", "Thực hiện chức năng Chèn Văn bản.")
def InsPic():
    messagebox.showinfo("Chèn", "Thực hiện chức năng Chèn Hình ảnh.")
def About():
    messagebox.showinfo("Về Ứng Dụng", "Đây là ứng dụng Tkinter Menu Demo.")
# --- Xây dựng cấu trúc Menu ---
root = Tk()
root.title("tk")
root.geometry("300x150")  # Đặt kích thước dễ nhìn
# 1. Tạo Menu Bar chính
menu = Menu(root)
root.config(menu=menu)
# 2. Menu File
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=OpenFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)
# 3. Menu Insert
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)
# 4. Menu Help
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.mainloop()
