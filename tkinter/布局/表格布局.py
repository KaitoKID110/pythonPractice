import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

l1 = tkinter.Label(win,text = "good",bg = "skyblue")
l2 = tkinter.Label(win,text = "nice",bg = "red")
l3 = tkinter.Label(win,text = "cool",bg = "pink")
l4 = tkinter.Label(win,text = "handsome",bg = "yellow")

l1.grid(row = 0,column = 0)
l2.grid(row = 0,column = 1)
l3.grid(row = 1,column = 0)
l4.grid(row = 1,column = 1)


win.mainloop()
