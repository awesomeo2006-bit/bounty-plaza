from pymongo import MongoClient
from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
users = db['users']

# Function to hash password
def hash_password(password):
    return generate_password_hash(password)

# Function to register a new user
def register_user(username, password):
    hashed_password = hash_password(password)
    user = {
        'username': username,
        'password': hashed_password
    }
    users.insert_one(user)

# Function to authenticate a user
def authenticate_user(username, password):
    user = users.find_one({'username': username})
    if user and check_password_hash(user['password'], password):
        return user
    return None

# Example usage
username = 'admin'
password = 'password123'

# Register a new user
register_user(username, password)

# Authenticate the user
authenticated_user = authenticate_user(username, password)
if authenticated_user:
    print('Authentication successful')
else:
    print('Authentication failed')