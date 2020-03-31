import tkinter
from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("ERROR")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("CALCULATOR")
    window.configure(background="black")
    window.geometry("250x250")

    equation = tkinter.StringVar()

    expression_str = Entry(window, textvariable=equation, fg="black")
    expression_str.grid(columnspan=9, ipadx=40)

    equation.set("")


    # Button Initialization

    bt1 = Button(window, text='7', bg='black', fg='green', command=lambda: press(7), height=1, width=7)
    bt1.grid(row=7, column=0)

    bt2 = Button(window, text="8", bg='black', fg='green', command=lambda: press(8), height=1, width=7)
    bt2.grid(column=1, row=7)

    bt3 = Button(window, text="9", bg="black", fg="green", command=lambda: press(9), height=1, width=7)
    bt3.grid(row=7, column=2)

    bt4 = Button(window, text="/", bg="black", fg="green", command=lambda: press("/"), height=1, width=7)
    bt4.grid(row=7, column=3)

    bt5 = Button(window, text="4", bg="black", fg="green", command=lambda: press(4), height=1, width=7)
    bt5.grid(row=8, column=0)

    bt6 = Button(window, text="5", bg="black", fg="green", command=lambda: press(5), height=1, width=7)
    bt6.grid(row=8, column=1)

    bt7 = Button(window, text="6", bg="black", fg="green", command=lambda: press(6), height=1, width=7)
    bt7.grid(row=8, column=2)

    bt8 = Button(window, text="x", bg="black", fg="green", command=lambda: press("*"), height=1, width=7)
    bt8.grid(row=8, column=3)

    bt9 = Button(window, text="1", bg="black", fg="green", command=lambda: press(1), height=1, width=7)
    bt9.grid(row=9, column=0)

    bt10 = Button(window, text="2", bg="black", fg="green", command=lambda: press(2), height=1, width=7)
    bt10.grid(row=9, column=1)

    bt11 = Button(window, text="3", bg="black", fg="green", command=lambda: press(3), height=1, width=7)
    bt11.grid(row=9, column=2)

    bt12 = Button(window, text="-", bg="black", fg="green", command=lambda: press("-"), height=1, width=7)
    bt12.grid(row=9, column=3)

    bt13 = Button(window, text="0", bg="black", fg="green", command=lambda: press(0), height=1, width=7)
    bt13.grid(row=10, column=0)

    bt14 = Button(window, text="C", bg="black", fg="green", command=clear, height=1, width=7)
    bt14.grid(row=10, column=1)

    bt15 = Button(window, text="=", bg="black", fg="green", command=equal_press, height=1, width=7)
    bt15.grid(row=10, column=2)

    bt16 = Button(window, text="+", bg="black", fg="green", command=lambda: press("+"), height=1, width=7)
    bt16.grid(row=10, column=3)

    window.mainloop()
