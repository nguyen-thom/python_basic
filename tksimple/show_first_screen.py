import tkinter as tk


def add_numbers():
    num1 = int(input1.get())
    num2 = int(input2.get())
    result = num1 + num2
    label3.config(text=result)

root = tk.Tk()
root.geometry("400x600")

input1 = tk.Entry(root)
input1.grid(row=0, column=0)

input2 = tk.Entry(root)
input2.grid(row=0, column=1)

button = tk.Button(root, text="Add", command=add_numbers)
button.grid(row=1, column=0)

label3 = tk.Label(root, text="")
label3.grid(row=2, column=0)

root.mainloop()
