import cv2
import os
import pandas as pd
from datetime import datetime

# ---------------- FACE RECOGNIZER ----------------

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

# ---------------- FACE DETECTOR ----------------

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- STUDENT NAMES ----------------

names = sorted(os.listdir("dataset"))

# ---------------- CAMERA ----------------

cap = cv2.VideoCapture(0)

# ---------------- ATTENDANCE LIST ----------------

attendance = []

# Prevent duplicate entries
marked_names = []

# ---------------- MAIN LOOP ----------------

while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Better confidence = lower number
        if confidence < 70:

            name = names[id]

            date = datetime.now().strftime("%Y-%m-%d")
            time = datetime.now().strftime("%H:%M:%S")

            # Prevent duplicate attendance
            if name not in marked_names:

                attendance.append([name, date, time])

                marked_names.append(name)

                print(f"{name} attendance marked")

            # Display name on webcam
            cv2.putText(
                frame,
                name,
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        # Face rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            2
        )

    # Webcam window
    cv2.imshow("Attendance System", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ---------------- CLOSE CAMERA ----------------

cap.release()
cv2.destroyAllWindows()

# ---------------- SAVE ATTENDANCE ----------------

os.makedirs("attendance", exist_ok=True)

df = pd.DataFrame(
    attendance,
    columns=["Name", "Date", "Time"]
)

file_path = "attendance/Attendance.xlsx"

df.to_excel(file_path, index=False)

print("Attendance Saved Successfully")
print("File Location:", file_path)