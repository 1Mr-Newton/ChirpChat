# Import the required modules
import firebase_admin
import datetime
from firebase_admin import credentials, auth, db,firestore

# Initialize the Firebase SDK
# Load the service account key
cred = credentials.Certificate('chirpchat-23dba-firebase-adminsdk-kh0p1-529b03f269.json')

# Initialize the Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chirpchat-23dba-default-rtdb.firebaseio.com/'
})

db = firestore.client()

# print(auth.get_user_by_email('kwesi@gmail.com'))


# Function to create the user account
def create_user_account(email, password):
  try:
    user = auth.create_user(
        email=email,
        password=password
    )
    return user.uid
  except Exception as e:
    return None

# Function to store the user details
def store_user_details(user_id, email, username, date_of_birth):
    # Get a reference to the users node
    users_ref = db.reference().child('users')
    
    # Update the user information
    users_ref.child(user_id).update({
        'email': email,
        'username': username,
        'date_created': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })

# from firebase_admin import auth

def list_users():
    users = auth.list_users().iterate_all()
    for user in users:
        print("User ID:", user.uid)
        print("Email:", user.email)
        print("Display Name:", user.display_name)
        print("Phone Number:", user.phone_number)
        print("Email Verified:", user.email_verified)
        print("Disabled:", user.disabled)


# import firebase_admin
# from firebase_admin import db

def get_all_usernames():
    users_ref = db.reference("/userdata")
    users = users_ref.get()
    usernames = [user["username"] for user in users.values()]
    return usernames



def register(email, password, username, date_of_birth):
    # Use Firebase's authentication service to register the user
    user = auth.create_user_with_email_and_password(email, password)
    # Store the user's ID token in memory
    id_token = user['idToken']
    # Save the user's details to the database
    user_ref = db.collection('users').document(user['localId'])
    user_ref.set({
        'username': username,
        'date_of_birth': date_of_birth
    })
    # Return the user's ID token and details
    return id_token, {
        'username': username,
        'date_of_birth': date_of_birth
    }
import firebase_admin
from firebase_admin import auth

def create_user_with_username_and_dob(email, password, username, dob):
    user = auth.create_user(
        email=email,
        password=password,
        display_name=username,
        # set user metadata with custom claims
        user_metadata={
            "username": username,
            "dob": dob
        }
    )
    return user.uid



get_all_usernames()