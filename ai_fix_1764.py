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

# Function to verify password
def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

# Example usage
username = "admin"
password = "secure_password123"

# Hash the password before storing
hashed_password = hash_password(password)
users.insert_one({"username": username, "password": hashed_password})

# Verify the password during login
login_password = "secure_password123"
user = users.find_one({"username": username})
if user and verify_password(user['password'], login_password):
    print("Login successful")
else:
    print("Login failed")