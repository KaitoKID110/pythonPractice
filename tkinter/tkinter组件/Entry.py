import tkinter

win = tkinter.Tk()
win.title("第一个tkinter窗口")
win.geometry("400x400+700+200")

e = tkinter.Variable()

#show 密文显示
entry = tkinter.Entry(win,textvariable = e)
entry.pack()

#设置值
e.set("sunck is a good man")
#取值
print(e.get())
print(entry.get())

win.mainloop()
