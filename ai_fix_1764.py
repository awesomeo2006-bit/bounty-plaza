import bcrypt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
users = db['users']

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def authenticate(username, password):
    user = users.find_one({'username': username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return user
    return None

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")

user = authenticate(username, password)
if user:
    print("Authentication successful!")
else:
    print("Authentication failed.")