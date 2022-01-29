import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")
#                         模式
lb = tkinter.Listbox(win,selectmode = tkinter.BROWSE)
lb.pack()
for item in ["good","nice","handsome","very good","very nice"]:
    lb.insert(tkinter.END,"sunck is a %s man!"% item)
#在开始添加
lb.insert(tkinter.ACTIVE,"sunck is a cool man!")

#把一个列表当成一个元素添加
#lb.insert(tkinter.END,['1','2'])

#删除 参数1为开始的索引，参数2为结束的索引
#lb.delete(1,3)
#lb.delete(1)

#选中 参数1为开始的索引，参数2为结束的索引
#lb.select_set(2,4)
#lb.select_set(2)


#取消选中 参数1为开始的索引，参数2为结束的索引
#lb.select_clear(2,4)
#lb.select_clear(3)

#获取列表中的元素个数
#print(lb.size())

#获取值 参数1为开始的索引，参数2为结束的索引
#print(lb.get(2,4))
#print(lb.get(2))

#返回选中项的索引
#print(lb.curselection())

#判断 一个选项是否被选中
#print(lb.select_includes(1))

win.mainloop()
