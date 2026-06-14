import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Smart Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Entry field
expression = ""

entry = tk.Entry(
    root,
    font=("Arial", 20),
    bd=10,
    relief=tk.RIDGE,
    justify="right"
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Functions
def press(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Expression")
        clear()

# Button Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        action = (
            calculate if btn == "="
            else lambda x=btn: press(x)
        )

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 18),
            command=action,
            width=5,
            height=2
        ).pack(side="left", expand=True, fill="both")

# Clear Button
tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 18),
    command=clear,
    height=2
).pack(fill="both", padx=10, pady=10)

root.mainloop()
5
