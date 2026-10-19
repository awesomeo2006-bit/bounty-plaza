from pymongo import MongoClient
from bcrypt import hashpw, gensalt

# Example function to authenticate user
def authenticate_user(username, password):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database']
    users = db['users']

    # Validate input
    if not isinstance(username, str) or not isinstance(password, str):
        return False

    # Fetch user document
    user_doc = users.find_one({'username': username})

    if not user_doc:
        return False

    # Verify password
    stored_password = user_doc['password']
    if hashpw(password.encode('utf-8'), stored_password) == stored_password:
        return True

    return False