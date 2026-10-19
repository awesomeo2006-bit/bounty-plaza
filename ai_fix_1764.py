import bcrypt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
users_collection = db['users']

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def authenticate_user(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Invalid input types")
    
    user = users_collection.find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return True
    return False

# Example usage
username = "admin"
password = "admin123"
hashed_password = hash_password(password)
users_collection.insert_one({"username": username, "password": hashed_password})

# Authenticate
is_authenticated = authenticate_user(username, password)
print("Authentication successful:", is_authenticated)