import firebase_admin
from firebase_admin import credentials, firestore

# Load service account key
cred = credentials.Certificate("firebase_key.json")

# Initialize Firebase app (only once)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Create Firestore client
db = firestore.client()
