import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

l1 = tkinter.Label(win,text = "good",bg = "skyblue")
l2 = tkinter.Label(win,text = "nice",bg = "red")
l3 = tkinter.Label(win,text = "cool",bg = "pink")

#绝对布局,窗口的变化对位置没有影响。
l1.place(x = 10,y = 10)
l2.place(x = 50,y = 50)
l3.place(x = 100,y = 100)



win.mainloop()