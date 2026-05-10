import cv2
import os
import numpy as np
from tkinter import messagebox
import tkinter as tk

# Hide root window
root = tk.Tk()
root.withdraw()

recognizer = cv2.face.LBPHFaceRecognizer_create()

dataset_path = "dataset"

faces = []
labels = []

id = 0

for person in os.listdir(dataset_path):

    person_path = os.path.join(dataset_path, person)

    for image_name in os.listdir(person_path):

        image_path = os.path.join(person_path, image_name)

        image = cv2.imread(
            image_path,
            cv2.IMREAD_GRAYSCALE
        )

        faces.append(image)
        labels.append(id)

    id += 1

recognizer.train(faces, np.array(labels))

# Create trainer folder
os.makedirs("trainer", exist_ok=True)

recognizer.save("trainer/trainer.yml")

messagebox.showinfo(
    "Success",
    "Training Completed Successfully!"
)