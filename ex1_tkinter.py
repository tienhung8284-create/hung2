from tkinter import *

root = Tk()                             # Tạo đối tượng root từ class Tk()
root.title('Free Fire')             # Dùng đối tượng root gọi phương thức title()
root.minsize(width=300,height=250)      # Dùng đối tượng root gọi phương thức minsize()
root.resizable(width=True,height=True)  # Dùng đối tượng root gọi phương thức resizable()
Label(root,text='Mày có muốn chết không ?',fg='Blue',font=('Helvetica 20 italic bold')).pack(pady=100)
Button(root,text='YES',command=root.quit).pack(side=RIGHT)
Button(root,text='Có',command=root.quit).pack(side=RIGHT)

def makecenter(root):
    root.update_idletasks()
    width = root.winfo_width()           # Lấy độ rộng cửa sổ chương trình
    height = root.winfo_height()            # Lấy chiều cao của cửa số chương trình
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
makecenter(root)
root.mainloop()                         # Dùng đối tượng root gọi phương thức mainloop()
