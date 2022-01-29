import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

cv = tkinter.StringVar()
com = ttk.Combobox(win,textvariable = cv)
com.pack()
com["value"] = ("黑龙江","吉林","辽宁")

com.current(0)

def func(event):
    print(cv.get())
    print(com.get())
    print("sunck is a good man")
com.bind("<<ComboboxSelected>>",func)

win.mainloop()
