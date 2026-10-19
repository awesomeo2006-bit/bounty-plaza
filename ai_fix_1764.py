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
    if not username or not password:
        raise ValueError("Username and password cannot be empty")
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings")
    hashed_password = hash_password(password)
    user = {
        "username": username,
        "password": hashed_password
    }
    users.insert_one(user)

# Function to authenticate a user
def authenticate_user(username, password):
    if not username or not password:
        raise ValueError("Username and password cannot be empty")
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings")
    user = users.find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return True
    return False

# Example usage
try:
    register_user("admin", "password123")
    if authenticate_user("admin", "password123"):
        print("Authentication successful")
    else:
        print("Authentication failed")
except ValueError as e:
    print(e)