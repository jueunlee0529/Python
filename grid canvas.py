from tkinter import *

win = Tk()
canvas = Canvas(bg = "white", width = 100, height = 100)
canvas.pack()
x1,y1 = 0,0
x2,y2 = 100,0
for i in range(10):
    canvas.create_line(x1, y1, x2, y2)
    y1 += 10
    y2 = y1
x1,y1 = 0,0
x2,y2 = 0,100
for i in range(11):
    canvas.create_line(x1, y1, x2, y2)
    x1 += 10
    x2 = x1

#canvas.create_oval(30,30, 70, 50, fill = "blue")

#canvas.create_rectangle(30,10, 60, 90, fill = "yellow")

canvas.create_polygon(20, 10, 20, 90, 80, 90, fill = "red")
win.mainloop()
