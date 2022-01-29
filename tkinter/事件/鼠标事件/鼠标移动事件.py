import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

#<Bi-Motion> 鼠标按住且移动

def func(event):
    print(event.x,event.y)
lable1 = tkinter.Label(win,text = "sunck is a good man")
lable1.pack()
lable1.bind("<B1-Motion>",func)


win.mainloop()
