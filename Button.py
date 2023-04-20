from tkinter import *
Btn = Tk()
Btn.geometry("350x150+10+10")
Btn.title("Button")

def ChangeC():
    global ChangeC
    if ChangeC:
        but1.config(bg="Yellow")
        ChangeC = False
    else:
        but1.config(bg="Blue")
        ChangeC = True

but1 = Button(Btn, text = "Color", bg = 'Blue', fg = 'Red', font = ('Calibri', 10), command = ChangeC)
but1.place(x=40, y=100)

but2 = Button(Btn, text = "<---Click to change the color of the button", font = ('Calibri', 10), command = ChangeC)
but2.place(x=90, y=100)

Btn.mainloop()