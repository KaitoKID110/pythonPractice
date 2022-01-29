import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

#绑定变量
lbv = tkinter.StringVar()
#与BROWSE相似，但它不支持鼠标按下移动选中位置
lb = tkinter.Listbox(win,selectmode = tkinter.SINGLE,listvariable = lbv)
lb.pack()
for item in ["good","nice","handsome","very good","very nice"]:
    lb.insert(tkinter.END,"sunck is a %s man!"% item)

#打印当前列表中的选项
#print(lbv.get())

#设置选项
#lbv.set(("1","2","3"))

def myprint(event):
    print(lb.get(lb.curselection()))

#绑定事件
lb.bind("<Double-Button-1>",myprint)


win.mainloop()
