import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

def updata():
    print(r.get())

r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win,text = "one",value = 44,variable = r,command = updata)
radio1.pack()
radio2 = tkinter.Radiobutton(win,text = "two",value = 55,variable = r,command = updata)
radio2.pack()
radio2 = tkinter.Radiobutton(win,text = "thr",value = 66,variable = r,command = updata)
radio2.pack()

win.mainloop()
