from tkinter import *
TF = Tk()
TF.geometry("300x100+10+10")
TF.title("Text field")

text1 = Text(TF, height = 3, width = 23, font = ('Calibri', 12))
text1.place(x=55, y=20)

TF.mainloop()