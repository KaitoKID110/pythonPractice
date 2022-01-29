import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

l1 = tkinter.Label(win,text = "good",bg = "skyblue")
l2 = tkinter.Label(win,text = "nice",bg = "red")
l3 = tkinter.Label(win,text = "cool",bg = "pink")


l1.pack(fill = tkinter.Y,side = tkinter.LEFT)
l2.pack(fill = tkinter.X,side = tkinter.TOP)
l3.pack(fill = tkinter.BOTH)


win.mainloop()