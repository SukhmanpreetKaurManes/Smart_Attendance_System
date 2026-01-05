import os
import cv2
import pickle
import numpy as np
import json

# ---------------- LOAD TRAINED FACE DATA ----------------
with open("faces_data.pkl", "rb") as f:
    faces, labels, label_map = pickle.load(f)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))

print("✅ Face recognizer trained")

# ---------------- LOAD CLASSROOM IMAGE ----------------
classroom_image_path = os.path.abspath(
    os.path.join("data", "students", "dweep", "class.jpeg")
)

print("Using classroom image path:", classroom_image_path)

img = cv2.imread(classroom_image_path)

if img is None:
    print("❌ Classroom image not found or unreadable by OpenCV")
    exit()

print("✅ Classroom image loaded successfully")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ---------------- FACE DETECTION ----------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces_detected = face_cascade.detectMultiScale(gray, 1.3, 5)
print("👤 Faces detected:", len(faces_detected))

# ---------------- FACE RECOGNITION ----------------
attendance = set()

for (x, y, w, h) in faces_detected:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = recognizer.predict(face_roi)

    if confidence < 80:
        student_name = label_map[label]
        attendance.add(student_name)

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            img,
            student_name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )
    else:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(
            img,
            "Unknown",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 0, 255),
            2
        )

# ---------------- DISPLAY RESULT ----------------
cv2.namedWindow("Attendance Result", cv2.WINDOW_NORMAL)
cv2.imshow("Attendance Result", img)

print("🟢 Image window opened. Press ANY key to close.")
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save attendance to file
with open("attendance_output.json", "w") as f:
    json.dump(list(attendance), f)

print("💾 Attendance saved to attendance_output.json")