import pickle
import firebase_admin
import datetime
from firebase_admin import credentials, auth, db as DB,firestore

cred = credentials.Certificate('chirpchat-23dba-firebase-adminsdk-kh0p1-529b03f269.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chirpchat-23dba-default-rtdb.firebaseio.com/'
})

db = firestore.client()
users_ref = db.collection("userdata")



import firebase_admin
from firebase_admin import auth, firestore

def create_user(email, password, username):
  try:
    user = auth.create_user(email=email, password=password)
    uid = user.uid
    user_data = {
        'username': username,
    }
    user_ref = firestore.client().collection('userdata').document(uid)
    user_ref.set(user_data)
    return uid
  except:
    return None  


def fetch_users():
  users_ref = db.reference("/users")
  users = users_ref.get()
  usernames = [user["username"] for user in users.values()]
  return usernames

# # fetch_users()
users = [doc.to_dict() for doc in users_ref.get()]

# print(users)

def fetch_messages(ref_id):
  r = DB.reference(ref_id)
  messages = r.get()
  return messages
  