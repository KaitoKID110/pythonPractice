import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+700+200")

frm = tkinter.Frame(win)
frm.pack()

#left
frm_l = tkinter.Frame(frm)
tkinter.Label(frm_l,text = "左上",bg = "pink").pack(side = tkinter.TOP)
tkinter.Label(frm_l,text = "左下",bg = "blue").pack(side = tkinter.TOP)
frm_l.pack(side = tkinter.LEFT)

#right
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r,text = "右上",bg = "red").pack(side = tkinter.TOP)
tkinter.Label(frm_r,text = "右下",bg = "yellow").pack(side = tkinter.TOP)
frm_r.pack(side = tkinter.RIGHT)

win.mainloop()