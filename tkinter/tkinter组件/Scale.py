import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")
#                                                           水平                        宽高
sc = tkinter.Scale(win,from_ = 0,to = 100,orient = tkinter.HORIZONTAL,tickinterval = 100,length = 200)
sc.pack()

#设置值
sc.set(20)

#取值
def showNum():
    print(sc.get())

tkinter.Button(win,text = "按钮",command = showNum).pack()

win.mainloop()
