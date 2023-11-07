# # import required modules
# import firebase_admin
# from firebase_admin import db, credentials
# from datetime import datetime

# def save():
#     # authenticate to firebase
#     cred = credentials.Certificate("credentials.json")
#     firebase_admin.initialize_app(cred, {"databaseURL": "https://task-bot-7c5ae-default-rtdb.europe-west1.firebasedatabase.app/"})


#     # creating reference to root node
#     ref = db.reference("/")

#     # retrieving and printing data from root node
#     print('Root node data:', ref.get())

#     # set operation
#     db.reference("/updatedat").set(datetime.now().isoformat())

# def get():
#     # fetching and printing the updated data at "/videos"
#     videos_ref = db.reference("/videos")
#     print('Videos data:', videos_ref.get())
    
#     updatedat_ref = db.reference("/updatedat")
#     print('Updated at:', updatedat_ref.get())

# save()


# firebase_handler.py

import firebase_admin
from firebase_admin import credentials, db

class FirebaseHandler:


    def __init__(self, cred_path = "credentials.json", db_url="https://task-bot-7c5ae-default-rtdb.europe-west1.firebasedatabase.app/"):
        
        # Initialize the Firebase app with credentials and database URL
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': db_url
        })

    def get(self, ref_path):
        ref = db.reference(ref_path)
        return ref.get()

    def set(self, ref_path, value):
        ref = db.reference(ref_path)
        ref.set(value)

    def set_list(self, ref_path, value):
        ref = db.reference(ref_path)
        newref = ref.push()
        newref.set(value)

'''
# main example how to use.py

from firebase_handler import FirebaseHandler

# Path to your Firebase credentials and database URL
CREDENTIAL_PATH = "path_to_your_credentials.json"
DATABASE_URL = "https://your-database-name.firebaseio.com/"

# Initialize the Firebase handler
firebase = FirebaseHandler(CREDENTIAL_PATH, DATABASE_URL)

# Set a value in Firebase
firebase.set("/path/in/firebase", {"key": "value"})

# Get a value from Firebase
value = firebase.get("/path/in/firebase")
print(value)

'''