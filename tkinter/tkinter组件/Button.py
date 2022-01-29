import tkinter

def func():
    print("sunck is a good man")

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")


#创建按钮
button1 = tkinter.Button(win,
                        text = "按钮",
                        command = func,
                        width = 10,
                        height = 5)
button1.pack()

button1 = tkinter.Button(win,
                        text = "关闭",
                        command = win.quit)
button1.pack()

win.mainloop()
