import tkinter

win = tkinter.Tk()
win.title("sunck")
#win.geometry("400x400+700+200")

#EXTENDED 可以使Listbox支持shift和ctrl
lb = tkinter.Listbox(win,selectmode = tkinter.EXTENDED)
for item in ["good","nice","handsome","very good","very nice","good1","nice1","handsome1","very good1","very nice1","good2","nice2","handsome2","very good2","very nice2"]:
    lb.insert(tkinter.END,item)

#按住shift，可以实现连续按
#按住ctrl，可以实现多选
#滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side = tkinter.RIGHT,fill = tkinter.Y)
lb.configure(yscrollcommand = sc.set)
lb.pack(side = tkinter.LEFT,fill = tkinter.BOTH)
#额外给属性赋值
sc["command"] = lb.yview


win.mainloop()