from tkinter import *

win = Tk()
img = PhotoImage(file = 'light.png')
lbl = Label(win, image = img)
lbl.pack()
win.mainloop()
