import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("sunck")
win.geometry("600x400+700+200")

#表格
tree = ttk.Treeview(win)
tree.pack()

#定义列
tree["columns"] = ("姓名","年龄","身高","体重")
#设置列
tree.column("姓名",width = 100)
tree.column("年龄",width = 100)
tree.column("身高",width = 100)
tree.column("体重",width = 100)
#设置表头
tree.heading("姓名",text = "姓名-name")
tree.heading("年龄",text = "年龄-age")
tree.heading("身高",text = "身高-height")
tree.heading("体重",text = "体重-weight")

#添加数据
tree.insert("",0,text = "line1",values = ("卢彦旭","28","165","80"))
tree.insert("",1,text = "line2",values = ("范玉斌","29","167","70"))



win.mainloop()