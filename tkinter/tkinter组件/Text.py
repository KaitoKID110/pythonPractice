import tkinter

win = tkinter.Tk()
win.title("第一个tkinter窗口")
win.geometry("400x400+700+200")
#                             列数          行数
text = tkinter.Text(win,width = 30,height = 4)
text.pack()
str = """If there is anyone out there who still doubts that america is a place where all things are possible; who still wonders if the dream of our founders is alive in our time; who still questions the power of our democracy, tonight is your answer.
"""
text.insert(tkinter.INSERT,str)
win.mainloop()