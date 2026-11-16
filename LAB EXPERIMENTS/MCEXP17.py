import tkinter as tk
from tkinter import messagebox

def connection():
    messagebox.showerror("Network Error",
                         "Connection Lost!")

root = tk.Tk()
root.title("Network Alert")
root.geometry("300x200")

label = tk.Label(root, text="Mobile Network Status")
label.pack(pady=20)

button = tk.Button(root, text="Check Connection",
                   command=connection)
button.pack()

root.mainloop()
