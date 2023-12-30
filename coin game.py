from tkinter import *
from random import *

win = Tk()
win.title("coin Game")

def change_img():
    List = ["front.png", "back.png"]
    coin = randint(0, 1)
    coin_img = PhotoImage(file = List[coin])

    lbl_coin['image'] = coin_img
    lbl_coin.image = coin_img

    return coin

def game(btn) :
    coin = change_img()

    if btn == coin :
        lbl_res['text'] = "correct"
    else :
        lbl_res['text'] = "incorrect"
        
img = PhotoImage(file = "front.png")
lbl_coin = Label(win, image = img, relief = "solid")

lbl_res = Label(win, text = '', width = 15, font = ("consolas", 20, "bold"), fg = "brown", bg = "lightyellow")

btn_front = Button(win, text = "front", width = 15, font = ("consolas", 15), bg = "skyblue", command = lambda : game(0))
btn_back = Button(win, text = "back", width = 15, font = ("consolas", 15), bg = "pink", command = lambda : game(1))

lbl_coin.grid(row = 0, column = 0, columnspan = 2)
lbl_res.grid(row = 1, column = 0, columnspan = 2)

btn_front.grid(row = 2, column= 0)
btn_back.grid(row = 2, column= 1)

win.mainloop()


                
