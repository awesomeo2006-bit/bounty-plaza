import bcrypt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
users = db['users']

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def authenticate(username, password):
    user = users.find_one({'username': username})
    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return user
    return None

# Example usage
username = "admin"
password = "admin_password"
hashed_password = hash_password(password)
users.insert_one({'username': username, 'password': hashed_password})

# Authenticate
authenticated_user = authenticate(username, password)
if authenticated_user:
    print("Authentication successful")
else:
    print("Authentication failed")