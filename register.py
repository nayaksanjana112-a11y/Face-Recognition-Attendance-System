import cv2
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

# ---------------- GUI INPUT ----------------

root = tk.Tk()
root.withdraw()

# Ask student name in popup
name = simpledialog.askstring(
    "Student Registration",
    "Enter Student Name:"
)

# If cancel pressed
if not name:
    messagebox.showerror("Error", "Name cannot be empty!")
    exit()

# ---------------- CREATE DATASET FOLDER ----------------

path = f"dataset/{name}"
os.makedirs(path, exist_ok=True)

# ---------------- FACE DETECTOR ----------------

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- CAMERA ----------------

cap = cv2.VideoCapture(0)

count = 0

# ---------------- CAPTURE LOOP ----------------

while True:

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        count += 1

        face = gray[y:y+h, x:x+w]

        cv2.imwrite(
            f"{path}/{count}.jpg",
            face
        )

        cv2.rectangle(
            img,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            img,
            f"Images Captured: {count}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Register Student", img)

    # Press q OR auto stop at 50 images
    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
        break

# ---------------- CLOSE CAMERA ----------------

cap.release()
cv2.destroyAllWindows()

# ---------------- SUCCESS MESSAGE ----------------

messagebox.showinfo(
    "Success",
    f"{name} registered successfully!"
)