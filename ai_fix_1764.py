from pymongo import MongoClient
from bcrypt import gensalt, hashpw, checkpw

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
users = db['users']

# Function to hash password
def hash_password(password):
    return hashpw(password.encode('utf-8'), gensalt())

# Function to register a new user
def register_user(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings")
    hashed_password = hash_password(password)
    users.insert_one({'username': username, 'password': hashed_password})

# Function to authenticate a user
def authenticate_user(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings")
    user = users.find_one({'username': username})
    if user and checkpw(password.encode('utf-8'), user['password']):
        return True
    return False

# Example usage
register_user('admin', 'password123')
print(authenticate_user('admin', 'password123'))  # Should return True
print(authenticate_user('admin', 'wrongpassword'))  # Should return False