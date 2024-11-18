from tkinter import *

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        history.append(f"{equation_text} = {total}")  # Add the calculation to history
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

def clear_button():
    global equation_text
    equation_label.set("")
    equation_text = ""

def view_history():
    # Create a new window for history
    history_window = Toplevel(window)
    history_window.title("Calculation History")
    history_window.geometry("400x400")

    history_label = Label(history_window, text="History", font=("consolas", 18))
    history_label.pack()

    # Add each history item as a label in the window
    for item in history:
        item_label = Label(history_window, text=item, font=("consolas", 14))
        item_label.pack()

window = Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()
history = []  # List to store calculation history

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="black", fg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear_equation = Button(window, text='Clear', height=4, width=15, font=35, fg= "orange", command=clear_button)
clear_equation.pack()

history_button = Button(window, text='History', height=4, width=15, font=35, fg= "orange", command=view_history)
history_button.pack()

window.mainloop()
