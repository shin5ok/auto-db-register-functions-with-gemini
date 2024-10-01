import firebase_admin
from firebase_admin import credentials, firestore
import ulid

from sampledata import data

import config as c

firebase_admin.initialize_app()

db = firestore.client()
collection_name = c.COLLECTION_NAME

def add(data=data):

    id = str(ulid.ULID())

    doc_ref = db.collection(collection_name).document(id)
    doc_ref.set(data)
    
    print(f"Data written to Firestore with document ID: {id}")

def get_all():

    doc_ref = db.collection(collection_name).stream()
    results = []
    for doc in doc_ref:
        results.append(doc.to_dict())
    return results
    
if __name__ == "__main__":
    add()
    