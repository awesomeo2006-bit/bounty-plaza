from pymongo import MongoClient
from bcrypt import gensalt, hashpw, checkpw

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
users = db['users']

# Function to hash password
def hash_password(password):
    return hashpw(password.encode('utf-8'), gensalt())

# Function to verify password
def verify_password(stored_password, provided_password):
    return checkpw(provided_password.encode('utf-8'), stored_password)

# Function to create a new user
def create_user(username, password):
    hashed_password = hash_password(password)
    users.insert_one({'username': username, 'password': hashed_password})

# Function to authenticate a user
def authenticate_user(username, password):
    user = users.find_one({'username': username})
    if user and verify_password(user['password'], password):
        return True
    return False

# Example usage
create_user('admin', 'password123')
print(authenticate_user('admin', 'password123'))  # Should return True
print(authenticate_user('admin', 'wrongpassword'))  # Should return False