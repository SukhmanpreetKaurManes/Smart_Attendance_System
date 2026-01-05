from firebase_config import db

THRESHOLD = 75  # attendance rule

# Get all attendance records
docs = db.collection("attendance").stream()

total_classes = 0
attendance_count = {}

for doc in docs:
    total_classes += 1
    data = doc.to_dict()

    for student, present in data.items():
        if student not in attendance_count:
            attendance_count[student] = 0
        if present:
            attendance_count[student] += 1

print("\n📊 ATTENDANCE REPORT")
print("Total classes conducted:", total_classes)

print("\nStudent-wise Attendance:")

low_attendance_students = []

for student, present_days in attendance_count.items():
    percentage = (present_days / total_classes) * 100
    status = "SAFE"

    if percentage < THRESHOLD:
        status = "LOW ATTENDANCE"
        low_attendance_students.append(student)

    print(f"{student}: {percentage:.2f}% → {status}")

print("\n🚨 Students below 75% attendance:")
for student in low_attendance_students:
    print("❌", student)
