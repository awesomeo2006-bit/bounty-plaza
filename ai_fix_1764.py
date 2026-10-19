import bcrypt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
users = db['users']

# Function to hash password
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

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
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return True
    return False

# Example usage
register_user('admin', 'password123')
print(authenticate_user('admin', 'password123'))  # Should return True
print(authenticate_user('admin', 'wrongpassword'))  # Should return False