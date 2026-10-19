import bcrypt
from pymongo import MongoClient

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def authenticate_user(username, password):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database']
    collection = db['users']

    # Validate input
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Invalid input")

    # Hash password
    hashed_password = hash_password(password)

    # Query database with parameterized query
    user = collection.find_one({"username": username, "password": hashed_password})
    if user:
        return True
    else:
        return False

# Example usage
username = "admin"
password = "admin123"
if authenticate_user(username, password):
    print("Authentication successful")
else:
    print("Authentication failed")