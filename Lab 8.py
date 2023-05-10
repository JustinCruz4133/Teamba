from tkinter import *


class ListBoxTest:
    def __init__(self):
        self.root = Tk()
        self.list_box_1 = Listbox(self.root, selectmode=EXTENDED)
        self.list_box_1.pack()

        self.insert_entry = Entry(self.root)
        self.insert_entry.pack()

        self.insert_button = Button(self.root, text="Insert", command=self.InsertWord)
        self.insert_button.pack()

        self.delete_button = Button(self.root, text="Delete", command=self.DeleteSelection)
        self.delete_button.pack()

        self.list_box_1.insert(1, "C++")
        self.list_box_1.insert(2, "Python")
        self.list_box_1.insert(3, "HTML")
        self.list_box_1.insert(4, "Java")

        self.root.mainloop()

    def InsertWord(self):
        word = self.insert_entry.get()
        self.list_box_1.insert(END, word)
        self.insert_entry.delete(0, END)

    def DeleteSelection(self):
        items = self.list_box_1.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.list_box_1.delete(idx, idx)
            pos += 1


lbt = ListBoxTest()
