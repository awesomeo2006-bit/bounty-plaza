from pymongo import MongoClient
from bcrypt import hashpw, gensalt
from bson.objectid import ObjectId

# Example function to authenticate a user
def authenticate_user(username, password):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database']
    users = db['users']

    # Sanitize and validate inputs
    if not isinstance(username, str) or not isinstance(password, str):
        return False

    # Fetch user document
    user = users.find_one({'username': username})

    if user:
        # Compare hashed password
        if hashpw(password.encode('utf-8'), user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
            return True

    return False