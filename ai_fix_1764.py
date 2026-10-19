import bcrypt
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
collection = db['users']

def validate_input(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings")
    if not password.strip():  # Ensure password is not just whitespace
        raise ValueError("Password cannot be empty")

def hash_password(password):
    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def authenticate(username, password):
    validate_input(username, password)
    hashed_password = hash_password(password)
    query = {"username": username, "password": hashed_password}
    user = collection.find_one(query)
    return user