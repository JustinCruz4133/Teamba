from tkinter import *

def sim_back():
    screen1.destroy()
    screen.deiconify()

def com_back():
    screen2.destroy()
    screen.deiconify()

def sim_clear():
    principal.set("")
    interest_rate.set("")
    time.set("")
    total_sim_i.set("")
    future_sim.set("")

def com_clear():
    principal.set("")
    interest_rate.set("")
    time.set("")
    num_time_com.set("")
    total_com_i.set("")
    future_com.set("")

def cal_sim():
    global sim_i_amount
    global future_sim_a
    principal_value = float(principal.get())
    interest_rate_value = float(interest_rate.get()) / 100  # convert percentage to decimal
    time_value = float(time.get())

    sim_i_amount = str(round(principal_value * interest_rate_value * time_value, 2))
    total_sim_i.set(sim_i_amount)

    future_sim_a = str(round(principal_value + (principal_value * interest_rate_value * time_value), 2))
    future_sim.set(future_sim_a)

def cal_com():
    global com_i_amount
    global future_com_a
    principal_value = float(principal.get())
    interest_rate_value = float(interest_rate.get()) / 100  # convert percentage to decimal
    time_value = float(time.get())
    num_time_com_value = float(num_time_com.get())

    com_i_amount = str(round((principal_value * (1 + (interest_rate_value/num_time_com_value))**(num_time_com_value * time_value)) - principal_value, 2))
    total_com_i.set(com_i_amount)

    future_com_a = str(round(principal_value * (1 + (interest_rate_value/num_time_com_value))**(num_time_com_value * time_value), 2))
    future_com.set(future_com_a)

def simple_i():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("400x450+750+275")
    screen1.title("SIMPLE INTEREST")
    screen1.configure(bg="#1B262C")
    screen1.resizable(False, False)
    screen.withdraw()

    global principal
    global interest_rate
    global time

    principal = StringVar()
    interest_rate = StringVar()
    time = StringVar()

    Label(screen1, text = "SIMPLE INTEREST", fg="#3282B8", bg="#1B262C", height=3, width=50, font=("Helvetica", 20, "bold")).pack()
    Label(screen1, text="Enter the details below:", fg="white", bg="#1B262C", font=("Helvetica", 13, "bold")).pack()
    Label(screen1, text = "", bg="#1B262C").pack()

    Label(screen1, text="Principal Amount:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    principal_entry = Entry(screen1, textvariable=principal).pack()
    Label(screen1, text="Interest Rate (in % - Percent):", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    interest_rate_entry = Entry(screen1, textvariable=interest_rate).pack()
    Label(screen1, text = "Time (in years):", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    time_entry = Entry(screen1, textvariable=time).pack()

    Label(screen1, text="", bg="#1B262C").pack()

    global total_sim_i
    total_sim_i = StringVar()

    global future_sim
    future_sim = StringVar()

    Button(screen1, text="Calculate", fg="white", bg="#0F4C75", height=1, width=20, bd=5, font=("Helvetica", 12, "bold"), command= cal_sim).pack()
    Label(screen1, text = "Total Interest:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    Entry(screen1, textvariable=total_sim_i).pack()
    Label(screen1, text = "Future Amount:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    Entry(screen1, textvariable=future_sim).pack()

    Button(screen1, text="CLEAR", fg="white", bg="#0F4C75", font=("Helvetica", 10, "bold"), command=sim_clear).place(x=315, y=350)
    Button(screen1, text="BACK", fg="white", bg="#0F4C75", font=("Helvetica", 10, "bold"), command=sim_back).place(x=45, y=350)

def compound_i():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("400x500+750+250")
    screen2.title("COMPOUND INTEREST")
    screen2.configure(bg="#1B262C")
    screen2.resizable(False, False)
    screen.withdraw()

    global principal
    global interest_rate
    global time
    global num_time_com

    principal = StringVar()
    interest_rate = StringVar()
    time = StringVar()
    num_time_com = StringVar()

    Label(screen2, text="COMPOUND INTEREST", fg="#3282B8", bg="#1B262C", height=3, width=50,font=("Helvetica", 20, "bold")).pack()
    Label(screen2, text="Enter the details below:", fg="white", bg="#1B262C", font=("Helvetica", 13, "bold")).pack()
    Label(screen2, text="", bg="#1B262C").pack()

    Label(screen2, text="Principal Amount:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    principal_entry = Entry(screen2, textvariable=principal).pack()
    Label(screen2, text="Interest Rate (in % - Percent):", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    interest_rate_entry = Entry(screen2, textvariable=interest_rate).pack()
    Label(screen2, text="Frequency:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    Label(screen2, text="1 : Annually     2 : Semi-Annually     4 : Quarterly     12 : Monthly", fg="white", bg="#1B262C", font=("Helvetica", 9, "bold")).pack()
    num_time_com_entry = Entry(screen2, textvariable=num_time_com).pack()
    Label(screen2, text="Time (in years):", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    time_entry = Entry(screen2, textvariable=time).pack()

    Label(screen2, text="", bg="#1B262C").pack()

    global total_com_i
    total_com_i = StringVar()

    global future_com
    future_com = StringVar()

    Button(screen2, text="Calculate", fg="white", bg="#0F4C75", height=1, width=20, bd=5, font=("Helvetica", 12, "bold"), command=cal_com).pack()
    Label(screen2, text="Total Interest:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    Entry(screen2, textvariable=total_com_i).pack()
    Label(screen2, text="Future Amount:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    Entry(screen2, textvariable=future_com).pack()

    Button(screen2, text="CLEAR", fg="white", bg="#0F4C75", font=("Helvetica", 10, "bold"), command=com_clear).place(x=315, y=413)
    Button(screen2, text="BACK", fg="white", bg="#0F4C75", font=("Helvetica", 10, "bold"), command=com_back).place(x=45, y=413)

def main_proj():

    global screen
    screen = Tk()
    screen.geometry("400x400+750+300")
    screen.title("INTEREST CALCULATOR")
    screen.configure(bg = "#1B262C")

    Label(text = "", bg="#1B262C").pack()
    Label(text = "INTEREST CALCULATOR", fg = "#3282B8", bg = "#1B262C", height = 3, width = 50, font = ("Helvetica", 20, "bold")).pack()
    Label(text = "", bg = "#1B262C").pack()
    Button(text = "Simple Interest", fg = "white", bg = "#0F4C75", height = 2, width = 20, bd = 5, font = ("Helvetica", 15, "bold"), command = simple_i).pack()
    Label(text = "", bg = "#1B262C").pack()
    Label(text = "", bg="#1B262C").pack()
    Button(text = "Compound Interest", fg = "white", bg = "#0F4C75", height = 2, width=20, bd=5, font=("Helvetica", 15, "bold"), command=compound_i).pack()

    screen.resizable(False, False)
    screen.mainloop()

main_proj()