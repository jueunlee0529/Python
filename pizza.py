from tkinter import*

win = Tk()
img = PhotoImage(file = 'pizza.png')
lbl1 = Label(win, image = img)
lbl2 = Label(win,text = "pizza", fg = "red", bg = "yellow")
lbl1.pack()
lbl2.pack()
win.mainloop()
