import tkinter as tk
from tkinter import messagebox
import os

# ADMIN CREDENTIALS (change if you want)
ADMIN_USER = "admin"
ADMIN_PASS = "1234"

def open_main():
    os.system("python main.py")

def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username == ADMIN_USER and password == ADMIN_PASS:
        messagebox.showinfo("Success", "Login Successful")
        root.destroy()
        open_main()
    else:
        messagebox.showerror("Error", "Invalid Credentials")

# GUI
root = tk.Tk()
root.title("Admin Login")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()