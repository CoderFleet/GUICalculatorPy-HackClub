# User Instructions
# pip install tk
import tkinter as tk
import math


root = tk.Tk()
root.title("Simple CalculatorPy")
root.resizable(False, False)


entry = tk.Entry(root, width=35, borderwidth=5, font=("Arial", 12))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_sin():
    number = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.sin(number))

def button_cos():
    number = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.cos(number))

def button_tan():
    number = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.tan(number))

def button_sqrt():
    number = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.sqrt(number))

def button_equal():
    second_number = entry.get()
    global f_num
    global math
    entry.delete(0, tk.END)

    if math == "addition":
        entry.insert(0, f_num + float(second_number))

    if math == "subtraction":
        entry.insert(0, f_num - float(second_number))

    if math == "multiplication":
        entry.insert(0, f_num * float(second_number))

    if math == "division":
        entry.insert(0, f_num / float(second_number))


button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="#f0f0f0", font=("Arial", 14))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="#f0f0f0", font=("Arial", 14))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="#f0f0f0", font=("Arial", 14))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="#f0f0f0", font=("Arial", 14))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="#f0f0f0", font=("Arial", 14))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="#f0f0f0", font=("Arial", 14))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="#f0f0f0", font=("Arial", 14))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="#f0f0f0", font=("Arial", 14))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="#f0f0f0", font=("Arial", 14))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="#f0f0f0", font=("Arial", 14))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add, bg="#ffcccb", font=("Arial", 14))
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract, bg="#ffcccb", font=("Arial", 14))
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply, bg="#ffcccb", font=("Arial", 14))
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide, bg="#ffcccb", font=("Arial", 14))
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal, bg="#90ee90", font=("Arial", 14))

button_sin = tk.Button(root, text="sin", padx=36, pady=20, command=button_sin, bg="#add8e6", font=("Arial", 14))
button_cos = tk.Button(root, text="cos", padx=36, pady=20, command=button_cos, bg="#add8e6", font=("Arial", 14))
button_tan = tk.Button(root, text="tan", padx=36, pady=20, command=button_tan, bg="#add8e6", font=("Arial", 14))
button_sqrt = tk.Button(root, text="√", padx=38, pady=20, command=button_sqrt, bg="#add8e6", font=("Arial", 14))

def button_clear():
    entry.delete(0, tk.END)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear, bg="#f0e68c", font=("Arial", 14))

def button_add_point():
    current = entry.get()
    if "." not in current:
        entry.insert(tk.END, ".")

button_point = tk.Button(root, text=".", padx=42, pady=20, command=button_add_point, bg="#f0f0f0", font=("Arial", 14))

def button_backspace():
    current = entry.get()
    entry.delete(len(current) - 1)
button_backspace = tk.Button(root, text="⌫", padx=37, pady=20, command=button_backspace, bg="#ffcccb", font=("Arial", 14))

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
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_sin.grid(row=1, column=3)
button_cos.grid(row=2, column=3)
button_tan.grid(row=3, column=3)
button_sqrt.grid(row=4, column=3)

button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_point.grid(row=5, column=3)
button_backspace.grid(row=0, column=3)



root.mainloop()