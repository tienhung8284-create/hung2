from tkinter import *

def ContinueAction():
    hesoa.set('')
    hesob.set('')
    ketqua.set('')


root = Tk()


hesoa = StringVar()
hesob = StringVar()
ketqua = StringVar()

def Cong():
    a = float(hesoa.get())
    b = float(hesob.get())
    ketqua.set(a+b)
def Tru():
    a = float(hesoa.get())
    b = float(hesob.get())
    ketqua.set(a-b)
def Nhan():
    a = float(hesoa.get())
    b = float(hesob.get())
    ketqua.set(a*b)
def Chia():
    a = float(hesoa.get())
    b = float(hesob.get())
    ketqua.set(a/b)
def amub():
    a = float(hesoa.get())
    b = float(hesob.get())
    ketqua.set(a**b)
def module():
    a = float(hesoa.get())
    b = float(hesob.get())
    ketqua.set(a%b)
def chialayphanguyen():
    a = float(hesoa.get())
    b = float(hesob.get())
    ketqua.set(a//b)

root.title('Làm phép toán')
root.minsize(width=400,height=200)
Label(root,text='Cộng trừ nhân chia',fg='green',font='Tahooma 20 bold').grid(row=0,columnspan=4)

def makecenter(root):
    root.update_idletasks()
    width = root.winfo_width()           # Lấy độ rộng cửa sổ chương trình
    height = root.winfo_height()            # Lấy chiều cao của cửa số chương trình
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
makecenter(root)

frame = Frame()
Button(frame,text='Cộng',command=Cong).pack(side=TOP,fill=X)
Button(frame,text='Trừ',command=Tru).pack(side=TOP,fill=X)
Button(frame,text='Nhân',command=Nhan).pack(side=TOP,fill=X)
Button(frame,text='Chia',command=Chia).pack(side=TOP,fill=X)

frame.grid(row=1,column=0,rowspan=4)

frame = Frame()
Button(frame,text='a mũ b',command=amub).pack(side=TOP,fill=X)
Button(frame,text='Module',command=module).pack(side=TOP,fill=X)
Button(frame,text='Chia lấy phần nguyên',command=chialayphanguyen).pack(side=TOP,fill=X)
frame.grid(row=1,column=5,rowspan=4)

Label(root,text='Hệ số a').grid(row=1,column=1)
Entry(root,width=15,textvariable=hesoa).grid(row=1,column=2)
Label(root,text='Hệ số b',).grid(row=2,column=1)
Entry(root,width=15,textvariable=hesob).grid(row=2,column=2)
Label(root,text='Kết Quả').grid(row=3,column=1)
Entry(root,width=15,textvariable=ketqua).grid(row=3,column=2)

frame = Frame()
Button(frame,text='Tiếp',command=ContinueAction).pack(side=LEFT,fill=X)
Button(frame,text='Thoát',command=quit).pack(side=LEFT,fill=X)
frame.grid(row=4,column=1,columnspan=2)


root.mainloop()





