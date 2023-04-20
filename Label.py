from tkinter import *
Lab = Tk()
Lab.geometry("300x100+10+10")
Lab.title("Label")

lbl1 = Label(Lab, text = "Laboratory Activity 5")
lbl1.place(x=90, y=40)
lbl2 = Label(Lab, text = "Submitted to: Mam Sayo")
lbl2.place(x=80, y=60)

Lab.mainloop()