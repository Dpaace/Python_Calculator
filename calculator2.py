# importing lambda function
from _ast import Lambda
from tkinter import *


# creating application window
root = Tk()
root.geometry("466x644")
root.resizable(0, 0)


# defining title of the project
root.title("Simple Calculator")
root.iconbitmap("D:/Python Tkinter/ficon.ico")


# creating display window
e = Entry(root, width=20, borderwidth=10, fg="black", bg="#84BA48", font=("Times New Roman", 20, "bold"), justify=RIGHT)
e.grid(row=0, column=0, columnspan=4, ipadx=82, ipady=20)


# creating button functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


# Defining the buttons

button_1 = Button(root, text="1", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(1))
button_2 = Button(root, text="2", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(2))
button_3 = Button(root, text="3", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(3))

button_4 = Button(root, text="4", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(4))
button_5 = Button(root, text="5", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(5))
button_6 = Button(root, text="6", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(6))

button_7 = Button(root, text="7", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(7))
button_8 = Button(root, text="8", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(8))
button_9 = Button(root, text="9", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(9))

button_0 = Button(root, text="0", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(0))

button_add = Button(root, text="+", borderwidth=8, padx=24, pady=10, fg="light blue", bg="grey",
                    font=("Bariol", 30, "bold"), cursor="hand2", command=button_add)
button_sub = Button(root, text="-", borderwidth=8, padx=29, pady=10, fg="light blue", bg="grey",
                    font=("Bariol", 30, "bold"), cursor="hand2", command=button_sub)
button_mul = Button(root, text="*", borderwidth=8, padx=28, pady=10, fg="light blue", bg="grey",
                    font=("Bariol", 30, "bold"), cursor="hand2", command=button_mul)
button_div = Button(root, text="/", borderwidth=8, padx=30, pady=10, fg="light blue", bg="grey",
                    font=("Bariol", 30, "bold"), cursor="hand2", command=button_div)
button_clear = Button(root, text="Clear", borderwidth=8, padx=46, pady=10, fg="light blue", bg="grey",
                      font=("Bariol", 28, "bold"), cursor="hand2", command=button_clear)

button_point = Button(root, text=".", borderwidth=8, padx=88, pady=10, fg="light blue", bg="grey",
                      font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click("."))
button_equal = Button(root, text="=", borderwidth=8, padx=84, pady=10, fg="light blue", bg="grey",
                      font=("Bariol", 28, "bold"), cursor="hand2", command=button_equal)

# Putting buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_equal.grid(row=5, column=2, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=2)
button_point.grid(row=4, column=1, columnspan=2)

root.mainloop()
