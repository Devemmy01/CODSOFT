import tkinter as tk

# the function to get and calculate user input
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = entry_operation.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = "Invalid operation choice!"

    label_result.config(text="Result: " + str(result))

# the main window
window = tk.Tk()
window.title("Calculator")

# input fields
label_num1 = tk.Label(window, text="Enter the first number:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Enter the second number:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

label_operation = tk.Label(window, text="Enter the operation (+, -, *, /):")
label_operation.pack()
entry_operation = tk.Entry(window)
entry_operation.pack()

# calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()

# result label
label_result = tk.Label(window, text="Result:")
label_result.pack()

# the main loop
window.mainloop()