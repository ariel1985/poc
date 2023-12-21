# usage: uvicorn main:app --reload
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase_admin import credentials, firestore, initialize_app

# Use a service account
cred = credentials.Certificate('.secret/serviceAccountKey.json')
default_app = initialize_app(cred)

db = firestore.client()

app = FastAPI()

collectionName = 'demo-lition'
documentName = 'config'
fieldName = 'f'

@app.get("/") 
def root():
    return {"Hello": "go to /config or /firebase"}

@app.get("/firebase")
def get_config():
    print(cred.project_id)
    return {'Firebase DB': f'SUCESS: Connected to {cred.project_id}'}

@app.get("/firebase/collection")
def get_firebase_data():
    docs = db.collection(collectionName).stream()
    result = []
    for doc in docs:
        result.append(doc.to_dict())
    print(result)
    return result

@app.get("/firebase/collection/document")
def get_firebase_data():
    doc = db.collection(collectionName).document(documentName).get()
    result = []
    result.append(doc.to_dict())
    print(result)
    return result

# basic crud methods for collection

# create example for  http://localhost:8000/firebase/collection?data={"f":"g"} using curl
# curl -X POST "http://localhost:8000/firebase/collection" -d '{"f":"g"}' -H  "accept: application/json" -H  "Content-Type: application/json"
@app.post("/firebase/collection")
def create_firebase_data(data: dict):
    db.collection(collectionName).document(documentName).set(data)
    return {"message": "Data created successfully"}

# update example for  http://localhost:8000/firebase/collection?data={"f":"g"} using curl
# curl -X PUT "http://localhost:8000/firebase/collection" -d '{"f":"789"}' -H  "accept: application/json" -H  "Content-Type: application/json"
@app.put("/firebase/collection")
def update_firebase_data(data: dict):
    db.collection(collectionName).document(documentName).update(data)
    return {"message": "Data updated successfully"}

# delete example for  http://localhost:8000/firebase/collection using curl
# curl -X DELETE "http://localhost:8000/firebase/collection" -H  "accept: application/json" -H  "Content-Type: application/json"
@app.delete("/firebase/collection")
def delete_firebase_data():
    db.collection(collectionName).document(documentName).delete()
    return {"message": "Data deleted successfully"}
