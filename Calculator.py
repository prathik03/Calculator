import tkinter
import math
from math import *
from tkinter import *
import time

expression = ""
divisor = ""
dividend = ""



def close():
    main_wind.destroy()

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


def close1():
    main_wind.destroy()

    def press1(num):
        global expression
        global divisor
        divisor = divisor + str(num)
        expression = expression + str(num)
        equation1.set(expression)

    def logarithm1(num):
        try:
            global expression
            expression = str(math.log(num, 10))
            equation1.set(expression)
            expression = ""
        except:
            equation1.set("log of this value not possible")
            expression = ""

    def logarithm2(num):
        try:
            global expression
            expression = str(math.log(num))
            equation1.set(expression)
            expression = ""
        except:
            equation1.set("ln of the value not possible")
            expression = ""

    def exponent(num):
        global expression
        expression = str(math.exp(num))
        equation1.set(expression)
        expression = ""

    def cube(num):
        global expression
        expression = str(math.pow(num, 3))
        equation1.set(expression)
        expression = ""

    def square(num):
        global expression
        expression = str(math.pow(num, 2))
        equation1.set(expression)
        expression = ""



    def modulus_press(num1):
        global expression
        global divisor
        expression = expression + str(num1)
        equation1.set(expression)

        def press2(divid):
            global expression
            global dividend

            dividend = dividend + str(divid)
            equation1.set(dividend)

        def equal_press2():
            global dividend
            global expression
            global divisor


            expression = int(divisor) % int(dividend)
            equation1.set(str(expression))
            expression =""
            divisor = ""
            dividend =""
            
        def clear2():
            global expression
            global dividend
            global divisor
            equation1.set("")
            divisor = ""
            dividend=""
            expression=""

        '''
        global expression
        expression = expression + str(num1)
        equation1.set(expression)
        
        '''

        bta1 = Button(window1, text='7', bg='black', fg='green', command=lambda: press2(7), height=1,
                      width=7)
        bta1.grid(column=1, row=7)
        bta2 = Button(window1, text="8", bg='black', fg='green', command=lambda: press2(8), height=1,
                      width=7)
        bta2.grid(column=2, row=7)
        bta3 = Button(window1, text="9", bg="black", fg="green", command=lambda: press2(9), height=1,
                      width=7)
        bta3.grid(column=3, row=7)
        bta5 = Button(window1, text="4", bg="black", fg="green", command=lambda: press2(4), height=1,
                      width=7)
        bta5.grid(column=1, row=8)
        bta6 = Button(window1, text="5", bg="black", fg="green", command=lambda: press2(5), height=1,
                      width=7)
        bta6.grid(column=2, row=8)
        bta7 = Button(window1, text="6", bg="black", fg="green", command=lambda: press2(6), height=1,
                      width=7)
        bta7.grid(column=3, row=8)
        bta9 = Button(window1, text="1", bg="black", fg="green", command=lambda: press2(1), height=1,
                      width=7)
        bta9.grid(column=1, row=9)
        bta10 = Button(window1, text="2", bg="black", fg="green", command=lambda: press2(2), height=1,
                       width=7)
        bta10.grid(column=2, row=9)
        bta11 = Button(window1, text="3", bg="black", fg="green", command=lambda: press2(3), height=1,
                       width=7)
        bta11.grid(column=3, row=9)
        bta13 = Button(window1, text="0", bg="black", fg="green", command=lambda: press2(0), height=1,
                       width=7)
        bta13.grid(column=1, row=10)

        bta15 = Button(window1, text="=", bg="black", fg="green", command=equal_press2, height=1, width=7)
        bta15.grid(row=10, column=3)

        bta14 = Button(window1, text="C", bg="black", fg="green", command=clear2, height=1, width=7)
        bta14.grid(row=10, column=2)

        expression = ""
        equation1.set("")



    def absolute(num):
        global expression
        expression = str(abs(num))
        equation1.set(expression)

    def inverse(num):
        global expression
        expression = str(math.pow(num, -1))
        equation1.set(expression)

    def equal_press1():
        try:
            global expression
            total = str(eval(expression))
            equation1.set(total)
            expression = ""
        except:
            equation1.set("ERROR")
            expression = ""

    def clear1():
        global expression
        expression = ""
        equation1.set("")

    window1 = tkinter.Tk()
    window1.configure(background="black")
    window1.geometry("300x155")

    equation1 = tkinter.StringVar()

    expression_str1 = Entry(window1, textvariable=equation1, fg="black")
    expression_str1.grid(columnspan=9, ipadx=40)

    equation1.set("")

    # Button Initialization

    

    """                     ROW 1                           """

    bt_2 = Button(window1, text='x^2', bg='black', fg='green', command=lambda: square(int(expression)), height=1,
                  width=7)
    bt_2.grid(column=0, row=6)

    bt_3 = Button(window1, text='mod', bg='black', fg='green', command=lambda: modulus_press("mod"), height=1, width=7)
    bt_3.grid(column=1, row=6)

    bt_4 = Button(window1, text='pi', bg='black', fg='green', command=lambda: press1("pi"), height=1, width=7)
    bt_4.grid(column=2, row=6)

    bt_5 = Button(window1, text='|x|', bg='black', fg='green', command=lambda: absolute(int(expression)), height=1,
                  width=7)
    bt_5.grid(column=3, row=6)

    bt_6 = Button(window1, text='1/x', bg='black', fg='green', command=lambda: inverse(int(expression)), height=1,
                  width=7)
    bt_6.grid(column=4, row=6)

    """                 ROW 2               """

    bt_1 = Button(window1, text='x^3', bg='black', fg='green', command=lambda: cube(int(expression)), height=1,
                  width=7)
    bt_1.grid(column=0, row=7)

    bt1 = Button(window1, text='7', bg='black', fg='green', command=lambda: press1(7), height=1, width=7)
    bt1.grid(column=1, row=7)

    bt2 = Button(window1, text="8", bg='black', fg='green', command=lambda: press1(8), height=1, width=7)
    bt2.grid(column=2, row=7)

    bt3 = Button(window1, text="9", bg="black", fg="green", command=lambda: press1(9), height=1, width=7)
    bt3.grid(row=7, column=3)

    bt4 = Button(window1, text="/", bg="black", fg="green", command=lambda: press1("/"), height=1, width=7)
    bt4.grid(row=7, column=4)

    """                 ROW 3               """

    bt_7 = Button(window1, text='exp', bg='black', fg='green', command=lambda: exponent(int(expression)), height=1,
                  width=7)
    bt_7.grid(column=0, row=8)

    bt5 = Button(window1, text="4", bg="black", fg="green", command=lambda: press1(4), height=1, width=7)
    bt5.grid(row=8, column=1)

    bt6 = Button(window1, text="5", bg="black", fg="green", command=lambda: press1(5), height=1, width=7)
    bt6.grid(row=8, column=2)

    bt7 = Button(window1, text="6", bg="black", fg="green", command=lambda: press1(6), height=1, width=7)
    bt7.grid(row=8, column=3)

    bt8 = Button(window1, text="x", bg="black", fg="green", command=lambda: press1("*"), height=1, width=7)
    bt8.grid(row=8, column=4)

    """                 ROW 4                   """

    bt_8 = Button(window1, text='log', bg='black', fg='green', command=lambda: logarithm1(int(expression)), height=1,
                  width=7)
    bt_8.grid(column=0, row=9)

    bt9 = Button(window1, text="1", bg="black", fg="green", command=lambda: press1(1), height=1, width=7)
    bt9.grid(row=9, column=1)

    bt10 = Button(window1, text="2", bg="black", fg="green", command=lambda: press1(2), height=1, width=7)
    bt10.grid(row=9, column=2)

    bt11 = Button(window1, text="3", bg="black", fg="green", command=lambda: press1(3), height=1, width=7)
    bt11.grid(row=9, column=3)

    bt12 = Button(window1, text="-", bg="black", fg="green", command=lambda: press1("-"), height=1, width=7)
    bt12.grid(row=9, column=4)

    """                 ROW 5                   """

    bt_9 = Button(window1, text='ln', bg='black', fg='green', command=lambda: logarithm2(int(expression)), height=1,
                  width=7)
    bt_9.grid(column=0, row=10)

    bt13 = Button(window1, text="0", bg="black", fg="green", command=lambda: press1(0), height=1, width=7)
    bt13.grid(row=10, column=1)

    bt14 = Button(window1, text="C", bg="black", fg="green", command=clear1, height=1, width=7)
    bt14.grid(row=10, column=2)

    bt15 = Button(window1, text="=", bg="black", fg="green", command=equal_press1, height=1, width=7)
    bt15.grid(row=10, column=3)

    bt16 = Button(window1, text="+", bg="black", fg="green", command=lambda: press1("+"), height=1, width=7)
    bt16.grid(row=10, column=4)

    window1.mainloop()


"""
                        WORK FLOW OF THE PROGRAM

                            1) Calculator
                                    -> Standard
                                    -> Scientific
    
"""

if __name__ == '__main__':
    """                 SELECTION MENU WINDOW
    """

    main_wind = tkinter.Tk()
    main_wind.title("SELECTION MENU")
    main_wind.configure(bg="black")
    main_wind.geometry("500x500")

    calc = Button(main_wind, text="STANDARD CALCULATOR", fg="green", height=5, width=20, command=close).place(x=260,
                                                                                                              y=150,
                                                                                                              anchor=CENTER)

    conv = Button(main_wind, text="SCIENTIFIC CALCULATOR", fg="green", height=5, width=20, command=close1).place(x=260,
                                                                                                                 y=350,
                                                                                                                 anchor=CENTER)

    main_wind.mainloop()
