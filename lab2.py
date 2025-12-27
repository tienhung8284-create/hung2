from tkinter import *

def ContinueAction():
    hesoa.set('')
    hesob.set('')
    ketqua.set('')

root = Tk()


hesoa = StringVar()
hesob = StringVar()
ketqua = StringVar()


root.title('Tiến Hùng')
root.minsize(width=400,height=400)
root.resizable(width=True,height=True)
Label(root,text='Cộng Trừ Nhân Chia',fg='blue',font='Helvetica 18',justify=CENTER).grid(row=0,column=2)

frmbtn = Frame()
Button(frmbtn,text='Cộng').pack(side=TOP,fill=X)
Button(frmbtn,text='Trừ').pack(side=TOP,fill=X)
Button(frmbtn,text='Nhân').pack(side=TOP,fill=X)
Button(frmbtn,text='Chia').pack(side=TOP,fill=X)
frmbtn.grid(row=1,column=0,rowspan=4)

Label(root,text='Hệ số a').grid(row=1,column=1)
Entry(root,width=15,textvariable=hesoa).grid(row=1,column=2)
Label(root,text='Hệ số b').grid(row=2,column=1)
Entry(root,width=15,textvariable=hesob).grid(row=2,column=2)
Label(root,text='Kết Quả').grid(row=3,column=1)
Entry(root,width=15,textvariable=ketqua).grid(row=3,column=2)

frmbtn = Frame()
Button(frmbtn,text='Tiếp',command=ContinueAction).pack(side=LEFT,fill=X)
Button(frmbtn,text='Thoát',command=quit).pack(side=LEFT,fill=X)
frmbtn.grid(row=4,column=1,columnspan=2)

root.mainloop()