import cv2

# Absolute path (since Option 2 worked)
image_path = r"C:\Users\HP\OneDrive\Desktop\d1.jpeg"

# Load image
img = cv2.imread(image_path)

if img is None:
    print("❌ Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5
)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(f"✅ Faces detected: {len(faces)}")

# Show result
cv2.imshow("Face Detection Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
