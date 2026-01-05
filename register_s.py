import cv2
import os
import pickle

DATASET_PATH = "C:\images"   # 👈 IMPORTANT CHANGE
print("Looking for dataset at:", DATASET_PATH)


# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = []
labels = []
label_map = {}
current_label = 0

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png")

for student_name in os.listdir(DATASET_PATH):
    student_path = os.path.join(DATASET_PATH, student_name)

    if not os.path.isdir(student_path):
        continue

    print(f"\n📁 Registering student: {student_name}")
    label_map[current_label] = student_name

    for img_name in os.listdir(student_path):

        # Only image files
        if not img_name.lower().endswith(VALID_EXTENSIONS):
            continue

        img_path = os.path.join(student_path, img_name)
        img = cv2.imread(img_path)

        if img is None:
            print(f"❌ Could not read {img_path}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detected_faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        if len(detected_faces) == 0:
            print(f"⚠️ No face detected in {img_name}")
            continue

        # Take the first detected face
        (x, y, w, h) = detected_faces[0]
        face_roi = gray[y:y+h, x:x+w]

        faces.append(face_roi)
        labels.append(current_label)

        print(f"✅ Face registered from {img_name}")

    current_label += 1

# Save registered face data
with open("faces_data.pkl", "wb") as f:
    pickle.dump((faces, labels, label_map), f)

print("\n🎉 STUDENT REGISTRATION COMPLETED")
print("🧾 Label map:", label_map)
print(f"📊 Total faces registered: {len(faces)}")
