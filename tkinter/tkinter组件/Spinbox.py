import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")
#绑定变量
v = tkinter.StringVar()

def updata():
    print(v.get())

#                                             步长 默认为1    values = (0,2,4,6,8)
sp =tkinter.Spinbox(win,from_ = 0,to = 100,increment = 5,textvariable = v,command = updata)
sp.pack()

v.set(20)
print(v.get())

win.mainloop()