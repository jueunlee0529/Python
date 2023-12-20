from tkinter import *

win = Tk()

def click() :
    if btn['text'] == "red" :
        btn['text'] = "blue"
        btn['bg'] = "blue"

    else:
        btn['text'] = "red"
        btn['bg'] = "red"

btn = Button(win, text = "red", fg = "white", bg = "red", command = click)
btn.pack()
win.mainloop()
