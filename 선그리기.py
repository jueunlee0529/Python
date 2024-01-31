from tkinter import *

win = Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 500)
canvas.create_line(250,50,250,350, fill = "Light blue", width = 5)
canvas.pack()
win.mainloop()
