from datetime import date
import json
from firebase_config import db

# Load attendance from recognition output
with open("attendance_output.json", "r") as f:
    present_students = set(json.load(f))

all_students = ["dweep", "jashan", "karan", "raman"]

today = str(date.today())

attendance_data = {}

for student in all_students:
    attendance_data[student] = student in present_students

db.collection("attendance").document(today).set(attendance_data)

print("✅ Attendance uploaded to Firebase (AI-based)")
print(attendance_data)
