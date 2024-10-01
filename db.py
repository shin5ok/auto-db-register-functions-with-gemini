import firebase_admin
from firebase_admin import credentials, firestore
import uuid

from sampledata import data

firebase_admin.initialize_app()

db = firestore.client()

def add(data=data):

    id = str(uuid.uuid4())

    doc_ref = db.collection("house_specifications").document(id)
    doc_ref.set(data)
    
    print(f"Data written to Firestore with document ID: {id}")

if __name__ == "__main__":
    add()
    