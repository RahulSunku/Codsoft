from tkinter import *

def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def buttonClear():
    global operator
    operator = ""
    input_value.set("")

def buttonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator = ""

main = Tk()
main.title("Calculator")

operator = ""
input_value = StringVar()

# Flat display with light gray background
display_text = Entry(main, font=("arial", 20, "bold"), textvariable=input_value, bd=30, insertwidth=4,
                     bg="lightgray", justify=RIGHT, relief=FLAT)
display_text.grid(columnspan=4, pady=10)

# Function to configure a rounded button with a light blue background
def configure_button(button):
    button.config(padx=16, bd=8, fg="black", bg="lightblue", font=("arial", 16, "bold"), relief=FLAT,
                  overrelief=RIDGE, borderwidth=2, width=5, height=2)

# Row 1 7 8 9 +
btn_7 = Button(main, text="7", command=lambda: buttonClick(7))
configure_button(btn_7)
btn_7.grid(row=1, column=0)

btn_8 = Button(main, text="8", command=lambda: buttonClick(8))
configure_button(btn_8)
btn_8.grid(row=1, column=1)

btn_9 = Button(main, text="9", command=lambda: buttonClick(9))
configure_button(btn_9)
btn_9.grid(row=1, column=2)

btn_add = Button(main, text="+", command=lambda: buttonClick("+"))
configure_button(btn_add)
btn_add.grid(row=1, column=3)

# Row 2 - 4 5 6 -
btn_4 = Button(main, text="4", command=lambda: buttonClick(4))
configure_button(btn_4)
btn_4.grid(row=2, column=0)

btn_5 = Button(main, text="5", command=lambda: buttonClick(5))
configure_button(btn_5)
btn_5.grid(row=2, column=1)

btn_6 = Button(main, text="6", command=lambda: buttonClick(6))
configure_button(btn_6)
btn_6.grid(row=2, column=2)

btn_sub = Button(main, text="-", command=lambda: buttonClick("-"))
configure_button(btn_sub)
btn_sub.grid(row=2, column=3)

# Row 3 - 1 2 3 *
btn_1 = Button(main, text="1", command=lambda: buttonClick(1))
configure_button(btn_1)
btn_1.grid(row=3, column=0)

btn_2 = Button(main, text="2", command=lambda: buttonClick(2))
configure_button(btn_2)
btn_2.grid(row=3, column=1)

btn_3 = Button(main, text="3", command=lambda: buttonClick(3))
configure_button(btn_3)
btn_3.grid(row=3, column=2)

btn_mul = Button(main, text="*", command=lambda: buttonClick("*"))
configure_button(btn_mul)
btn_mul.grid(row=3, column=3)

# Row 4 - 0 C = /
btn_0 = Button(main, text="0", command=lambda: buttonClick(0))
configure_button(btn_0)
btn_0.grid(row=4, column=0)

btn_clear = Button(main, text="C", command=buttonClear)
configure_button(btn_clear)
btn_clear.grid(row=4, column=1)

btn_equal = Button(main, text="=", command=buttonEqual)
configure_button(btn_equal)
btn_equal.grid(row=4, column=2)

btn_div = Button(main, text="/", command=lambda: buttonClick("/"))
configure_button(btn_div)
btn_div.grid(row=4, column=3)

main.mainloop()
