import tkinter

win = tkinter.Tk()
win.title("sunck")
#win.geometry("400x400+700+200")

#EXTENDED 可以使Listbox支持shift和ctrl
lb = tkinter.Listbox(win,selectmode = tkinter.MULTIPLE)
lb.pack()
for item in ["good","nice","handsome","very good","very nice"]:
    lb.insert(tkinter.END,item)

win.mainloop()