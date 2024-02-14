from tkinter import*
def draw_shape(event):
    x1, y1 = event.x, event.y
    canvas.create_oval(x1-25, y1, x1+25, y1+50, fill = "yellow")
    
win = Tk()
canvas = Canvas(win, width = 300, height = 300, bg = "white")
canvas.pack()
canvas.bind("<Double-Button-1>", draw_shape)

win.mainloop()
                
