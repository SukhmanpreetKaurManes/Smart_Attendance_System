# Smart Attendance Management System

An AI-based attendance management system that automatically marks attendance using face recognition and stores records using Google Firebase Firestore.

## Features
- Automatic attendance using face recognition
- Handles unknown faces safely
- Cloud storage using Google Firebase
- Attendance percentage calculation (75% rule)
- Modular and scalable architecture

## Tech Stack
- Python
- OpenCV
- LBPH Face Recognition
- Google Firebase Firestore

## How to Run
pip install -r requirements.txt
python recognize_attendance.py
python upload_attendance.py
python attendance_percentage.py
