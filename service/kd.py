import pickle
import firebase_admin
import datetime
from firebase_admin import credentials, auth, db,firestore

cred = credentials.Certificate('../chirpchat-23dba-firebase-adminsdk-kh0p1-529b03f269.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chirpchat-23dba-default-rtdb.firebaseio.com/'
})

from firebase_admin import db

# Initialize the app
# firebase_admin.initialize_app(options)

# Get a reference to the database
ref = db.reference("/messages")

# Retrieve messages in real-time
message = {
   "sender_id": "user_id",
   "receiver_id": "receiver_id",
   "text": "Testing!"
}

messages = ref.get()
ref.push(message)


# Listen for new messages
# def on_new_message(event):
#     new_message = event.data
#     print("New message: ", new_message)

# # Add a listener to the reference
# ref.listen(on_new_message)
