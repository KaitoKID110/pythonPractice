import tkinter

win = tkinter.Tk()
win.title("第一个tkinter窗口")
win.geometry("400x400+700+200")


entry = tkinter.Entry(win)
entry.pack()
def func():
    print(entry.get())

button1 = tkinter.Button(win,text = "按钮",command = func,)
button1.pack()





win.mainloop()