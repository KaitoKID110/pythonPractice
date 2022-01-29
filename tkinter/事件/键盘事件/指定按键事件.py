import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

def func(event):
    print("event.char = ",event.char)
    print("event.keycode = ", event.keycode)
win.bind("a",func)

win.mainloop()