# usage: uvicorn main:app --reload
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase_admin import credentials, firestore, initialize_app

# Use a service account
cred = credentials.Certificate('.secret/serviceAccountKey.json')
default_app = initialize_app(cred)

db = firestore.client()

app = FastAPI()

@app.get("/") 
def root():
    return {"Hello": "go to /config or /firebase"}

@app.get("/firebase")
def get_config():
    print(cred.project_id)
    return {'Firebase DB': f'SUCESS: Connected to {cred.project_id}'}

@app.get("/firebase/collection")
def get_firebase_data():
    docs = db.collection('demo').stream()
    result = []
    for doc in docs:
        result.append(doc.to_dict())
    print(result)
    return result

@app.get("/firebase/collection/document")
def get_firebase_data():
    doc = db.collection('demo').document('config').get()
    result = []
    result.append(doc.to_dict())
    print(result)
    return result