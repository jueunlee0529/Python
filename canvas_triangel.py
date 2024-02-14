from tkinter import*

win = Tk()
canvas = Canvas(win, width = 200, height = 100, bg = "white")
canvas.pack()

canvas.create_polygon(100, 10, 30, 90, 160, 90, fill = "red")

win.mainloop()
