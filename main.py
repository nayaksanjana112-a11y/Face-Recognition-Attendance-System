import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess
import sys
import threading
import pandas as pd
import os

# ---------------- FUNCTIONS ----------------

def run_register():
    subprocess.Popen([sys.executable, "register.py"])

def run_train():
    subprocess.Popen([sys.executable, "train.py"])

def run_detect():
    threading.Thread(
        target=lambda: subprocess.Popen([sys.executable, "detect.py"])
    ).start()

# ---------------- LOAD ATTENDANCE ----------------

def load_attendance():

    file_path = os.path.abspath("attendance/Attendance.xlsx")

    print("Looking for file at:", file_path)

    if not os.path.isfile(file_path):
        messagebox.showerror(
            "Error",
            f"Attendance file not found!\n\n{file_path}"
        )
        return

    df = pd.read_excel(file_path)

    # Clear old rows
    for row in table.get_children():
        table.delete(row)

    # Insert rows into table
    for index, row in df.iterrows():
        table.insert(
            "",
            "end",
            values=(row["Name"], row["Date"], row["Time"])
        )

    messagebox.showinfo("Success", "Attendance Loaded Successfully")

# ---------------- EXIT ----------------

def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

# ---------------- GUI WINDOW ----------------

root = tk.Tk()
root.title("Face Recognition Attendance System - Admin Panel")
root.geometry("750x500")
root.config(bg="lightblue")

# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="ADMIN DASHBOARD",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
title.pack(pady=15)

# ---------------- BUTTON FRAME ----------------

frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10)

# ---------------- BUTTONS ----------------

btn_register = tk.Button(
    frame,
    text="Register Student",
    width=18,
    height=2,
    command=run_register
)
btn_register.grid(row=0, column=0, padx=10)

btn_train = tk.Button(
    frame,
    text="Train Model",
    width=18,
    height=2,
    command=run_train
)
btn_train.grid(row=0, column=1, padx=10)

btn_detect = tk.Button(
    frame,
    text="Start Attendance",
    width=18,
    height=2,
    command=run_detect
)
btn_detect.grid(row=0, column=2, padx=10)

btn_load = tk.Button(
    frame,
    text="Load Attendance",
    width=18,
    height=2,
    command=load_attendance
)
btn_load.grid(row=0, column=3, padx=10)

# ---------------- TABLE ----------------

columns = ("Name", "Date", "Time")

table = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=15
)

table.heading("Name", text="Name")
table.heading("Date", text="Date")
table.heading("Time", text="Time")

table.column("Name", width=220)
table.column("Date", width=220)
table.column("Time", width=220)

table.pack(pady=20)

# ---------------- EXIT BUTTON ----------------

btn_exit = tk.Button(
    root,
    text="Exit",
    width=20,
    height=2,
    bg="red",
    fg="white",
    command=exit_app
)

btn_exit.pack(pady=10)

# ---------------- RUN APP ----------------

root.mainloop()