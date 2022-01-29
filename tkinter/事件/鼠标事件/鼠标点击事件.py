import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

#鼠标左键<Button-1> 鼠标滚轮<Button-2> 鼠标右键<Button-3>
#鼠标左键双击<Double Button-1>
#鼠标滚轮双击<Double Button-2>
#鼠标右键双击<Double Button-3>
#<Triple Button-i> 三击
def func(event):
    print(event.x,event.y)
button1 = tkinter.Button(win,text = "leftmouse button")
button1.pack()
button1.bind("<Triple Button-1>",func)


win.mainloop()