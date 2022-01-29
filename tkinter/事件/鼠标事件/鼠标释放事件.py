import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

#<ButtonRelease-i> 鼠标释放事件

def func(event):
    print(event.x,event.y)
lable1 = tkinter.Label(win,text = "sunck is a good man",bg = "red")
lable1.pack()
lable1.bind("<ButtonRelease-1>",func)

win.mainloop()
