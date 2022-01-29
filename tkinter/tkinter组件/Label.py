import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

#text 文本
#bg 背景色
#fg 前景色
#font 字体
#width height 宽高
#wraplength  指定text中多宽进行换行
#justify 换行时的对齐方式
#anchor 位置 n北 e东 s南 w西 center居中 ne se nw sw
label = tkinter.Label(win,
                      text = "sunck",
                      bg = "yellow",
                      fg = "green",
                      font = ("微软雅黑",20),
                      width = 10,
                      height = 4,
                      wraplength = 100,
                      justify = "left",
                      anchor = "center")
#显示出来
label.pack()


win.mainloop()













