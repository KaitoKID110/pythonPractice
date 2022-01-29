import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

#<Key>相应所有按键

def func(event):
    print("event.char = ",event.char)
    print("event.keycode = ", event.keycode)
lable1 = tkinter.Label(win,text = "sunck is a good man",bg = "red")
#设置焦点
lable1.focus_set()
lable1.pack()

lable1.bind("<Key>",func)

win.mainloop()