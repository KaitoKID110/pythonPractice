import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

#<Enter>光标进入事件
#<Leave>光标离开事件

def func(event):
    print(event.x,event.y)
lable1 = tkinter.Label(win,text = "sunck is a good man",bg = "red")
lable1.pack()
lable1.bind("<Leave>",func)


win.mainloop()